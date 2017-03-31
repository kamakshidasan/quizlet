#!/bin/bash

python download.py $1
python3 find_words.py word-list1.txt
python3 find_words.py word-list2.txt

rm 'sets/word-list1.txt'
rm 'sets/word-list2.txt'

mv 'sets/word-list1.csv' 'sets/'$1'-1.txt'
mv 'sets/word-list2.csv' 'sets/'$1'-2.txt'

echo 'Done! :)'

