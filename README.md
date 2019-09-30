# Project Description
This is an individual project that I find very interesting. I Conducted text mining on Eminiem lyrics data set step by step. This project follows a very standard way of how to conduct text mining using python, including building a model for future prediction. text mining reference please see: https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/

# Dataset
Row: 500
Columns: 5 (text, Song, Album, Text_length, Year)

# Prerequistes
Tools:
Python (Anaconda Environment): https://www.anaconda.com/distribution/

# Running the tests
## 1. Data wangling:
The data contains a lot of missing value and the duplicated value such as the same song name with both uppoercase and lowercase need to be removed. 
```
import numpy as np
import pandas as pd
import os

os.chdir('C:/Users/yifan.000/Desktop/eminem')
eminem=pd.read_csv('eminem.csv')
eminem=eminem.drop(labels='Unnamed: 0',axis=1)
eminem.info()
#album_value=eminem['Album'].value_counts()
#album_year=eminem[-eminem['Album'].isnull()]
#album_year_nan=eminem[eminem['Album'].isnull()]
#album_year_missing=album_year[album_year.Year.isnull()]
#album_year_missing.Album.value_counts()
#album_year_missing=album_year_missing.reindex(range(len(album_year_missing)))
#miscellaneous=album_year_missing[album_year_missing.Album=='Miscellaneous']

'All Eyes pm Me': 2017
'The Marshall Mathers LP': 2000
'The Enminem Show': 2002
'The Slim Shady Lp': 1999
'Straight From The Vault EP': 2011
'Off the Wall': 2000
'Green Lantern ': 2003
'Whiteboy Wasted ': 2011
'Infinite': 1996
'8 Mile (Soundtrack)': 2002
'The Underground Collection': 1999
'SHADYXV': 2014
'Role Model / Cum on Everybody / 97 Bonnie &amp; Clyde': 1999
'Mockingbird': 2004
'The Marshall Mathers 2 (Deluxe Version)': 2013
'We Made You ':  2009
'Relapse (Deluxe Version)':2009
'Recovery vs. Thank Me Later Instrumentals' :2010 
'Cleanin Out My Closet':2002
'Remission': 2013
'The Marshall Mathers LP (Bonus Track Version)':2010
'Outta Control':2015
'The return of the 3 kingz (Volume 4)':2012
'Hellbound': 2005
'Stan': 2000
'The Evolution of Pac': 2009
'Crank Calls':
'The Man Not the Myth': 2009
'Guilty Conscience': 1999
'Road to Recovery: Withdrawal': 2010
'Fight Night': 
'Sing for the Moment': 2002
'Straight From the Vault, Volume 1': 2011
'The Marshall Mathers LP 2 Bonus Disc':2013
'Eminem &amp; Friendz - The Dirtiest Dozen (disc 1)':2002
'Xtreme Cardio Mix, Vol. 15 (60 Min Non-Stop Workout Mix) [140-150 BPM]':2004
'When Im Gone': 2005
'Slim Shday EP': 1997
'Best of Slim Shady':2012
'35 Top Hits: Workout Mixes, Volume 6':
'The return of the 3 kingz (Volume 5)':
'The Marshall Mathers LP2':2013
'Catch a Fade, Vol. 1':
'2005-04-28: Color Line Arena, Hamburg, Germany': 2005
'Like Toy Soldiers': 2004
'The Story of Marshall Mathers':   
'The Best Party of RnB 2011':
'bonus cd':
'Straight From the Lab EP': 2003  
'Bravo Hits 40':
'Return of the Psycho':2010
'Ass Like That':2004
'More Maximum Eminem':2002
'The Marshall Mathers LP - Tour Edition (International Version)': 2000
'Real Steel - Music From The Motion Picture': 2011
'The Showdown': 1999

def albumyear(data):
    for i in range(len(data)):
        if data.Album[i]=='All Eyes On Me':
            data.Year[i]=2017
        if data.Album[i]=='All Eyes on Me (The Eminem Files)':
            data.Year[i]=2017
        if data.Album[i]=='3 Kingz':
            data.Year[i]=2012
        if data.Album[i]=='35 Top Hits: Workout Mixes, Volume 6':
            data.Year[i]=2013
        if data.Album[i]=='The Marshall Mathers LP':
                    .
                    .
                    .
        if data.Song[i]=='untitled':
            data.Album[i]='Recovery'
            data.Year[i]=2010
    return data
        #if data.Song[i]=='

eminem_new=albumyear(eminem)        
eminem_new=eminem_new.drop_duplicates(subset=['text'])
eminem_new=eminem_new.drop_duplicates(subset=['Song'])           
eminem_new=eminem.dropna()

eminem_new.to_csv('eminem_new.csv')
```

## 2. text mining：
- Impot basic package and load data to pandas
```
import pandas as pd
import numpy as np
import os
os.chdir('D:eminem')
#data exploring
eminem=pd.read_csv('eminem_new.csv')
eminem=eminem.drop(columns='Unnamed: 0')
eminem.info()
eminem['Year']=eminem['Year'].astype('int64')

#Basic Feature Extraction
#Number of Words
eminem['word_count']=eminem['text'].apply(lambda x: len(str(x).split(' ')))
eminem=eminem.rename(columns={'Text_lenght':'Character_count'})
```
- Average Word Length
```
def avg_text(data):
    data=data.split(' ')
    return(sum(len(i) for i in data)/len(data))
    
eminem['avg_text']=eminem['text'].apply(lambda x: avg_text(x))
```
- Remove Stopword
```
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop=stopwords.words('english')
eminem['stopwords']=eminem['text'].apply(lambda x:len([x for x in x.split(' ') if x in stop]))
```
- Number of Special Characters
```
#number of special characters
#hashtag
eminem['hashtag']=eminem['text'].apply(lambda x: len([x for x in str(x).split(' ') if x.startswith('#')]))
```
- Number of Numerics
```
#number of numerics
eminem['numeric_count']=eminem['text'].apply(lambda x:len([x for x in x.split(' ')if x.isdigit()]))
```
- Number of Uppercase Words
```
#Number of Uppercase words
eminem['uppercase_count']=eminem['text'].apply(lambda x:len([x for x in x.split(' ')if x.isupper()]))
```
- Basic Pre-processing
```
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
```
#### Freq_most: ['im', 'like', 'dont', 'get', 'know', 'got', 'cause', 'back', 'shit', 'fuck']
#### Freq_least: ['peggin', 'curiosity', 'deaths', 'boones', 'sackltbr', 'melania', 'seavers', 'acclimated', 'heir', 'gossip']
#### Stopwords: ['i', 'me', 'my', 'myself', 'won', ..., "won't", 'wouldn', "wouldn't"]

### findings:
1. Eminem uses a lot of negative words such as 'shit','fuck'. The most least frequent words are those word which is hard to put in rap lyrics because it seems to be hard to rhyme the flow.
2. Eminem sounds contain total 179 stopwords, most of those stop words are in the same root but different stemming.(e.g."hadn't","hadn'","hasn't","haven'","haven't")

```
#Spelling Correction ( spelling correction is a useful pre-processing step because this also will help us in reducing multiple copies of words. For example, “Analytics” and “analytcs” will be treated as different words even if they are used in the same sense.)

#Tokenization
from textblob import TextBlob
TextBlob(eminem['text'][1]).words

#Stemming
from nltk.stem import PorterStemmer
st=PorterStemmer()
eminem['text']=eminem['text'].apply(lambda x: ' '.join([st.stem(word) for word in x.split()]))

#Lemmatization (Lemmatization is a more effective option than stemming because it converts the word into its root word, rather than just stripping the suffices. It makes use of the vocabulary and does a morphological analysis to obtain the root word. Therefore, we usually prefer using lemmatization over stemming.)
from textblob import Word
eminem['text']=eminem['text'].apply(lambda x: ' '.join([Word(word).lemmatize() for word in x.split()]))
```
- Advance Text Processing
```
#Term frequency
tf1=(eminem['text']).apply(lambda x: pd.value_counts(x.split(' ')))
tf1 = tf1.fillna(0)
tf1['total term'] = np.sum(tf1, axis = 1)
tf1 = tf1.iloc[:,:-1].div(tf1['total term'], axis = 0)

#inverse term frequency
IDF = pd.DataFrame()
for i, word in enumerate(tf1.columns):
    IDF.loc[i,'IDF'] = np.log(eminem.shape[0]/(len(eminem[eminem['text'].str.contains(word)])))
IDF = IDF.T.values
DF_IDF = tf1.mul(IDF, axis = 1)

    
#Inverse Document Frequency
for i,word in enumerate(tf1['words']):
    tf1.loc[i,'idf']=np.log(eminem.shape[0]/len(eminem[eminem['text'].str.contains(word)]))

#Term Frequency-Inverse Document Frequency(TF-IDF)
tf1['tfidf']=tf1['tf']*tf1['idf']    
```
- Use sklearn to calcuate TF andf IDF（less amount of code and less time complexity）
```
##use sklearn to calculate TF and IDF
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(max_features=1000, lowercase=True, analyzer='word',stop_words='english',ngram_range=(1,1))
train_vect=tfidf.fit_transform(eminem['text'])
train_vect
```
- Bag of Words (two similar text fields will contain similar kind of words, and will therefore have a similar bag of words. Further, that from the text alone we can learn something about the meaning of the document.)
``` 
##bag of words
from sklearn.feature_extraction.text import CountVectorizer
bow=CountVectorizer(max_features=1000, lowercase=True, ngram_range=(1,1), analyzer='word')
train_bow=bow.fit_transform(eminem['text'])
train_bow
```
- Sentiment Analysis
```
#Sentiment Analysis
eminem['sentiment']=eminem['text'].apply(lambda x: TextBlob(x).sentiment[0])
```
- Word Embeddings(Word Embedding is the representation of text in the form of vectors. The underlying idea here is that similar words will have a minimum distance between their vectors.)
```
# Word Embeddings
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file='glove.6B.100d.txt'
word2vec_output_file='glove.6B.100d.txt.word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)
```
-build a predictive model
```
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

- Convert the text corpus into the feature vectors
```
from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=1000, lowercase=True, analyzer='word',stop_words='english',ngram_range=(1,3))
train_vectors = vectorizer.fit_transform(X_train)
test_vectors = vectorizer.transform(X_test)
print(train_vectors.shape)

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(train_vectors, y_train)

from sklearn.metrics import accuracy_score
predicted=clf.predict(test_vectors)
accuracy_score(y_test,predicted)
```


  





















