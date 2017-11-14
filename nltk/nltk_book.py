from __future__ import division
import nltk, re, pprint
from urllib import urlopen
from nltk.book import *
from nltk.corpus import brown
from nltk.corpus import gutenberg
from nltk.corpus import webtext
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from operator import itemgetter
import codecs

#Chapter 1
text1.concordance("touching")
text3.dispersion_plot(['touching','there','land'])
fdist1 = FreqDist(text1)
vocabulary1 = fdist1.keys()
vocabulary1['touching']
sorted([w for w in set(text5) if lwn(w) > 7 and FreqDist(text5) >7])
#useful string function on page 23
[word.lower() for word in text1 if word.isalpha()]
#NLP: Disambiguation / Pronoun Resolution / Translation / Generating Output

#Chapter 2
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
#summary program on page 40 and useful corpus functions are on page 50
#load local text on page 51
nltk.bigran(sent7)
#conditional frequency functions are on page 56
wn.synsets('car')
wn.synset('car.n.01').lemma_names

#Chapter 3
url = 'http://www.gutenberg.org/files/2254/2254.txt'
raw = urlopen(url).read()
raw = ntlk.clean_html(urlopen(url).read())
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
#string methods are on page 92
f = codecs.open(path, encoding='latin2')
#regular expressions on page 101
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', 'processes')
moby.findall(r"<a> (<.*>) <man>")
#use stemmers to normalize text
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
[porter.stem(t) for t in tokens]
#use lemmatization to normalize text
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens]
#tokenization by white space
re.split(r'[ \t\n]+', raw)
#tokenization by non-word
re.split(r' \W+', raw)
#tokenization for words with punctuations
re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw)
#regular expression symbols are on page 111
nltk.regexp_tokenize(text, pattern)
#segmentation is a complex problem: sentence segmentation & word segmentation
print('%s -> %d;' % ('haha',3))
print('%-*s -> %d' % (6, 'dog', 3))
#write text to a file
output_file = open('output.txt', 'w')
for word in words:
    output_file.write(word + '\n')
output_file.write(str(len(words)) + '\n')
output_file.close()
#use textwrap package for text wrapping

#Chapter 4
#weird assignment on page 131
all(len(w) > 4 for w in words)
#useful loops on page 135
training_data, test_data = text[:cut], text[cut:]
#sort words in a string by their length
words = 'I turned off the spedsdsd'.split()
wordlens = [(len(word),word) for word in words]
wordlens.sort()
' '.join(w for (_, w) in wordlens)
#parameters checking
assert isinstance(word, basestring), "argument must be a string"
#weird function bug on page 157
b is c
b == c

#Chapter 5
nltk.pos_tag(text)
#simplified POS tagset on page 183
sorted(set(b for (a,b) in nltk.ibigrams(brown_learned_text) if a == 'often'))
tags = [b[1] for (a, b) in nltk.ibigrams(brown_Irnd_tagged) if a[0] == 'often']
fd = ntlk.FreqDist(tags)
pos.keys()
pos.values()
pos = nltk.defaultdict(lambda: 'N')
sorted(counts.items(), key=itemgetter(1), reverse=True)
#inverting a dictionary
pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V'}
pos2 = dict((value, key) for (key, value) in pos.items())
#dictionary methods summary is on page 198
bigram_tagger = nltk.BigramTagger(train_sents)
bigram_tagger.tag(brown_sents[2007])
#tagging: default tagger, regex tagger, unigram tagger and n-gram tagger
#we can set backoff to combine taggers

#Chapter 6
#A simple decision tree model is on page 229
#A naive bayes model is on page 235
#Precision: TP/(TP+FP) / Recall: TP/(TP+FN)
#Naive Bayes is on page 248

#Chapter 7
#information extraction architecture is on page 263
sentences = nltk.sent_tokenize(document)
sentences = [nltk.word_tokenize(sent) for sent in sentences]
sentences = [nltk.pos_tag(sent) for sent in sentences]
#tree representation of chunk structures is on page 270
#a tree structure example is on page 280
#need to know how chunkers work

#Chapter 8 - 11
#syntatic categories can be found on page 298
#an example of WFST table is shown on page 308
#sentences have internal organization that can be represented using a tree
#definitions of recursice descent parser and shift-reduce parser are on page 321
#construct dictionary to represent grammar feature in lexical level
#build meaning representations compositionally, use supplement first-order logic
#a closed expression is one that has no free variables
