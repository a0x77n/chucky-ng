#!/bin/bash

source chucky/chucky.conf

if [ ! -d "$BAG_OF_WORDS_DIR" ]; then
   	printf 'No embedding found at %s.\n' "$BAG_OF_WORDS_DIR"
	printf 'Run chucky/symbol-embedding.sh first.\n'
	printf 'Exiting now.\n'
	exit 1
fi

if [ -f "$NEIGHBORS_FILE" ]; then
	printf 'Neighbor file already exists.\n'
	printf 'Exiting now.\n'
	exit 1
fi

#
# Neighborhood discovery
#
echo $FUNCTION | knn.py -k $K --dirname $BAG_OF_WORDS_DIR | awk '{ print "functionId:" $1 }' > $NEIGHBORS_FILE
