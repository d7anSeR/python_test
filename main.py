import os

import requests
from bs4 import BeautifulSoup, Beautyfulsoup
#import re
#from re import sub
#from decimal import Decimal
#import io
#from datetime import datetime
#import pandas as pd

URL = "https://www.kinopoisk.ru/film/435/reviews/"
html_text= requests.get(URL).text
soup = BeautifulSoup(html_text, 'lxml')
soup.fond('div', class_ = 'reviewItem userReview')
#html_page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
# html_page.text - хранит html код веб-страницы