#!/bin/bash

source chucky/chucky.conf

if [ ! -f "$NEIGHBORS_FILE" ]; then
    printf 'No neighbors file found.\n'
    printf 'Run chucky/neighborhood-detection.sh first.\n'
    printf 'Exiting now.\n'
    exit 1

fi
if [ ! -d "$TAINT_DIR" ]; then
    printf 'No taint output found.\n'
    printf 'Run chucky/taint first.\n'
    printf 'Exiting now.\n'
    exit 1
fi

if [ -d "$FUNCTIONS_DIR" ]; then
    printf 'Function embedding already exists.\n'
    printf 'Exiting now.\n'
    exit 1
fi

#
# Condition extraction
#   1. Get tainted symbols of each neighbor function
#   2. Get conditions using those symbols
#
cat $NEIGHBORS_FILE | \
while read line; do
	ID=(${line##*:})
	KEY=$(grep -n $ID $TAINT_DIR/TOC | cut -d: -f1) ; (( KEY -= 1 ))
	SYMBOLS=$(cat $TAINT_DIR/data/$KEY | awk '{ printf("\"%s\",",$1) }' | sed 's/^/[/' | sed 's/,$/]\n/')
	printf "queryNodeIndex(\047%s AND type:Condition\047).as(\047condition\047).out(\047USE\047).filter{ $SYMBOLS.contains(it.code) }.back(\047condition\047).subTrees()\n" "$line"
done | \
lookup.py -g -a functionId code | \
awk 'BEGIN {FS="\t"; OFS="\t"} { split($2,a,":"); split($3,b,":"); print a[2] "\t" b[2] }' | \
demux.py --outputDir $FUNCTIONS_DIR

#
# Normalization
# TODO normalisation of return value (and arguments)
#
FILES="$FUNCTIONS_DIR/data/*"
for f in $FILES; do

	sed -i 's/\b[-+]*\([0-9]\+[ ][\*\/+-][ ]\)*[0-9]\+\b/$NUM/g' $f
	sed -i 's/! //g' $f
	sed -i 's/ == / $CMP /g' $f
	sed -i 's/ >= / $CMP /g' $f
	sed -i 's/ <= / $CMP /g' $f
	sed -i 's/ != / $CMP /g' $f
	sed -i 's/ > / $CMP /g' $f
	sed -i 's/ < / $CMP /g' $f

	KEY=${f##*/} ; (( KEY += 1 ))
	ID=$(cat $FUNCTIONS_DIR/TOC | sed -n "${KEY}p")
	ARGS=$(printf 'queryNodeIndex(\047functionId:%s AND code:%s AND type:Symbol\047).hasArguments().dedup()\n' "$ID" "$SYMBOL" | \
	lookup.py -g --attribute code | \
	awk '{ split($2,a,":"); print a[2] }')

	for arg in $ARGS; do
		sed -i 's/\b${arg}\b/\$ARG/g' $f
	done

	sort -u $f -o $f
done

#
# Embedding 
#
sally -q -n 1 --input_format=dir $FUNCTIONS_DIR/data/ $FUNCTIONS_DIR/embedding.libsvm --hash_file $FUNCTIONS_DIR/feats.gz --vect_embed=bin
