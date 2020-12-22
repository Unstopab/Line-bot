import requests
from bs4 import BeautifulSoup


def scrape()
	re = requests.get("https://www.ccclub.io/course/2020Spring") #放要爬的網址

	print(re.status_code) #確定有無成功爬取網頁
# print(re.text) #列出網頁的html原始碼

	soup = BeautifulSoup(re.text, "html.parser") #解析網頁，第一個要放網頁原始碼

# print(soup.link) 
# print(soup.link.string)
# print(soup.title.text)
#soup.可以用來取tag裡的東西或文字；soup.find("")用來取tag裡的東西；
#soup.findALL("")用來取多個tag；soup.find_all("")用來取多個tag，這兩個會回傳一個list!!
#soup.findAll('div', {'class': 'movielist_info'}) 查找特定屬性的資料

	body = soup.tbody
	for tr in body.find_all("tr"):
    	td = tr.find_all("td")
        content = td[2].text
        print(content)
    return content
