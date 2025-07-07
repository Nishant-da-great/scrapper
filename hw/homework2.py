import requests
from bs4 import BeautifulSoup
import json


url = 'https://books.toscrape.com'

def for_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')



# purai html file input bhaisakyo aba tesbata value nikalna

    books_det = soup.find_all('atricle',class_='product.pod')
    
