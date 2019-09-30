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
- impot basic package and load data to pandas
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
- average Word Length
```
def avg_text(data):
    data=data.split(' ')
    return(sum(len(i) for i in data)/len(data))
    
eminem['avg_text']=eminem['text'].apply(lambda x: avg_text(x))
```
- remove stopword
```
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop=stopwords.words('english')
eminem['stopwords']=eminem['text'].apply(lambda x:len([x for x in x.split(' ') if x in stop]))
```
- number of special characters
```
#number of special characters
#hashtag
eminem['hashtag']=eminem['text'].apply(lambda x: len([x for x in str(x).split(' ') if x.startswith('#')]))
```
- number of numerics
```
#number of numerics
eminem['numeric_count']=eminem['text'].apply(lambda x:len([x for x in x.split(' ')if x.isdigit()]))
```
- Number of Uppercase words
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








