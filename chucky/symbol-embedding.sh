#!/bin/bash

source chucky/chucky.conf

if [ -d "$BAG_OF_WORDS_DIR" ]; then
    printf 'Embedding already exists.\n'
    printf 'Exiting now.\n'
    exit 1
fi

#
# Identification of sinks and sources
#
echo "type:Symbol AND code:$SYMBOL" | \
lookup.py --attributes functionId | \
cut --fields=2 | \
awk '{printf("%s AND (type:IdentifierDeclType OR type:ParameterType OR type:Callee)\n", $1) }' | 
lookup.py --attributes functionId code | \
awk 'BEGIN { FS=OFS="\t" } { split($2,a,":"); split($3,b,":"); print a[2], b[2] }' | \
demux.py --outputDir $BAG_OF_WORDS_DIR

#
# Sink/Source Embedding
#
sally -q -n 1 --input_format=dir $BAG_OF_WORDS_DIR/data/ $BAG_OF_WORDS_DIR/embedding.libsvm --hash_file $BAG_OF_WORDS_DIR/feats.gz --vect_embed=tfidf
