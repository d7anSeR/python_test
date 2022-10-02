import os
import requests
from bs4 import BeautifulSoup
from time import sleep
URL = "https://www.kinopoisk.ru/film/435/reviews/"
html_text = requests.get(URL).text
soup = BeautifulSoup(html_text, 'html.parser')
i = 0
data = []
review = soup.find('div', class_= 'reviewItem userReview')
reviewsAll = soup.findAll('div', class_= 'reviewItem userReview')
len(reviewsAll)
for p in range(1, 11):
    print(p)
    url = f"https://www.kinopoisk.ru/film/435/reviews/ord/date/status/all/perpage/10/page/{p}/"

    req = requests.get(url)
    sleep(3)
    soup = BeautifulSoup(req.text, 'lxml')
    reviewsAll = soup.findAll('div', class_= 'reviewItem userReview')
    len(reviewsAll)
    for review in reviewsAll:
        feedback = soup.find('span', class_ ='_reachbanner_').text
        if soup.find('span', class_ = 'yes'):
          nature_review = '\good'
        if soup.find('span', class_ = 'no'):
          nature_review = '\bad'
        #wayfile = 'C:\dataset' + nature_review + i.zfill(4)
       # f = open(wayfile, 'w')
        data.append([nature_review, feedback])
    i += 1
len(data)