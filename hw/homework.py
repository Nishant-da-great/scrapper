


import  requests
import csv
from bs4 import BeautifulSoup
import json

url = "https://books.toscrape.com/"

def scrap(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    books = soup.find_all('article',class_='product_pod')
    with open('books.csv','w',encoding="utf-8",newline="") as f:

    
        written = csv.writer(f)
        written.writerow(['Title','Price'])
        for i in books:
            title = i.h3.a['title']
            price = i.find('p',class_='price_color').text
            

            written.writerow([title,price])
        print('scraping complete')

 

        
scrap('https://books.toscrape.com/')


