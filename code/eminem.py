# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:25:28 2019

@author: yifan
"""
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
            data.Year[i]=2000
        if data.Album[i]=='The Enminem Show':
            data.Year[i]=2002
        if data.Album[i]=='The Slim Shady LP':
            data.Year[i]=1999
        if data.Album[i]=='Straight From The Vault EP':
            data.Year[i]=2011
        if data.Album[i]=='Off the Wall':
            data.Year[i]=2000
        if data.Album[i]=='Green Lantern':
            data.Year[i]=2003
        if data.Album[i]=='The Slim Shady EP':
            data.Year[i]=1997
        if data.Album[i]=='Whiteboy Wasted':
            data.Year[i]=2011
        if data.Album[i]=='Infinite':
            data.Year[i]=1996
        if data.Album[i]=='8 Mile (Soundtrack)':
            data.Year[i]=2002
        if data.Album[i]=='SHADYXV':
            data.Year[i]=2014
        if data.Album[i]=='Mockingbird':
            data.Year[i]=2004
        if data.Album[i]=='The Marshall Mathers 2 (Deluxe Version)':
            data.Year[i]=2013
        if data.Album[i]=='We Made You':
            data.Year[i]=2009
        if data.Album[i]=='Relapse (Deluxe Version)':
            data.Year[i]=2009
        if data.Album[i]=='Recovery vs. Thank Me Later Instrumentals':
            data.Year[i]=2010
        if data.Album[i]=='Cleanin Out My Closet':
            data.Year[i]=2002
        if data.Album[i]=='Remission':
            data.Year[i]=2013
        if data.Album[i]=='The Marshall Mathers LP (Bonus Track Version)':
            data.Year[i]=2010
        if data.Album[i]=='Outta Control':
            data.Year[i]=2015
        if data.Album[i]=='The return of the 3 kingz (Volume 4)':
            data.Year[i]=2012
        if data.Album[i]=='Hellbound':
            data.Year[i]=2005
        if data.Album[i]=='Stan':
            data.Year[i]=2000
        if data.Album[i]=='The Evolution of Pac':
            data.Year[i]=2009
        if data.Album[i]=='The Man Not the Myth':
            data.Year[i]=2009
        if data.Album[i]=='Guilty Conscience':
            data.Year[i]=1999
        if data.Album[i]=='Road to Recovery: Withdrawal':
            data.Year[i]=2010
        if data.Album[i]=='Sing for the Moment':
            data.Year[i]=2002
        if data.Album[i]=='Straight From the Vault, Volume 1':
            data.Year[i]=2011
        if data.Album[i]=='The Marshall Mathers LP 2 Bonus Disc':
            data.Year[i]=2013
        if data.Album[i]=='Eminem &amp; Friendz - The Dirtiest Dozen (disc 1)':
            data.Year[i]=2002
        if data.Album[i]=='Best of Slim Shady':
            data.Year[i]=2012
        if data.Album[i]=='The Marshall Mathers LP2':
            data.Year[i]=2013
        if data.Album[i]=='2005-04-28: Color Line Arena, Hamburg, Germany':
            data.Year[i]=2005
        if data.Album[i]=='Like Toy Soldiers':
            data.Year[i]=2004
        if data.Album[i]=='Straight From the Lab EP':
            data.Year[i]=2003
        if data.Album[i]=='Return of the Psycho':
            data.Year[i]=2010
        if data.Album[i]=='Ass Like That':
            data.Year[i]=2004
        if data.Album[i]=='The Marshall Mathers LP - Tour Edition (International Version)':
            data.Year[i]=2000
        if data.Album[i]=='Real Steel - Music From The Motion Picture':
            data.Year[i]=2011
        if data.Album[i]=='The Showdown':
            data.Year[i]=1999
        if data.Album[i]=='bonus cd':
            data.Year[i]=2004
        if data.Album[i]=='The return of the 3 kingz (Volume 5)':         
            data.Year[i]=2006
        if data.Album[i]=='The Story of Marshall Mathers':         
            data.Year[i]=2006
        if data.Album[i]=='The Best Party of RnB 2011':         
            data.Year[i]=2002
        if data.Album[i]=='Pre Up':         
            data.Year[i]=2006
        if data.Album[i]=='More Maximum Eminem':         
            data.Year[i]=2002
        if data.Album[i]=="Cleanin' Out My Closet":         
            data.Year[i]=2002
        if data.Album[i]=="Bravo Hits 40":         
            data.Year[i]=2003
        if data.Album[i]=="Catch a Fade, Vol. 1":         
            data.Year[i]=2013
        if data.Album[i]=="Crank Calls":         
            data.Year[i]=2010
        if data.Album[i]=="When I'm Gone":         
            data.Year[i]=2010
        if data.Album[i]=="Compilation":         
            data.Year[i]=2014
        if data.Album[i]=="Fight Night":         
            data.Year[i]=2010  
        if data.Album[i]=='The Underground Collection':
            data.Year[i]=1999
        if data.Album[i]=='Xtreme Cardio Mix, Vol. 15 (60 Min Non-Stop Workout Mix) [140-150 BPM]':
            data.Year[i]=2014        
        if data.Album[i]=='Miscellaneous':
            data.Year[i]=2011
        if data.Album[i]=="Role Model / Cum on Everybody / '97 Bonnie &amp; Clyde":
            data.Year[i]=1999
        if '97 bonnie clyde' in data.Song[i]:
            data.Album[i]="Role Model / Cum on Everybody / '97 Bonnie &amp; Clyde" 
            data.Year[i]=1999
        if '8 mile' in data.Song[i]:
            data.Album[i]='Miscellaneous' 
            data.Year[i]=2011
        if data.Song[i]=='alchemist freestyle':
            data.Album[i]='Westwood Studio' 
            data.Year[i]=2014
        if data.Song[i]=='arose':
            data.Album[i]='Revival' 
            data.Year[i]=2017
        if 'ass like' in data.Song[i]:
            data.Album[i]='Encore' 
            data.Year[i]=2005
        if data.Song[i]=='believe':
            data.Album[i]='Revival' 
            data.Year[i]=2017
        if data.Song[i]=='berzerk':
            data.Album[i]='The Marshall Mathers LP 2' 
            data.Year[i]=2013
        if data.Song[i]=='biggie vs slim shady freestyle':
            data.Album[i]='First Word Freestyle' 
            data.Year[i]=1998
        if data.Song[i]=='bitch skit':
            data.Album[i]='The Slim Shady LP'
            data.Year[i]=1999
        if data.Song[i]=='brainless':
            data.Album[i]='The Marshall Mathers LP 2' 
            data.Year[i]=2013
        if data.Song[i]=='bullys pt 2':
            data.Album[i]='Straight from the Lab' 
            data.Year[i]=2003
        if data.Song[i]=='can i bitch':
            data.Album[i]='Straight from the Lab' 
            data.Year[i]=2003
        if data.Song[i]=='conglomerate':
            data.Album[i]='Westwood Studio' 
            data.Year[i]=2014
        if data.Song[i]=='curtains up':
            data.Album[i]='The Eminem Show' 
            data.Year[i]=2002
        if data.Song[i]=='detroit rap city':
            data.Album[i]='The People vs.' 
            data.Year[i]=2005
        if data.Song[i]=='dr west skit':
            data.Album[i]='Relapse'
            data.Year[i]=2009
        if data.Song[i]=='drop the bomb':
            data.Album[i]='Relapse'
            data.Year[i]=2009
        if data.Song[i]=='em calls paul skit':
            data.Album[i]='Encore'
            data.Year[i]=2004
        if data.Song[i]=='encore':
            data.Album[i]='encore' 
            data.Year[i]=2004
        if data.Song[i]=='evil twin':
            data.Album[i]='The Marshall Mathers LP 2' 
            data.Year[i]=2013
        if data.Song[i]=='evlenmeden olmaz':
            data.Album[i]='Oyun Senin' 
            data.Year[i]=2003
        if data.Song[i]=='final thought skit':
            data.Album[i]='Encore' 
            data.Year[i]=2004
        if data.Song[i]=='forever':
            data.Album[i]='Forever (International Version)' 
            data.Year[i]=2009
        if data.Song[i]=='framed':
            data.Album[i]='Revival' 
            data.Year[i]=2017
        if data.Song[i]=='fubba u cubba cubba':
            data.Album[i]='Anger Management 3' 
            data.Year[i]=2005
        if data.Song[i]=='get money':
            data.Album[i]='Straight From The Lab Part 2' 
            data.Year[i]=2011
        if data.Song[i]=='get to it':
            data.Album[i]='The Slim Shady LP' 
            data.Album[i]=1999
        if data.Song[i]=='girls limp bizkit diss':
            data.Album[i]="Devil's Night" 
            data.Year[i]=2001
        if data.Song[i]=='goodbye':
            data.Album[i]='The Eminem Show' 
            data.Song[i]=2002
        if data.Song[i]=='got u slippin':
            data.Album[i]='All Eyes on Me' 
            data.Year[i]=2017
        if data.Song[i]=='hazardous youth a cappella version':
            data.Album[i]='The Slim Shady LP' 
            data.Year[i]=1999
        if data.Song[i]=='heat':
            data.Album[i]='revival' 
            data.Year[i]=2017
        if data.Song[i]=='how come':
            data.Album[i]='D12 World' 
            data.Year[i]=2004
        if data.Song[i]=='i love you more':
            data.Album[i]='Encore' 
            data.Year[i]=2004
        if data.Song[i]=='i run rap massive trip blnd':
            data.Album[i]='Miscellaneous' 
            data.Year[i]=2011
        if data.Song[i]=='im alive':
            data.Album[i]='Relapse' 
            data.Year[i]=2009
        if data.Song[i]=='im shady':
            data.Album[i]='The Slim Shady LP' 
            data.Year[i]=1999
        if data.Song[i]=='in your head':
            data.Album[i]='Revival' 
            data.Year[i]=2017
        if data.Song[i]=='interlude':
            data.Album[i]='Revival' 
            data.Year[i]=2017
        if data.Song[i]=='introduction lose yourself':
            data.Album[i]='8 mile' 
            data.Year[i]=2002
        if data.Song[i]=='invasion':
            data.Album[i]='Shady Times: Invasion, Pt. 1' 
            data.Year[i]=2003
        if data.Song[i]=='invasion':
            data.Album[i]='Shady Times: Invasion, Pt. 1' 
            data.Year[i]=2003     
        if data.Song[i]=='jerk massive trip xclsv remix blnd':
            data.Album[i]='Relapse: Refill' 
            data.Year[i]=2009
        if i==326:
            data.Song[i]='just don t give a fuck'
        if data.Song[i]=='legacy':
            data.Album[i]='The Marshall Mathers LP 2' 
            data.Year[i]=2013
        if data.Song[i]=='rap god':
            data.Album[i]='The Marshall Mathers LP 2'
            data.Year[i]=2013
        if data.Song[i]=='quitter hit em up everlast diss':
            data.Album[i]='diss me diss you (CD1)'
            data.Year[i]=2014
        if data.Song[i]=='until i collapse':
            data.Album[i]='Real Steel'
            data.Year[i]=2002
        if data.Song[i]=='can a bitch':
            data.Album[i]='Straight from the lab'
            data.Year[i]=2003
        if data.Song[i]=='hail mary':
            data.Album[i]='The Massacre'
            data.Year[i]=2005
        if data.Song[i]=='rhyme or reason':
            data.Album[i]='The Marshall Mathers LP 2'
            data.Year[i]=2013
        if data.Song[i]=='still don t give a fk':
            data.Album[i]='The Slim Shady LP'
            data.Year[i]=1999
        if data.Song[i]=='let s go':
            data.Album[i]='The Eminem Show'
            data.Year[i]=2002
        if data.Song[i]=='patiantly waiting':
            data.Album[i]='Get Rich or Die Tryin'
            data.Year[i]=2003
        if data.Song[i]=='remind me intro':
            data.Album[i]='Revival'
            data.Year[i]=2017
        if data.Song[i]=='parking lot skit':
            data.Album[i]='The Marshall Mathers LP 2'
            data.Year[i]=2013
        if data.Song[i]=='just lose it album version':
            data.Album[i]='Encore'
            data.Year[i]=2004
        if data.Song[i]=='doe rae me':
            data.Album[i]='Straight from the lab'
            data.Year[i]=2003
        if data.Song[i]=='searchin':
            data.Album[i]='Infinite'
            data.Year[i]=1996
        if data.Song[i]=='we made you instrumental':
            data.Album[i]='Relapse'
            data.Year[i]=2009
        if data.Song[i]=='the watcher freestyle':
            data.Album[i]='The Marshall Mathers LP (Snippet Tape)'
            data.Year[i]=2000
        if data.Song[i]=='untouchable':
            data.Album[i]='Revival'
            data.Year[i]=2017
        if data.Song[i]=='my house':
            data.Album[i]='off the wall(2000)'
            data.Year[i]=2000
        if data.Song[i]=='my name is explicit version':
            data.Album[i]='The Slim Shady LP'
            data.Year[i]=1999
        if data.Song[i]=='castle':
            data.Album[i]='Revival'
            data.Year[i]=2017
        if data.Song[i]=='w e g o':
            data.Album[i]='Infinite'
            data.Song[i]=1996
        if data.Song[i]=='microphone':
            data.Album[i]='Westwood Studio'
            data.Year[i]=2010
        if data.Song[i]=='chonky fire':
            data.Album[i]='Westwood Studio'
            data.Year[i]=2010
        if data.Song[i]=='wee wee':
            data.Album[i]='Straight from the Vault EP'
            data.Year[i]=2011
        if data.Song[i]=='the people s champ intro':
            data.Album[i]='Straight from the Vault EP'
            data.Year[i]=2011
        if data.Song[i]=='the kiss':
            data.Album[i]='The Eminem Show'
            data.Year[i]=2002
        if data.Song[i]=='pills':
            data.Album[i]="Devil's Night"
            data.Year[i]=2002
        if data.Song[i]=='not afraid radio edit':
            data.Album[i]="Recovery"
            data.Year[i]=2010
        if data.Song[i]=='patiantly waiting':
            data.Album[i]="Get Rich or Die Tryin"
            data.Year[i]=2003
        if data.Song[i]=='im having a relapse new single':
            data.Album[i]="Get Rich or Die Tryin"
            data.Year[i]=2003 
        if data.Song[i]=='drug ballad exclu':
            data.Album[i]='The Marshall Mathers LP'
            data.Year[i]=2000 
        if data.Song[i]=='the warning mariah carey and nick cannon diss':
            data.Album[i]='Relapse'
            data.Year[i]=2009            
        if data.Song[i]=='offended':
            data.Album[i]='Revival'
            data.Year[i]=2017
        if data.Song[i]=='revival interlude':
            data.Album[i]='Revival'
            data.Year[i]=2017
        if data.Song[i]=='forget about dre':
            data.Album[i]='2001'
            data.Year[i]=1999
        if data.Song[i]=='remind me':
            data.Album[i]='revival'
            data.Year[i]=2017    
        if data.Song[i]=='the sauce benzino diss':
            data.Album[i]='Shady Times: Invasion, Pt. 1'
            data.Year[i]=2007          
        if data.Song[i]=='renegade':
            data.Album[i]='The Blueprint'
            data.Year[i]=2001                                 
        if data.Song[i]=='the real slim shady live':
            data.Album[i]='The Marshall Mathers LP'
            data.Year[i]=2000 
        if data.Song[i]=='stan live at radio 1':
            data.Album[i]='The Marshall Mathers LP'
            data.Year[i]=2000
            data.Year[i]=2000  
        if data.Song[i]=='no one s iller':
            data.Album[i]='The Slim Shady EP'
            data.Year[i]=1997                
        if data.Song[i]=='the way i am unedited version':
            data.Album[i]='The Marshall Mathers LP'
            data.Year[i]=2000                   
        if data.Song[i]=='pimp like me':
            data.Album[i]="Devil's Night"
            data.Year[i]=2001
        if data.Song[i]=='no love explicit':
            data.Album[i]="Recovery"
            data.Year[i]=2010
            data.Year[i]=2010       
        if data.Song[i]=='forever with drake kanye west lil wayne':
            data.Album[i]="Forever (International Version)"
            data.Year[i]=2009            
        if data.Song[i]=='mockingbird explicit version':
            data.Album[i]="Encore"
            data.Year[i]=2004   
        if data.Song[i]=='when the music stop':
            data.Album[i]="The Eminem Show"
            data.Year[i]=2002          
        if data.Song[i]=='shake that':
            data.Album[i]="Curtain Call: The Hits"
            data.Year[i]=2005
        if data.Song[i]=='shake that':
            data.Album[i]="Curtain Call: The Hits"
            data.Year[i]=2005
        if data.Song[i]=='without me radio edit':
            data.Album[i]="The Eminem Show"
            data.Year[i]=2002
        if data.Song[i]=='tonya skit':
            data.Album[i]="Relapse"
            data.Year[i]=2009           
        if data.Song[i]=='so far':
            data.Album[i]='The Marshall Mathers LP 2'
            data.Year[i]=2013            
        if data.Song[i]=='no one is iller':
            data.Album[i]='The Slim Shady EP'
            data.Year[i]=1997
        if data.Song[i]=='kids unedited version':
            data.Album[i]='The Marshall Mathers LP'
            data.Year[i]=2000                                                     
        if data.Song[i]=='intro eminem curtain call':
            data.Album[i]='The Slim Shady EP'
            data.Year[i]=1997                
        if data.Song[i]=='stronger than i was':
            data.Album[i]='The Marshall Mathers LP 2'
            data.Year[i]=2013
        if data.Song[i]=='so much better':
            data.Album[i]='The Marshall Mathers LP 2'
            data.Year[i]=2013             
        if data.Song[i]=='rhyme or reason':
            data.Album[i]='The Marshall Mathers LP 2'               
            data.Year[i]=2013
        if data.Song[i]=='untitled':
            data.Album[i]='Recovery'
            data.Year[i]=2010
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
