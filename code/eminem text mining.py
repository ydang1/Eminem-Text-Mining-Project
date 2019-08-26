# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:21:01 2019

@author: YIFAN DANG
"""
import pandas as pd
import numpy as np
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#data exploring
eminem=pd.read_csv('eminem_new.csv')
eminem=eminem.drop(columns='Unnamed: 0')
eminem.info()
eminem['Year']=eminem['Year'].astype('int64')

#Basic Feature Extraction
#Number of Words
eminem['word_count']=eminem['text'].apply(lambda x: len(str(x).split(' ')))
eminem=eminem.rename(columns={'Text_lenght':'Character_count'})


#average Word Length
def avg_text(data):
    data=data.split(' ')
    return(sum(len(i) for i in data)/len(data))
    
eminem['avg_text']=eminem['text'].apply(lambda x: avg_text(x))

#remove stopword
stop=stopwords.words('english')
eminem['stopwords']=eminem['text'].apply(lambda x:len([x for x in x.split(' ') if x in stop]))

#number of special characters
#hashtag
eminem['hashtag']=eminem['text'].apply(lambda x: len([x for x in str(x).split(' ') if x.startswith('#')]))
      
#number of numerics
eminem['numeric_count']=eminem['text'].apply(lambda x:len([x for x in x.split(' ')if x.isdigit()]))

#Number of Uppercase words
eminem['uppercase_count']=eminem['text'].apply(lambda x:len([x for x in x.split(' ')if x.isupper()]))


#Basic Pre-processing
##Lower Case
eminem['text']=eminem['text'].apply(lambda x: " ".join(x.lower() for x in x.split()))


##Removing Punctuation
eminem['text']=eminem['text'].str.replace('[^\w\s]','')

#Removal of Stop Words
eminem['text']=eminem['text'].apply(lambda x: ' '.join([x for x in x.split() if x not in stop]))

##Common word removal
freq_most=pd.Series(' '.join(eminem['text']).split()).value_counts()[:10]
freq_most=list(freq_most.index)
eminem['text']=eminem['text'].apply(lambda x:' '.join([x for x in x.split() if x not in freq_most]))

#Rare words removal
freq_least=pd.Series(' '.join(eminem['text']).split()).value_counts()[-10:]
freq_least=list(freq_least.index)
eminem['text']=eminem['text'].apply(lambda x: ' '.join([x for x in x.split() if x not in freq_least]))

#spelling correction
from textblob import TextBlob
#text_series=pd.Series(' '.join(eminem['text'][:3]).split()).value_counts()
#text_3=eminem['text'][:3].apply(lambda x: str(TextBlob(x).correct()))
#text_3=pd.Series(' '.join(text_3).split()).value_counts()

#Tokenization
TextBlob(eminem['text'][1]).words


#Stemming
from nltk.stem import PorterStemmer
st=PorterStemmer()
eminem['text']=eminem['text'].apply(lambda x: ' '.join([st.stem(word) for word in x.split()]))

##Lemmatization
from textblob import Word
eminem['text']=eminem['text'].apply(lambda x: ' '.join([Word(word).lemmatize() for word in x.split()]))


#Advance Text Processing
#N-grams
TextBlob(eminem['text'][0]).ngrams(2)


#Term frequency
tf1=(eminem['text']).apply(lambda x: pd.value_counts(x.split(' '))).sum(axis=0).reset_index()
tf1.columns=['words','tf']


#Inverse Document Frequency
for i,word in enumerate(tf1['words']):
    tf1.loc[i,'idf']=np.log(eminem.shape[0]/len(eminem[eminem['text'].str.contains(word)]))

#Term Frequency-Inverse Document Frequency(TF-IDF)
tf1['tfidf']=tf1['tf']*tf1['idf']    


##use sklearn to calculate TF and IDF
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(max_features=1000, lowercase=True, analyzer='word',stop_words='english',ngram_range=(1,1))
train_vect=tfidf.fit_transform(eminem['text'])
train_vect


##bag of words
from sklearn.feature_extraction.text import CountVectorizer
bow=CountVectorizer(max_features=1000, lowercase=True, ngram_range=(1,1), analyzer='word')
train_bow=bow.fit_transform(eminem['text'])
train_bow

#Sentiment Analysis
eminem['sentiment']=eminem['text'].apply(lambda x: TextBlob(x).sentiment[0])


#Word Embeddings
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file='glove.6B.100d.txt'
word2vec_output_file='glove.6B.100d.txt.word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)

#build predictive model
#split data
eminem_model=eminem[['text','sentiment']]
from sklearn.model_selection import train_test_split
X=eminem_model['text']
y=eminem_model['sentiment']
X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
y_train=y_train.reset_index()
y_train=y_train.drop(columns=['index'])
for i in range(len(y_train)):
    if y_train['sentiment'].iloc[i]>0:
         y_train['sentiment'].iloc[i]=1
    else:
        y_train['sentiment'].iloc[i]=0

y_test=y_test.reset_index()
y_test=y_test.drop(columns=['index'])
for i in range(len(y_test)):
    if y_test['sentiment'].iloc[i]>0:
         y_test['sentiment'].iloc[i]=1
    else:
        y_test['sentiment'].iloc[i]=0    
        
X_train=X_train.values
y_train=y_train.values
X_test=X_test.values
y_test=y_test.values
y_train=y_train.astype('int64')
y_test=y_test.astype('int64')
#Convert the text corpus into the feature vectors
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=1000, lowercase=True, analyzer='word',stop_words='english',ngram_range=(1,3))
train_vectors = vectorizer.fit_transform(X_train)
test_vectors = vectorizer.transform(X_test)
print(train_vectors.shape, test_vectors.shape)

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(train_vectors, y_train)

from sklearn.metrics import accuracy_score
predicted=clf.predict(test_vectors)
accuracy_score(y_test,predicted)










