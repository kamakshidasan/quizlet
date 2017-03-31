from bs4 import BeautifulSoup
import requests
import sys
import csv
import quizlet
import os
import re

filePath = os.path.join(quizlet.SET_DIR, sys.argv[1])

with open(filePath) as f:
    words = f.readlines()

words = [x.strip() for x in words]

for word in words:
	
	word = word.lower()
	page = requests.get('http://wordsinasentence.com/'+word+'-in-a-sentence/', verify=False)
	soup = BeautifulSoup(page.content, 'html.parser')
	paragraphs = soup.findAll('p')

	try:
		meaning = paragraphs[1].get_text().capitalize().strip()
		replacement_word = len(word)* '_'
	
		sentence1 = paragraphs[3].get_text().strip()
		sentence2 = paragraphs[4].get_text().strip()
		sentence3 = paragraphs[5].get_text().strip()

		replacement = re.compile(re.escape(word), re.IGNORECASE)

		sentence1 = replacement.sub(replacement_word, sentence1)
		sentence2 = replacement.sub(replacement_word, sentence2)
		sentence3 = replacement.sub(replacement_word, sentence3)

		text = meaning + '\n\n' + sentence1 + '\n\n' + sentence2 + '\n\n' + sentence3 + '||'

		setFilename = sys.argv[1]
		currentFileName = os.path.splitext(sys.argv[1])[0] + '.csv'
		setPath = os.path.join(quizlet.SET_DIR, currentFileName)

		f = open(setPath, 'a')
		f.write(word + '|' + text + '\n')
		f.close()

		print ('Found: ', word)

	except:
			setPath = os.path.join(quizlet.SET_DIR, 'words-not-found.txt')
			fd = open(setPath, 'a')
			fd.write(word + '\n')
			fd.close()
			print ('Not Found: ', word)
print (sys.argv[1], " Done!")
