

import json
from collections import Counter
from pprint import pprint
with open('tweet_stream_NetNeutrality_10000.json') as infile:
    data = json.load(infile)

import string
content=[]
for item in data:
    if 'extended_tweet' in item:
        text = item['extended_tweet']['full_text']
        p = string.punctuation
        p+='…'
        p+='–'
        p+='—'
        table_p = str.maketrans(p, len(p) * " ")
        textdeal=text.translate(table_p).lower()    
        textword=textdeal.split()   
        textword=[x for x in textword if x != 'https' ]
        textword=[x for x in textword if x != 't' ]
        textword=[x for x in textword if x != 'co' ]
        textword=[x for x in textword if x != 'rt' ]
        content=content+textword
            
    else:
        text = item['text']
        p = string.punctuation
        p+='…'
        p+='–'
        p+='—'
        table_p = str.maketrans(p, len(p) * " ")
        textdeal=text.translate(table_p).lower()    
        textword=textdeal.split()
        textword=[x for x in textword if x != 'https' ]
        textword=[x for x in textword if x != 't' ]
        textword=[x for x in textword if x != 'co' ]
        textword=[x for x in textword if x != 'rt' ]
        content=content+textword
        
import nltk
# get frequent words
freq = nltk.FreqDist(content)
print(type(freq))
#freq.
freq.plot(10)


stopwords = nltk.corpus.stopwords.words('english')
stopwords.append('go')
stopwords.append('get')
stopwords.append('let')
stopwords.append('without')
stopwords.append('can’t')
stopwords.append('amp')
words2 = [w for w in content if w not in stopwords and len(w) > 1]
freq2 = nltk.FreqDist(words2)
freq2.plot(10)

import string
content=[]
#mention_list = []
for item in data:
    if 'extended_tweet' in item:
        text = item['extended_tweet']['full_text']
        p = string.punctuation
        p+='…'
        p+='–'
        p+='—'
        table_p = str.maketrans(p, len(p) * " ")
        textdeal=text.translate(table_p).lower()    
        textword=textdeal.split()   
        textword=[x for x in textword if x[0] == '#' and x != '#']
        content=content+textword
        
    else:
        text = item['text']
        p = string.punctuation
        p+='…'
        p+='–'
        p+='—'
        p = p.replace("#", "")
        table_p = str.maketrans(p, len(p) * " ")
        textdeal=text.translate(table_p).lower()    
        textword=textdeal.split()
        textword=[x for x in textword if x[0] == '#' and x != '#']
        content=content+textword

import nltk
# get frequent words
freq = nltk.FreqDist(content)
print(type(freq))
#freq.
freq.plot(10)

stopwords=[]
stopwords.append('#netneutraility')
stopwords.append('#netneutralityِ')
stopwords.append('#netnuetrality')
stopwords.append('#netn')
words2 = [w for w in content if w not in stopwords and len(w) > 1]
freq2 = nltk.FreqDist(words2)
freq2.plot(10)

import string
content=[]
#mention_list = []
for item in data:
    if 'extended_tweet' in item:
        text = item['extended_tweet']['full_text']
        p = string.punctuation
        p+='…'
        p+='–'
        p+='—'
        p = p.replace("@", "")
        table_p = str.maketrans(p, len(p) * " ")
        textdeal=text.translate(table_p).lower()    
        textword=textdeal.split()   
        textword=[x for x in textword if x[0] == '@' and x != '@']
        content=content+textword
        
    else:
        text = item['text']
        p = string.punctuation
        p+='…'
        p+='–'
        p+='—'
        p = p.replace("@", "")
        table_p = str.maketrans(p, len(p) * " ")
        textdeal=text.translate(table_p).lower()    
        textword=textdeal.split()
        textword=[x for x in textword if x[0] == '@' and x != '@']
        content=content+textword

import nltk
# get frequent words
freq = nltk.FreqDist(content)
print(type(freq))
#freq.
freq.plot(10)


counter ={}
for item in data:
    user=item['user']
    if user['screen_name'] in counter:
        counter[user['screen_name']]+=1
    else:
        counter[user['screen_name']]=1
name=max(counter, key=counter.get)
number=counter[name]
print('The user '+name+' is the most frequently tweeting person, he has tweeted '
      +str(number)+' tweets.')

influence=[]
for item in data:
    quote_count=item['quote_count']
    reply_count=item['reply_count']
    retweet_count=item['retweet_count']
    influence.append(quote_count+reply_count+retweet_count)
print(max(influence))


