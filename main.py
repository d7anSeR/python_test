import os
import string
from time import sleep

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}


def jobwith_url(p, link_page):
    url = link_page + "{p}/"
    req = requests.get(url, headers = headers)
    sleep(3)
    soup = BeautifulSoup(req.text, 'lxml')
    return soup


def make_dir():
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    if not os.path.isdir("dataset/good"):
        os.mkdir("dataset/good")
    if not os.path.isdir("dataset/bad"):
        os.mkdir("dataset/bad")


def download_review(data_good, data_bad, p, link_page):
    url_soup = jobwith_url(p, link_page)
    print(p)
    title_film = url_soup.find("h1", class_="breadcrumbs__head").text
    print(title_film)
    i = 0
    #review = url_soup.find('div', class_='reviewItem userReview')
    reviewsAll = url_soup.find_all("div", {"class": "reviewItem userReview"})
    for review in reviewsAll:
        i = +1
        print("[{i}]")
        feedback = review.find("span", {"class": "_reachbanner_"}).text
        if review.find('span', class_='yes') and data_good <= 1000:
            number = str(data_good+1).zfill(4)
            data_good = + 1
            with open(f'dataset/good/{number}.txt', 'wt') as f:
                f.seek(0)
                f.truncate(0)
                f.write(title_film + '\n' + feedback)
            pass
        if review.find('span', class_='no') and data_bad <= 1000:
            number = str(data_bad+1).zfill(4)
            data_bad = + 1
            with open(f'dataset/bad/{number}.txt', 'wt') as f:
                f.seek(0)
                f.truncate(0)
                f.write(title_film + '\n' + feedback)
            pass


def run(n, data_good, data_bad, link_page):
    make_dir()
    for p in range(1, n+1):
        download_review(data_good, data_bad, p, link_page)


if __name__ == '__main__':
    data_good = data_bad = 0
    run(41, data_good, data_bad,
        'https://www.kinopoisk.ru/film/435/reviews/ord/date/status/all/perpage/10/page/')

#film(27,data_good, data_bad, 'https://www.kinopoisk.ru/film/1294123/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/1294123/reviews/ord/rating/status/all/perpage/10/page/')
#film(13, data_good, data_bad, 'https://www.kinopoisk.ru/film/11130/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/11130/reviews/ord/rating/status/all/perpage/10/page/')
#film(7, data_good, data_bad, 'https://www.kinopoisk.ru/film/964318/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/964318/reviews/ord/rating/status/all/perpage/10/page/')
#film(55, data_good, data_bad, 'https://www.kinopoisk.ru/film/535341/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/535341/reviews/ord/rating/status/all/perpage/10/page/')
#film(237, data_good, data_bad, 'https://www.kinopoisk.ru/film/251733/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/251733/reviews/ord/rating/status/all/perpage/10/page/')
#film(119, data_good, data_bad, 'https://www.kinopoisk.ru/film/258687/reviews/', 'https://www.kinopoisk.ru/film/258687/reviews/ord/date/status/all/perpage/10/page/')
#film(30, data_good, data_bad, 'https://www.kinopoisk.ru/film/689/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/689/reviews/ord/rating/status/all/perpage/10/page/')
#film(102, data_good, data_bad, 'https://www.kinopoisk.ru/film/111543/reviews/ord/rating/', 'https://www.kinopoisk.ru/film/111543/reviews/ord/rating/status/all/perpage/10/page/')
print(data_bad, data_good)
