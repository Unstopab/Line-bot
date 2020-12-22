from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)

import json
# from linebot.exceptions import (
#     InvalidSignatureError 
# ) #只是為了測試button才先註解
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ImageCarouselTemplate,ImageCarouselColumn,PostbackAction
# )

from linebot.models import *
import utils, call_database, phoetalk

#-----------------button 測試區1
# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings

# from linebot.exceptions import InvalidSignatureError, LineBotApiError
# from scraper import Set 

#-----------------button 測試區1

app = Flask(__name__)

line_bot_api = LineBotApi('9rvIouCQrgODVyuKEfdDdFbaxPffXrTs9qyYuugiJoqHjITy/lcCPls0Xabr8XFzDtN2wVgNkHLmEr4RjgYLcnQjukZzDENd6U8y4gJYgcdLyNPL0nn2x24SABPLmApQ7keULkePNWQZf2AR3QG4oQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b3dd7bebba7dd30ab06e25add81eb054')  #line_bot_api跟handler，就是接line-bot裡面的參數

# #----------------------------------button 測試區2
# parser = WebhookParser('b3dd7bebba7dd30ab06e25add81eb054')

# @csrf_exempt
# def callback(request):

#     if request.method == 'POST':
#         signature = request.META['HTTP_X_LINE_SIGNATURE']
#         body = request.body.decode('utf-8')

#         try:
#             events = parser.parse(body, signature)  # 傳入的事件
#         except InvalidSignatureError:
#             return HttpResponseForbidden()
#         except LineBotApiError:
#             return HttpResponseBadRequest()

#         for event in events:
#             if isinstance(event, MessageEvent):  # 如果有訊息事件

#                 if event.message.text == "我要看房":

#                     line_bot_api.reply_message(  # 回復傳入的訊息文字：「行政區」
#                         event.reply_token,
#                         TemplateSendMessage(
#                             alt_text='Buttons template',
#                             template=ButtonsTemplate(
#                                 title='台北租屋',
#                                 text='請輸入您想找台北市的哪一區？',  
#                                 actions=[
#                                     PostbackTemplateAction(
#                                         label='中山區',
#                                         text='中山區',
#                                         data='A&中山區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='大安區',
#                                         text='大安區',
#                                         data='A&大安區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='信義區',
#                                         text='信義區',
#                                         data='A&信義區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='內湖區',
#                                         text='內湖區',
#                                         data='A&內湖區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='士林區',
#                                         text='士林區',
#                                         data='A&士林區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='北投區',
#                                         text='北投區',
#                                         data='A&北投區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='中正區',
#                                         text='中正區',
#                                         data='A&中正區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='松山區',
#                                         text='松山區',
#                                         data='A&松山區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='大同區',
#                                         text='大同區',
#                                         data='A&大同區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='萬華區',
#                                         text='萬華區',
#                                         data='A&萬華區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='文山區',
#                                         text='文山區',
#                                         data='A&文山區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='南港區',
#                                         text='南港區',
#                                         data='A&南港區'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='不限',
#                                         text='不限',
#                                         data='A&不限'
#                                     )
#                                 ]
#                             )
#                         )
#                     )


#             elif isinstance(event, PostbackEvent):  # 如果有回傳值事件

#                 if event.postback.data[0:1] == "A":  # 如果回傳值為「行政區」

#                     district = event.postback.data[2:]  # 透過切割字串取得地區文字

#                     line_bot_api.reply_message(   # 回復「房屋類型」按鈕樣板訊息
#                         event.reply_token,
#                         TemplateSendMessage(
#                             alt_text='Buttons template',
#                             template=ButtonsTemplate(
#                                 title='我要看房！',
#                                 text='請選擇美食類別',
#                                 actions=[
#                                     PostbackTemplateAction(  # 將第一步驟選擇的地區，包含在第二步驟的資料中
#                                         label='整層住家',
#                                         text='整層住家',
#                                         data='B&' + district + '&整層住家'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='獨立套房',
#                                         text='獨立套房',
#                                         data='B&' + district + '&獨立套房'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='分租套房',
#                                         text='分租套房',
#                                         data='B&' + district + '&分租套房'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='雅房',
#                                         text='雅房',
#                                         data='B&' + district + '&雅房'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='車位',
#                                         text='車位',
#                                         data='B&' + district + '&車位'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='不限',
#                                         text='不限',
#                                         data='B&' + district + '&不限'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='其他',
#                                         text='其他',
#                                         data='B&' + district + '&其他'
#                                     )
#                                 ]
#                             )
#                         )
#                     )

#             elif isinstance(event, PostbackEvent):  # 如果有回傳值事件

#                 if event.postback.data[0:1] == "B":  # 如果回傳值為「房屋類型」

#                     build_type = event.postback.data[2:].split('&')  # 透過切割字串取得房屋類型文字

#                     line_bot_api.reply_message(   # 回復「租金」按鈕樣板訊息
#                         event.reply_token,
#                         TemplateSendMessage(
#                             alt_text='Buttons template',
#                             template=ButtonsTemplate(
#                                 title='我要看房！',
#                                 text='請輸入您每個月欲付的租金？',
#                                 actions=[
#                                     PostbackTemplateAction(  # 將第一步驟、第二步驟選擇的地區，包含在第三步驟的資料中
#                                         label='5000以下',
#                                         text='5000以下',
#                                         data='C&' + district + build_type + '&5000以下'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='5000-10000',
#                                         text='5000-10000',
#                                         data='C&' + district + build_type + '&5000-10000'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='10000-20000',
#                                         text='10000-20000',
#                                         data='C&' + district + build_type + '&10000-20000'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='20000-30000',
#                                         text='20000-30000',
#                                         data='C&' + district + build_type + '&20000-30000'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='30000-40000',
#                                         text='30000-40000',
#                                         data='C&' + district + build_type + '&30000-40000'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='40000-60000',
#                                         text='40000-60000',
#                                         data='C&' + district + build_type + '&40000-60000'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='60000以上',
#                                         text='60000以上',
#                                         data='C&' + district + build_type + '&60000以上'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='不限',
#                                         text='不限',
#                                         data='C&' + district + build_type + '&不限'
#                                     )
#                                 ]
#                             )
#                         )
#                     )

#             elif isinstance(event, PostbackEvent):  # 如果有回傳值事件

#                 if event.postback.data[0:1] == "C":  # 如果回傳值為「租金」

#                     rent = event.postback.data[2:].split('&')  # 透過切割字串取得租金文字

#                     line_bot_api.reply_message(   # 回復「坪數」按鈕樣板訊息
#                         event.reply_token,
#                         TemplateSendMessage(
#                             alt_text='Buttons template',
#                             template=ButtonsTemplate(
#                                 title='我要看房！',
#                                 text='請輸入您想要的坪數？',
#                                 actions=[
#                                     PostbackTemplateAction(  # 將第一步驟、第二步驟、第三步驟選擇的地區，包含在第四步驟的資料中
#                                         label='10以下',
#                                         text='10以下',
#                                         data='D&' + district + build_type + rent + '&10以下'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='10-20',
#                                         text='10-20',
#                                         data='D&' + district + build_type + rent + '&10-20'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='20-30',
#                                         text='20-30',
#                                         data='D&' + district + build_type + rent + '&20-30'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='30-40',
#                                         text='30-40',
#                                         data='D&' + district + build_type + rent + '&30-40'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='40-50',
#                                         text='40-50',
#                                         data='D&' + district + build_type + rent + '&40-50'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='50以上',
#                                         text='50以上',
#                                         data='D&' + district + build_type + rent + '&50以上'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label='不限',
#                                         text='不限',
#                                         data='D&' + district  + build_type + rent +  '&不限'
#                                     )
#                                 ]
#                             )
#                         )
#                     )

#                 elif event.postback.data[0:1] == "D":  # 如果回傳值為「坪數」

#                     result = event.postback.data[2:].split('&')  # 回傳值的字串切割

#                     house = Set(
#                         result[0],  # 行政區
#                         result[1],  # 房屋類型
#                         result[2],  # 租金
#                         result[3]  # 坪數
#                     )

#                     line_bot_api.reply_message(  # 回復訊息文字
#                         event.reply_token,
#                         # 爬取591網站
#                         TextSendMessage(text=house.scrape())
#                     )

#         return HttpResponse()
#     else:
#         return HttpResponseBadRequest()


@app.route("/callback", methods=['POST']) #有人用瀏覽器發送訊號到我的網址，我再執行下面的程式
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'  #return之上的程式碼就不用動~


@handler.add(MessageEvent, message=TextMessage) #就我所知我們的動作就是寫在handler之下
def handle_message(event):
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text)) #event.message.text是使用者傳來的訊息，前面這行程式碼是回傳使用者傳來的訊息
    
    if "我要看房" in event.message.text:

        buttons_template_message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://hp1.591.com.tw/house/active/2020/08/20/159790889960316104_210x158.crop.jpg',
        title='台北租屋',
        text='請輸入您想找台北市的哪一區',
        actions=[
            PostbackAction(
                label='中山區',
                text='中山區',
                data='action=buy&itemid=1'
            ),
            MessageAction(
                label='點我看看',
                text='點我看看'
            ),
            URIAction(
                label='自己上591租屋網',
                uri='https://rent.591.com.tw/?kind=0&region=1'
            )
        ]
    )
)
        line_bot_api.reply_message(
        event.reply_token,
        buttons_template_message)    
        return
    

    if '圖片' in event.message.text:
        image_carousel_template_message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://hp1.591.com.tw/house/active/2020/12/06/160724847605069017_210x158.crop.jpg',
                action=PostbackAction(
                    label='我要看房!',
                    display_text='我要看房!',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://hp2.591.com.tw/house/active/2020/10/25/160361445000724103_210x158.crop.jpg',
                action=PostbackAction(
                    label='我也要看房!',
                    display_text='我也要看房!',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
)
        line_bot_api.reply_message(
        event.reply_token,
        image_carousel_template_message)    
        return

    if '草泥馬訓練紀錄' in event.message.text:  #-----
        reply = phoetalk.insert_record(event)
    elif '輸入資料' in event.message.text:        
        reply = phoetalk.insert_record2(event)
    elif '找租屋' in event.message.text:        
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="你要找什麼房子?"))       
    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="我難過"))
        
if __name__ == "__main__":
    app.run()