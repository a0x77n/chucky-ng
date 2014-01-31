#!/bin/bash

source chucky/chucky.conf

if [ -d "$BAG_OF_WORDS_DIR" ]; then
    printf 'Deleting directory %s ...\n' "$BAG_OF_WORDS_DIR"
    rm -rf "$BAG_OF_WORDS_DIR"
fi

if [ -d "$FUNCTIONS_DIR" ]; then
    printf 'Deleting directory %s ...\n' "$FUNCTIONS_DIR"
    rm -rf "$FUNCTIONS_DIR"
fi

if [ -d "$TAINT_DIR" ]; then
    printf 'Deleting directory %s ...\n' "$TAINT_DIR"
    rm -rf "$TAINT_DIR"
fi

if [ -f "$NEIGHBORS_FILE" ]; then
    printf 'Deleting file %s ...\n' "$NEIGHBORS_FILE"
    rm -f "$NEIGHBORS_FILE"
fi
