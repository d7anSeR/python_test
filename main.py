import os
import string
from time import sleep

import requests
from bs4 import BeautifulSoup
import codecs


def make_dir():
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    if not os.path.isdir("dataset/good"):
        os.mkdir("dataset/good")
    if not os.path.isdir("dataset/bad"):
        os.mkdir("dataset/bad")


def review_good(data_good, pages, link_page):
    for page in range(1, pages+1):
        print(page)
        url = link_page + f"{pages}/"
        sleep(30 + 2*pages)
        req = requests.get(url)
        req.encoding = 'UTF-8'
        soup = BeautifulSoup(req.text, 'lxml')
        try:
            title_film = soup.find("a", class_="breadcrumbs__link").text
        except:
            print("error when parsng the website")
        reviewsAll = soup.findAll("div", class_="response good")
        for review in reviewsAll:
            feedback = review.find("span", {"class": "_reachbanner_"}).text
            if data_good <= 1000:
                number = str(data_good+1).zfill(4)
                data_good += 1
            try:
                with codecs.open(f'dataset/good/{number}.txt', 'w', "utf-8") as f:
                    f.write(title_film + '\n' + feedback)
                pass
            except:
                print("Error open file")
    return data_good


def review_bad(data_bad, pages, link_page):
    for page in range(1, pages+1):
        print(page)
        url = link_page + f"{pages}/"
        sleep(30 + 2*pages)
        req = requests.get(url)
        req.encoding = 'UTF-8'
        soup = BeautifulSoup(req.text, 'lxml')
        try:
            title_film = soup.find("a", class_="breadcrumbs__link").text
        except:
            print("error when parsng the website")
        reviewsAll = soup.findAll("div", class_="response bad")
        for review in reviewsAll:
            feedback = review.find("span", {"class": "_reachbanner_"}).text
            if data_bad <= 1000:
                number = str(data_bad+1).zfill(4)
                data_bad += 1
            try:
                with codecs.open(f'dataset/bad/{number}.txt', 'w', "utf-8") as f:
                    f.write(title_film + '\n' + feedback)
                pass
            except:
                print("Error open file")
    return data_bad


def run(n, _data_good, _data_bad, link_page):
    make_dir()
    _data_good = review_good(_data_good, n, link_page)
    _data_bad = review_bad(_data_bad, n, link_page)
    return _data_good, _data_bad


if __name__ == '__main__':
    _data_good = _data_bad = 0
    _data_good = _data_bad = run(
        27, _data_good, _data_bad, 'https://www.kinopoisk.ru/film/1294123/reviews/ord/rating/status/all/perpage/10/page/')
    _data_good = _data_bad = run(
        13, _data_good, _data_bad, 'https://www.kinopoisk.ru/film/11130/reviews/ord/rating/status/all/perpage/10/page/')
    _data_good = _data_bad = run(
        7, _data_good, _data_bad, 'https://www.kinopoisk.ru/film/964318/reviews/ord/rating/status/all/perpage/10/page/')
    _data_good = _data_bad = run(
        55, _data_good, _data_bad, 'https://www.kinopoisk.ru/film/535341/reviews/ord/rating/status/all/perpage/10/page/')
    _data_good = _data_bad = run(
        237, _data_good, _data_bad, 'https://www.kinopoisk.ru/film/251733/reviews/ord/rating/status/all/perpage/10/page/')
    _data_good = _data_bad = run(
        119, _data_good, _data_bad, 'https://www.kinopoisk.ru/film/258687/reviews/ord/date/status/all/perpage/10/page/')
    _data_good = _data_bad = run(
        30,  _data_good, _data_bad, 'https://www.kinopoisk.ru/film/689/reviews/ord/rating/status/all/perpage/10/page/')
    _data_good = _data_bad = run(
        102, _data_good, _data_bad, 'https://www.kinopoisk.ru/film/111543/reviews/ord/rating/status/all/perpage/10/page/')
