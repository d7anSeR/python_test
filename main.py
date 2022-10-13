import os
from time import sleep

import requests
from bs4 import BeautifulSoup

URL = 'https://www.kinopoisk.ru/film/435/reviews/'
html_text = requests.get(URL).text
sleep(1)

soup = BeautifulSoup(html_text, features="lxml")
i = 0
review = soup.find('div', class_='reviewItem userReview')
reviewsAll = soup.findAll("div", {"class": "reviewItem userReview"})
print(len(reviewsAll))
title_film = soup.find("a", {"class": "breadcrumbs__link"})
print(title_film)
i = 0
for p in range(1, 46):
    url = f"https://www.kinopoisk.ru/film/435/reviews/ord/date/status/all/perpage/10/page/{p}/"
    req = requests.get(url)
    sleep(3)
    soup = BeautifulSoup(req.text, 'lxml')
    for r in reviewsAll:
        feedback = soup.find('span', class_='_reachbanner_').text
        if soup.find('span', class_='yes'):
            number = (i+1).zfill(4)
            with open('dataset/good/{number}.txt', mode = 'w') as f:
                f.write(title_film)
                f.write('\n')
                f.write(feedback)
            pass
        if soup.find('span', class_='no'):
            number = (i+1).zfill(4)
            with open('dataset/bad/{number}.txt', mode = 'w') as f:
                f.write(title_film)
                f.write('\n')
                f.write(feedback)
            pass
        i += 1
print("done")
