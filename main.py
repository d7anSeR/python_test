import os

from bs4 import BeautifulSoup

import requests
from time import sleep
from random import randint 


URL = 'https://www.kinopoisk.ru/film/435/reviews/'
html_text = requests.get(URL).text
sleep(randint(3,10))

soup = BeautifulSoup(html_text, features = "lxml")
i = 0
data = []
review = soup.find('div', class_= 'reviewItem userReview')
reviewsAll = soup.findAll("div", {"class":"reviewItem userReview"})
print(len(reviewsAll))
p = 1
for p in range(1, 46):
    url = f"https://www.kinopoisk.ru/film/435/reviews/ord/date/status/all/perpage/10/page/{p}/"
    req = requests.get(url)
    sleep(3)
    i = 0
    soup = BeautifulSoup(req.text, 'lxml')
    for review in reviewsAll:
        #feedback = soup.find('span', class_ ='_reachbanner_').text
        if soup.find('span', class_ = 'yes'):
          nature_review = '\good'
        if soup.find('span', class_ = 'no'):
          nature_review = '\bad'
        #wayfile = 'C:\dataset' + nature_review + i.zfill(4)
        #f = open(wayfile, 'w')
        data.insert(i, i)
        i += 1
print(data)