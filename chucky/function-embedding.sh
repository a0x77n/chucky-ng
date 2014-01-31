#!/bin/bash

source chucky/chucky.conf

if [ ! -f "$NEIGHBORS_FILE" ]; then
    printf 'No neighbors file found.\n'
    printf 'Run chucky/neighborhood-detection.sh first.\n'
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
#
cat $NEIGHBORS_FILE | \
awk -v s=$SYMBOL '{
	printf("symbols = queryNodeIndex(\047%s AND code:%s AND type:Symbol\047).taint().toList();",$1,s)
	printf("queryNodeIndex(\047%s AND type:Condition\047).as(\047condition\047).out(\047USE\047).retain(symbols).back(\047condition\047).subTrees()\n",$1)
}' | \
traversal.py -a functionId code | \
awk 'BEGIN {FS="\t"; OFS="\t"} { split($2,a,":"); split($3,b,":"); print a[2] "\t" b[2] }' | \
demux.py --outputDir $FUNCTIONS_DIR

#
# Normalization
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

	KEY=${f##*/}
	(( KEY += 1 ))
	ID=$(cat $FUNCTIONS_DIR/TOC | sed -n "${KEY}p")
	ARGS=$(printf 'queryNodeIndex(\047functionId:%s AND code:%s AND type:Symbol\047).hasArguments().dedup()\n' "$ID" "$SYMBOL" | \
	
	python/query.py --attribute code | \
	awk '{ split($2,a,":"); print a[2] }')

	for arg in $ARGS; do
		sed -i "s/\b${arg}\b/\$ARG/g" $f
	done

	sort -u $f -o $f
done

#
# Embedding 
#
sally -q -n 1 --input_format=dir $FUNCTIONS_DIR/data/ $FUNCTIONS_DIR/embedding.libsvm --hash_file $FUNCTIONS_DIR/feats.gz --vect_embed=bin
