#!/bin/bash

print_config() {
	printf 'Target source/sink is           %s\n' "$SYMBOL"
	printf 'Target function is              %s\n' "$FUNCTION"
	printf 'Maximum number of neighbors is  %s\n' "$K"
}

check_config() {
	valid=$(printf 'functionId:%s AND type:Symbol AND code:%s' "$FUNCTION" "$SYMBOL" | lookup.py --attribute code | awk '{ split($2,a,":"); print a[2] }')
	if [ ! "$valid" = "$SYMBOL" ]; then
		printf 'The target function (id %s) does not use the symbol %s.\n' "$FUNCTION" "$SYMBOL"
		printf 'Check chucky/chucky.conf\n'
		printf 'Exiting now.\n'
		exit 1	
	fi
}

source chucky/chucky.conf

check_config
print_config

printf "Identification of sinkes and sources ...\n"
chucky/symbol-embedding.sh
printf "Neighborhood discovery ...\n"
chucky/neighborhood-discovery.sh
printf "Lightweight tainting ...\n"
chucky/taint.sh
printf "Embedding of functions ...\n"
chucky/function-embedding.sh
printf "Anomaly detection ...\n"
chucky/anomaly-detection.sh
