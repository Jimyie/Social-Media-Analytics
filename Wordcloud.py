#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:03:41 2017

@author: Jimmy Lu
"""
import json
from collections import Counter 
stemlst = []
with open('tweet_stream_NetNeutrality_10000.json') as infile:
    data = json.load(infile)

import string
p = string.punctuation
p+='…'
p+='–'
p+='—'
table_p = str.maketrans(p, len(p) * " ")
import nltk
stopwords = nltk.corpus.stopwords.words('english')
stopwords.append('go')
stopwords.append('amp')
stopwords.append('let')
stopwords.append('https')
stopwords.append('t')
stopwords.append('co')
stopwords.append('rt')

content=[]
for item in data:
    if 'extended_tweet' in item:
        text = item['extended_tweet']['full_text']
        p = string.punctuation
        textdeal=text.translate(table_p).lower()    
        textword=textdeal.split()   
        textword=[x for x in textword if x not in stopwords ]
        content=content+textword
            
    else:
        text = item['text']
        textdeal=text.translate(table_p).lower()    
        textword=textdeal.split()
        textword=[x for x in textword if x not in stopwords ]
        content=content+textword

from wordcloud import WordCloud
import matplotlib.pyplot as plt

st = list(Counter(content).most_common(100))




# convert list to string
file1 =''
for word in st:
    file1 += ' {}'.format(word)

q="'"
table_q = str.maketrans(q, len(q) * " ")
file2 = file1.translate(table_q)
# Generate a word cloud image

wordcloud = WordCloud(max_font_size=40).generate(file2) 

# Display the generated image:
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#reference to change size :https://stackoverflow.com/questions/28786534/increase-resolution-with-word-cloud-and-remove-empty-border