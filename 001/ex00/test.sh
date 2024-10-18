#! /bin/bash

python Hello.py > out.txt

if diff out.txt expected.txt;
then
	echo "All good"
	rm out.txt
	exit 0
else
	echo "Error..."
	rm out.txt
	exit 1
fi
