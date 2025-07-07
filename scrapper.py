from bs4 import BeautifulSoup
import requests
import json

url = "http://books.toscrape.com/"
def scrape_books(url):
     response  = requests.get(url)
     if response.status_code != 200 :
          print('Cannot fetch data')
          return
    


     response.encoding = response.apparent_encoding
     
     # beautiful soup class ko object banaune

     soup = BeautifulSoup(response.text,"html.parser")

     articles = soup.find_all('article',class_='product_pod')

     
     bk=[]
     for article in articles:
          title = article.h3.a["title"]
          
          price_text = article.find("p",class_="price_color").text
          
          curency = price_text[0]
         
          price = float(price_text[1:])
          bk.append(
               {'title':title,
                'currency':curency,
                'price':price
               })
          return bk
        
     
    

all_books = scrape_books(url)
with open('books.json' , 'w') as f:
    json.dump(all_books,f,indent=2,ensure_ascii=False)
   # store data in csv file hw








# status 200 aye matra garna milxa







