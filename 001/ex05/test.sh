#! /bin/bash

# Define colors
RED="\033[31m"
GREEN="\033[32m"
RESET="\033[0m"

echo "Linting test"
if flake8 building.py;
then
	echo -e "${GREEN}Success!${RESET}"
else
	echo -e "${RED}Failed!${RESET}"
fi

echo "Testing with args"
for filename in arg*; do
	input=$(cat "$filename")
	cat "out.$filename" > expected.txt
	python building.py "$input" > actual.txt
	
	if diff expected.txt actual.txt;
	then                                      	
	 	echo -e "${GREEN}Success!${RESET}"
	else
	 	echo -e "${RED}Failed!${RESET}"
	fi
done

echo "Testing with stdin"
for filename in stdin*; do
	cat "out.$filename" > expected.txt
	cat "$filename" | python building.py > actual.txt
	
	if diff expected.txt actual.txt;
	then                                      	
	 	echo -e "${GREEN}Success!${RESET}"
	else
	 	echo -e "${RED}Failed!${RESET}"
	fi
done

rm expected.txt
rm actual.txt
