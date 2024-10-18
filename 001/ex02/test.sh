#! /bin/bash

# Define colors
RED="\033[31m"
GREEN="\033[32m"
RESET="\033[0m"

python tester.py > out.txt

if diff out.txt expected.txt;
then
   echo -e "${GREEN}Success!${RESET}" 
   exit 0
else
    echo -e "${RED}Test failed :${RED}"
    exit 1
fi
