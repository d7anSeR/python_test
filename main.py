import os
import string
from time import sleep

import requests
from bs4 import BeautifulSoup


def film(n, data_good, data_bad, link_site, link_page):
    URL = link_site
    html_text = requests.get(URL).text
    sleep(8)
    soup = BeautifulSoup(html_text, features="lxml")
    review = soup.find('div', class_='reviewItem userReview')
    title_film = soup.find("a", {"class": "breadcrumbs__link"}).text
    for p in range(1, n):
        url = link_page+"{p}/"
        req = requests.get(url)
        sleep(5)
        soup = BeautifulSoup(req.text, 'lxml')
        reviewsAll = soup.findAll("div", {"class": "reviewItem userReview"})
        print(len(reviewsAll))
        for review in reviewsAll:
            feedback = review.find("span", {"class": "_reachbanner_"}).text
            print(feedback)
            if review.find('span', class_='yes'):
                if(data_good < 1000):
                    number = chr(data_good+1).zfill(4)
                    data_good + 1
                    with open(r"C:\Users\Professional\.vscode\python_test\dataset\good\{number}.txt", 'a') as f:
                        f.write(title_film)
                        f.write('\n')
                        f.write(feedback)
                    pass       
            if review.find('span', class_='no'):
                if(data_bad < 1000):
                    number = chr(data_bad+1).zfill(4)
                    data_bad + 1
                    with open(r"C:\Users\Professional\.vscode\python_test\python_test\python_test\dataset\bad\{number}.txt", 'a') as f:
                        f.write(title_film)
                        f.write('\n')
                        f.write(feedback)
                    pass
data_good = data_bad = 0
film(41,data_good, data_bad, 'https://www.kinopoisk.ru/film/435/reviews/', 'https://www.kinopoisk.ru/film/435/reviews/ord/date/status/all/perpage/10/page/')
film(27,data_good, data_bad, 'https://www.kinopoisk.ru/film/1294123/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/1294123/reviews/ord/rating/status/all/perpage/10/page/')
film(13, data_good, data_bad, 'https://www.kinopoisk.ru/film/11130/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/11130/reviews/ord/rating/status/all/perpage/10/page/')
film(7, data_good, data_bad, 'https://www.kinopoisk.ru/film/964318/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/964318/reviews/ord/rating/status/all/perpage/10/page/')
film(55, data_good, data_bad, 'https://www.kinopoisk.ru/film/535341/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/535341/reviews/ord/rating/status/all/perpage/10/page/')
film(237, data_good, data_bad, 'https://www.kinopoisk.ru/film/251733/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/251733/reviews/ord/rating/status/all/perpage/10/page/')
film(119, data_good, data_bad, 'https://www.kinopoisk.ru/film/258687/reviews/', 'https://www.kinopoisk.ru/film/258687/reviews/ord/date/status/all/perpage/10/page/')
film(30, data_good, data_bad, 'https://www.kinopoisk.ru/film/689/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/689/reviews/ord/rating/status/all/perpage/10/page/')
film(102, data_good, data_bad, 'https://www.kinopoisk.ru/film/111543/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/111543/reviews/ord/rating/status/all/perpage/10/page/')
print(data_bad, data_good)