import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

test = " "

def go(test):
#import 套件

    url = 'https://rent.591.com.tw/?kind=24&region=1&section=5,7,6,12,11&rentprice=7&area=50,' 
    re = requests.get(url) 
    soup = BeautifulSoup(re.text, 'html.parser')

    houses = soup.findAll('li', {'class': 'pull-left infoContent'})
    prices = soup.findAll('div', {'class': "price"})
    content = ""
    num=0
    for house in houses:
        title = house.find("a").getText()   
        data = house.find("p", {"class": "lightBox"}).getText()
        data = data.replace(' ','').replace('\n','').replace('\xa0','')
        address = house.find("em").getText() 
        tag= house.find("a")
        tag = tag.get('href')
        rentprice = prices[num].find("i").getText()
        content += f"名稱：{title} \n連結： https:{tag} \n資訊：{data} \n地點：{address}\n價格：{rentprice}元/月 \n \n"
        num +=1
    print(soup)

go(test)