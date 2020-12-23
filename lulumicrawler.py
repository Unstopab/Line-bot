#import 套件
import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

#輸入條件
class Set(ABC):

    # def __init__(self, district, build_type, rent, ping):
    #     self.district = district #行政區
    #     self.build_type = build_type #房屋類型
    #     self.rent = rent #租金
    #     self.ping = ping #坪數
    def __init__(self, build_type):
        self.build_type = build_type #房屋類型

        #行政區    
        # if self.district == "中山區":
        #     self.district = "section=3"
        # elif self.district == "大安區":
        #     self.district = "section=5"
        # elif self.district == "信義區":
        #     self.district = "section=7"
        # elif self.district == "內湖區":
        #     self.district = "section=10" 
        # elif self.district == "士林區":
        #     self.district = "section=8"  
        # elif self.district == "中正區":
        #     self.district = "section=1"
        # elif self.district == "松山區":
        #     self.district = "section=4"  
        # elif self.district == "大同區":
        #     self.district = "section=2"
        # elif self.district == "萬華區":
        #     self.district = "section=6"
        # elif self.district == "北投區":
        #     self.district = "section=9" 
        # elif self.district == "文山區":
        #     self.district = "section=12"
        # elif self.district == "南港區":
        #     self.district = "section=11" 
        # elif self.district == "不限":
        #     self.district = ""
        
        #房屋類型
        if self.build_type == "整層住家":
            self.build_type = "kind=1"
        elif self.build_type == "獨立套房":
            self.build_type = "kind=2"
        elif self.build_type == "分租套房":
            self.build_type = "kind=3"
        elif self.build_type == "雅房":
            self.build_type = "kind=4"
        elif self.build_type == "車位":
            self.build_type = "kind=8"
        elif self.build_type == "不限":
            self.build_type = "kind=0"
        elif self.build_type == "其他":
            self.build_type = "kind=24"
    
        #租金
        # if self.rent == "5000以下":
        #     self.rent = "rentprice=1"
        # elif self.rent == "5000-10000":
        #     self.rent = "rentprice=2"
        # elif self.rent == "10000-20000": 
        #     self.rent = "rentprice=3"
        # elif self.rent == "20000-30000":
        #     self.rent = "rentprice=4"
        # elif self.rent == "30000-40000":
        #     self.rent = "rentprice=5"
        # elif self.rent == "40000-60000":
        #     self.rent = "rentprice=6"
        # elif self.rent == "60000以上":
        #     self.rent = "rentprice=7"   
        # elif self.rent == "不限":
        #     self.rent = "rentprice=0"
    
        # #坪數    
        # if self.ping == "10以下":
        #     self.ping = "area=0,10"
        # elif self.ping == "10-20":
        #     self.ping = "area=10,20"
        # elif self.ping == "20-30": 
        #     self.ping = "area=20,30"
        # elif self.ping == "30-40": 
        #     self.ping = "area=30,40"
        # elif self.ping == "40-50": 
        #     self.ping = "area=40,50"
        # elif self.ping =="50以上":
        #     self.ping = "area=50,"
        # elif self.ping =="不限":
        #     self.ping = "area=0,0"

    @abstractmethod
    def scrape(self):
        pass
#爬蟲       
class Rent(Set):
            
    def scrape(self):
        #設定網址
        # url="https://rent.591.com.tw/?" + self.build_type +
        #     "&region=1" + self.district + "&" + self.rent + "&" + self.ping
        # print(url)
        # response = requests.get("https://rent.591.com.tw/?" + self.build_type +"&region=1" + self.district + "&" + self.rent + "&" + self.ping)
        response = requests.get("https://rent.591.com.tw/?" + self.build_type +"&region=1")
        soup = BeautifulSoup(response.content, "html.parser") 
        print()
        #定位
        houses = soup.findAll('li', {'class': 'pull-left infoContent'})
        prices = soup.findAll('div', {'class': "price"})
        #下載查詢結果
        content = ""
        num=0
        for house in houses:
            title = house.find("a").getText() #名稱  
            data = house.find("p", {"class": "lightBox"}).getText()#基本資料
            data = data.replace(' ','').replace('\n','').replace('\xa0','')
            address = house.find("em").getText() #地址
            tag= house.find("a") #連結
            tag = tag.get('href')
            rentprice = prices[num].find("i").getText() #租金
            content += f"名稱：{title} \n連結： https:{tag} \n資訊：{data} \n地點：{address}\n價格：{rentprice}元/月 \n \n"
            num +=1
        return content
