#! /bin/bash

# Define colors
RED="\033[31m"
GREEN="\033[32m"
RESET="\033[0m"

assert() {
	if [[ "$1" == "$2" ]];
	then
		echo -e "${GREEN}Success!${RESET}"
	else
		echo -e "${RED}Failed!${RESET}"
		echo "Expected: \"$2\", Actual: \"$1\""
	fi
}

echo "Happy path - python sos.py 'sos'"
actual=$(python sos.py 'sos')
expected=$(echo "...  ---  ...")
assert "${actual}" "${expected}"

echo "-AssertionError - python sos.py 'h\$llo'"
actual=$(python sos.py 'h$llo')
expected=$(echo "AssertionError: the arguments are bad")
assert "${actual}" "${expected}"
