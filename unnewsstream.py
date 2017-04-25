from urllib.request import urlopen
import bs4
from bs4 import BeautifulSoup
import re
import time
counter=1

url= "http://unnewsstream.org/"


html_base=urlopen(url)
soup_base=BeautifulSoup(html_base,"html.parser")
newslinks=soup_base.findAll("div",{"class":"media-box news"})
for link in newslinks:
    html_news=urlopen(link.a.attrs['href'])
    soup_news=BeautifulSoup(html_news,"html.parser")
    
    date=link.find("div",{"class":"media-box-date"})
    date=date.text
    
    Headline=soup_news.findAll("h4",{"id":"story-headline"})
    Headline=Headline[0]
    
    print("Article" + str(counter) + " " + date + "-" + Headline.text)
    counter=counter+1

    Story=soup_news.findAll("div",{"id":"fullstory"})
    Story=Story[0]
    Story=Story.findAll("p")
    Story=Story[1:]
    for paragraphs in Story:
        print(paragraphs.text)
        
    time.sleep(5)
    
    
    
