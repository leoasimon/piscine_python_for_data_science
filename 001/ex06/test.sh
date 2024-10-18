#! /bin/bash

# Define colors
RED="\033[31m"
GREEN="\033[32m"
RESET="\033[0m"

n_tests=$((`cat tests.txt | grep "\-\-\-" | wc -l`))

assert() {
	if [[ "$1" == "$2" ]];
	then
		echo -e "${GREEN}Success!${RESET}"
	else
		echo -e "${RED}Failed!${RESET}"
		echo "Expected: \"$2\", Actual: \"$1\""
	fi
}

echo "Happy path - python filterstring.py 'Hello the World' 4"
actual=$(python filterstring.py 'Hello the World' 4)
expected=$(echo "['Hello', 'World']")
assert "${actual}" "${expected}"

echo "Happy path - python filterstring.py 'Hello the World' 99"
actual=$(python filterstring.py 'Hello the World' 99)
expected=$(echo "[]")
assert $actual $expected

echo "AssertionError - python filterstring.py 3 'Hello the World'"
actual=$(python filterstring.py 3 'Hello the World')
expected=$(echo "AssertionError: the arguments are bad")
assert "${actual}" "${expected}"

echo "AssertionError - python filterstring.py"
actual=$(python filterstring.py)
expected=$(echo "AssertionError: the arguments are bad")
assert "${actual}" "${expected}"
