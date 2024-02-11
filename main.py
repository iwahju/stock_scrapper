import requests
from bs4 import BeautifulSoup as bs
import time

start_time = time.time()

pages = []


for page_number in range(1,5):

    url_start = 'https://www.centralcharts.com/en/price-list-ranking/'
    url_end = 'ALL/asc/ts_29-us-nyse-stocks--qc_1-alphabetical-order'
    url = url_start +url_end +str(page_number)