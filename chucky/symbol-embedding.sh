#!/bin/bash

source chucky/chucky.conf
check_config

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
cut -f2 | \
awk '{printf("queryNodeIndex( \047%s\047 ).filter{ it.type == \047IdentifierDeclType\047 || it.type == \047ParameterType\047 || ( it.type == \047Identifier\047 && it.in.has( \047type\047, \047CallExpression\047 ) ) }\n", $1); }' | \
lookup.py -g -a functionId code | \
awk 'BEGIN { FS=OFS="\t" } { split($2,a,":"); split($3,b,":"); print a[2], b[2] }' | \
demux.py --outputDir $BAG_OF_WORDS_DIR

#
# Sink/Source Embedding
#
sally -q -n 1 --input_format=dir $BAG_OF_WORDS_DIR/data/ $BAG_OF_WORDS_DIR/embedding.libsvm --hash_file $BAG_OF_WORDS_DIR/feats.gz --vect_embed=tfidf
