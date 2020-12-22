#import 套件
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\USER\\OneDrive\\桌面\\coding\\Line-bot\\chromedriver.exe")
from selenium.webdriver.chrome.options import Options

#輸入條件
#行政區

while True:
    district = input("請輸入您想找台北市的哪一區(中山區、大安區、信義區、內湖區、士林區、中正區、松山區、大同區、萬華區、文山區、南港區、不限)：")
    if district == "中山區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[1]")
        break
    elif district == "大安區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[2]")
        break
    elif district == "信義區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[3]")
        break
    elif district == "內湖區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[4]")
        break   
    elif district == "士林區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[5]")  
        break 
    elif district == "中正區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[6]")
        break 
    elif district == "松山區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[7]")  
        break 
    elif district == "大同區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[8]")
        break 
    elif district == "萬華區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[9]")
        break 
    elif district == "北投區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[10]") 
        break 
    elif district == "文山區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[11]") 
        break 
    elif district == "南港區":
        district_xpath = ("/html/body/div[2]/section[3]/section/ul[1]/li[12]") 
        break
    elif district == "不限":
        district_xpath = ("/html/body/div[2]/section[3]/section/div[1]/span[2]")
        break
    else:
        continue
        
#房屋類型
while True:
    build_type = input("輸入您想要的房屋類型(整層住家、獨立套房、分租套房、雅房、車位、不限、其他)：")
    if build_type == "整層住家":
        build_type_xpath = ("/html/body/div[2]/section[3]/section/div[2]/span[2]")
        break
    elif build_type == "獨立套房":
        build_type_xpath = ("/html/body/div[2]/section[3]/section/div[2]/span[3]")
        break
    elif build_type == "分租套房":
        build_type_xpath = ("/html/body/div[2]/section[3]/section/div[2]/span[4]")
        break
    elif build_type == "雅房":
        build_type_xpath = ("/html/body/div[2]/section[3]/section/div[2]/span[5]")
        break
    elif build_type == "車位":
        build_type_xpath = ("/html/body/div[2]/section[3]/section/div[2]/span[6]")
        break
    elif build_type == "不限":
        build_type_xpath = ("/html/body/div[2]/section[3]/section/div[2]/span[1]")
        break
    elif build_type == "其他":
        build_type_xpath = ("/html/body/div[2]/section[3]/section/div[2]/span[7]")
        break
    else:
        continue
    
#租金
while True:
    rent = input("輸入您每個月欲付的租金(5000以下、5000-10000、10000-20000、20000-30000、30000-40000、40000-60000、60000以上、不限)：")
    if rent == "5000以下":
        rent_xpath = ("/html/body/div[2]/section[3]/section/div[3]/span[2]")
        break
    elif rent == "5000-10000":
        rent_xpath = ("/html/body/div[2]/section[3]/section/div[3]/span[3]")
        break
    elif rent == "10000-20000": 
        rent_xpath = ("/html/body/div[2]/section[3]/section/div[3]/span[4]")
        break
    elif rent == "20000-30000":
        rent_xpath = ("/html/body/div[2]/section[3]/section/div[3]/span[5]")
        break
    elif rent == "30000-40000":
        rent_xpath = ("/html/body/div[2]/section[3]/section/div[3]/span[6]")
        break
    elif rent == "40000-60000":
        rent_xpath = ("/html/body/div[2]/section[3]/section/div[3]/span[7]")
        break
    elif rent == "60000以上":
        rent_xpath = ("/html/body/div[2]/section[3]/section/div[3]/span[8]")
        break    
    elif rent == "不限":
        rent_xpath = ("/html/body/div[2]/section[3]/section/div[3]/span[1]")
        break
    else:
        continue
    
#坪數    
while True:
    ping = input("輸入您想要的坪數(10以下、10-20、20-30、30-40、40-50、50以上、不限)：")
    if ping == "10以下":
        ping_xpath = ("/html/body/div[2]/section[3]/section/div[5]/span[2]")
        break
    elif ping == "10-20":
        ping_xpath = ("/html/body/div[2]/section[3]/section/div[5]/span[3]")
        break
    elif ping == "20-30": 
        ping_xpath = ("/html/body/div[2]/section[3]/section/div[5]/span[4]")
        break
    elif ping == "30-40": 
        ping_xpath = ("/html/body/div[2]/section[3]/section/div[5]/span[5]")
        break
    elif ping == "40-50": 
        ping_xpath = ("/html/body/div[2]/section[3]/section/div[5]/span[6]")
        break
    elif ping =="50以上":
        ping_xpath = ("/html/body/div[2]/section[3]/section/div[5]/span[7]")
        break
    elif ping =="不限":
        ping_xpath = ("/html/body/div[2]/section[3]/section/div[5]/span[1]")
        break
    else:
        continue

#定義函式_列印搜尋結果
def download_data(answer):
#取得網頁原始碼
    html_text=driver.page_source
    soup=BeautifulSoup(html_text,"html.parser")   
#存取結果標題
    try:
        name_lst=[]
        for name in soup.find_all("h3"):
            name=name.text.replace("黄金曝光"," ").replace("VIP","").replace(" ","").replace("\n","")
            name_lst.append(name)
        #存取物件連結
        link_lst=[]
        for link_name in name_lst:
            link=driver.find_elements_by_link_text(link_name)
            link_url=link[0].get_attribute("href")
            link_lst.append(link_url)
        #存取圖片連結
        images = str(soup.find_all("li", {"class": "pull-left imageBox"})).split("</div>")
        i = 0
        image_list = []
        for num in range(len(images)-1):
            i += 1
            if i == 1:
                temp = images[num].split(" ")
                image_list.append(temp[9].split("data-original=")[1].strip('"'))
            else:
                temp = images[num].split(" ")
                image_list.append(temp[10].split("data-original=")[1].strip('"'))
        #存取結果基本資料
        basic_data_lst=[]
        basic_data=driver.find_elements_by_class_name("lightBox")
        for num in range(len(basic_data)):
            basic_data_lst.append(basic_data[num].text)       
        #存取結果價格
        price_lst=[]
        price=driver.find_elements_by_class_name("price")
        for num in range(len(price)):
            price_lst.append(price[num].text)       
        #印出結果
        for num in range (len(name_lst)):
            print(name_lst[num])
            print(link_lst[num])
            print(price_lst[num])
            print(basic_data_lst[num])
            print(image_list[num])
            print("\n")
    except:
        print("沒有符合條件的房子哦")


while True:
    try:
        start=input("是否開始搜尋(是/否)？")
    except:
        print("程式有誤，請聯絡開發人員")
    else:
        if start=="是":
            #取消所有的彈出視窗
            options = Options()
            options.add_argument("--disable-notifications")  
            # options.add_argument("--headless") #不開啟實體瀏覽器
            driver=webdriver.Chrome(options=options)
            #打開網頁
            url="https://rent.591.com.tw/"
            driver.get(url)
            #關閉廣告
            close_first = driver.find_element_by_class_name("area-box-close")
            close_first.click()
            #輸入條件
            #輸入台北市
            search_location = driver.find_element_by_xpath("/html/body/div[2]/section[3]/section/div[1]/span[1]")
            search_location.click()
            taipei_bottom = driver.find_element_by_xpath("/html/body/div[2]/section[3]/section/ul[1]/dl[1]/ul/li[1]/a")
            taipei_bottom.click()
            time.sleep(2)
            #輸入行政區
            distric_bottom = driver.find_element_by_xpath(district_xpath)
            distric_bottom.click()
            time.sleep(1)
            #輸入房屋類型
            build_type_bottom =  driver.find_element_by_xpath(build_type_xpath)
            build_type_bottom.click()
            time.sleep(1)
            #輸入租金
            rent_bottom =  driver.find_element_by_xpath(rent_xpath)
            rent_bottom.click()
            time.sleep(1)
            #輸入坪數
            ping_bottom =  driver.find_element_by_xpath(ping_xpath)
            ping_bottom.click()
            time.sleep(5)
            #印出結果
            print(download_data(start))
            while True:
                answer=input("是否進行下一頁(是/否)？")
                if answer=="是":
                    try:
                        next_page=driver.find_element_by_class_name("pageNext")
                        next_page.click()
                        time.sleep(3)
                        print(download_data(answer))
                    except:
                        print("沒有符合條件的房子囉")
                        print("感謝使用")
                        break
                elif answer=="否":
                    print("不再點選下一頁")
                    break
                else:
                    continue
        elif start=="否":
            print("感謝使用")
            break
        else:
            continue
