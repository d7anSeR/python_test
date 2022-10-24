import os
from time import sleep

import requests
from bs4 import BeautifulSoup
import codecs
#from selenium import webdriver
#import random


# def get_session(proxies):
#     # создаем сессию для отправки HTTP запроса
#     session = requests.Session()
#     # выбираем случайным образом один из адресов
#     proxy = random.choice(proxies)
#     session.proxies = {"http": proxy, "https": proxy}
#     return session


def make_dir():
    name_dir_good = os.path.join('dataset','good')
    name_dir_bad = os.path.join('dataset','bad')
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    if not os.path.isdir(name_dir_good):
        name = os.path.join('dataset', 'good')
        os.mkdir(name)
    if not os.path.isdir(name_dir_bad):
        name = os.path.join('dataset', 'bad')
        os.mkdir(name)


def review_good(data_good, pages, link_page):
    for page in range(1, pages+1):
        flag = True
        print(page)
        while (flag):
            url = link_page + f'{pages}/'
            sleep(30 + 2*page)
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'lxml')
            try:
                title_film = soup.find('a', class_='breadcrumbs__link').text
                flag = False
            except:
                sleep(900)
        reviewsAll = soup.findAll('div', class_='response good')
        for review in reviewsAll:
            feedback = review.find('span', class_='_reachbanner_').text
            if data_good < 1000:
                number = str(data_good + 1).zfill(4)
                data_good += 1
                print(data_good)
            try:
                name_file = os.path.join('dataset', 'good', '{number}.txt')
                file = codecs.open(name_file, 'w', 'utf-8')
                file.write(title_film + '\n' + feedback)
                file.close()
            except:
                print("Error open file")
    return data_good


def review_bad(data_bad, pages, link_page):
    for page in range(1, pages+1):
        flag = True
        print(page)
        while (flag):
            url = link_page + f'{pages}/'
            sleep(30+2*page)
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'lxml')
            try:
                title_film = soup.find('a', class_='breadcrumbs__link').text
                flag = False
            except:
                sleep(900)
        reviewsAll = soup.findAll('div', class_='response bad')
        for review in reviewsAll:
            feedback = review.find('span', class_='_reachbanner_').text
            if data_bad < 1000:
                number = str(data_bad+1).zfill(4)
                data_bad += 1
                print(data_bad)
            try:
                name_file = os.path.join('dataset', 'bad', '{number}.txt')
                file = codecs.open(name_file, 'w', 'utf-8')
                file.write(title_film + '\n' + feedback)
                file.close()
            except:
                print("Error open file")
    return data_bad


def run():
    _data_good, _data_bad = 0, 0
    make_dir()
    _data_good = review_good(
        _data_good, 50, 'https://www.kinopoisk.ru/film/326/reviews/ord/date/status/good/perpage/10/page/')
    _data_good = review_good(
        _data_good, 42, 'https://www.kinopoisk.ru/film/448/reviews/ord/date/status/good/perpage/10/page/')
    _data_good = review_good(
        _data_good, 12, 'https://www.kinopoisk.ru/film/11130/reviews/ord/date/status/good/perpage/10/page/')
    _data_bad = review_bad(
        _data_bad, 43, 'https://www.kinopoisk.ru/film/401177/reviews/ord/date/status/bad/perpage/10/page/')
    _data_bad = review_bad(
        _data_bad, 8, 'https://www.kinopoisk.ru/film/395060/reviews/ord/date/status/bad/perpage/10/page/')
    _data_bad = review_bad(
        _data_bad, 42, 'https://www.kinopoisk.ru/film/251733/reviews/ord/rating/status/bad/perpage/10/page/')
    _data_bad = review_bad(
        _data_bad, 13, 'https://www.kinopoisk.ru/film/470179/reviews/ord/date/status/bad/perpage/10/page/')
    _data_bad = review_bad(
        _data_bad, 7, 'https://www.kinopoisk.ru/film/464963/reviews/ord/date/status/bad/perpage/10/page/')
    _data_bad = review_bad(
        _data_bad, 7, 'https://www.kinopoisk.ru/film/464963/reviews/ord/date/status/bad/perpage/10/page/')
    _data_bad = review_bad(
        _data_bad, 37, 'https://www.kinopoisk.ru/film/714888/reviews/ord/date/status/bad/perpage/10/page/')
    _data_bad = review_bad(
        _data_bad, 10, 'https://www.kinopoisk.ru/film/718222/reviews/ord/date/status/bad/perpage/10/page/')


if __name__ == '__main__':
    run()
