#! /bin/bash

# Define colors
RED="\033[31m"
GREEN="\033[32m"
RESET="\033[0m"

test() {
	if [[ "$1" == "$2" ]];
	then
		echo -e "${GREEN}Success!${RESET}"
	else
		echo -e "${RED}Failed!${RESET}"
		echo "Expected: \"$1\", Actual: \"$2\""
	fi
}

echo "Happy path: python whatis.py 14"
out=$(python whatis.py 14)
expected="I'm Even."
test "$expected" "$out"

echo "Happy path: python whatis.py -5"
out=$(python whatis.py -5)
expected="I'm Odd."
test "$expected" "$out"

echo "No args: python whatis.py"
out=$(python whatis.py)
expected=""
test "$expected" "$out"
 
echo "Wrong argument: python whatis.py Hi!"
expected="AssertionError: argument is not an integer"
out=$(python whatis.py Hi!)
test "$expected" "$out"
 
echo "Too many args: python whatis.py 13 5"
expected="AssertionError: more than one argument is provided"
out=$(python whatis.py 13 5)
test "$expected" "$out"
