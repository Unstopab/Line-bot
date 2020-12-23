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

from lulumicrawler import Rent

from linebot.models import *
import utils, call_database, phoetalk, crawler

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

@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
            print(events)
 
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
         
            if isinstance(event, MessageEvent):  # 如果有訊息事件
         
                food = Rent(event.message.text)  #使用者傳入的訊息文字
         
                line_bot_api.reply_message(  # 回應前五間最高人氣且營業中的餐廳訊息文字
                    event.reply_token,
                    TextSendMessage(text=Set.scrape())
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()




# @app.route("/callback", methods=['POST']) #有人用瀏覽器發送訊號到我的網址，我再執行下面的程式
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         print("Invalid signature. Please check your channel access token/channel secret.")
#         abort(400)

#     return 'OK'  #return之上的程式碼就不用動~


# @handler.add(MessageEvent, message=TextMessage) #就我所知我們的動作就是寫在handler之下
# def handle_message(event):
#     # line_bot_api.reply_message(
#     #     event.reply_token,
#     #     TextSendMessage(text=event.message.text)) #event.message.text是使用者傳來的訊息，前面這行程式碼是回傳使用者傳來的訊息
    
#     if "我要看房" in event.message.text:

#         buttons_template_message = TemplateSendMessage(
#     alt_text='Buttons template',
#     template=ButtonsTemplate(
#         thumbnail_image_url='https://hp1.591.com.tw/house/active/2020/08/20/159790889960316104_210x158.crop.jpg',
#         title='台北租屋',
#         text='請輸入您想找台北市的哪一區',
#         actions=[
#             PostbackAction(
#                 label='中山區',
#                 text='中山區',
#                 data='action=buy&itemid=1'
#             ),
#             MessageAction(
#                 label='點我看看',
#                 text='點我看看'
#             ),
#             URIAction(
#                 label='自己上591租屋網',
#                 uri='https://rent.591.com.tw/?kind=0&region=1'
#             )
#         ]
#     )
# )
# #
#         line_bot_api.reply_message(
#         event.reply_token,
#         buttons_template_message)    
#         return
    
#     if "爬蟲" in event.message.text:
#         line_bot_api.reply_message(
#         event.reply_token,
#         scrape())    
#         return


#     if '圖片' in event.message.text:
#         image_carousel_template_message = TemplateSendMessage(
#     alt_text='ImageCarousel template',
#     template=ImageCarouselTemplate(
#         columns=[
#             ImageCarouselColumn(
#                 image_url='https://hp1.591.com.tw/house/active/2020/12/06/160724847605069017_210x158.crop.jpg',
#                 action=PostbackAction(
#                     label='我要看房!',
#                     display_text='我要看房!',
#                     data='action=buy&itemid=1'
#                 )
#             ),
#             ImageCarouselColumn(
#                 image_url='https://hp2.591.com.tw/house/active/2020/10/25/160361445000724103_210x158.crop.jpg',
#                 action=PostbackAction(
#                     label='我也要看房!',
#                     display_text='我也要看房!',
#                     data='action=buy&itemid=2'
#                 )
#             )
#         ]
#     )
# )
#         line_bot_api.reply_message(
#         event.reply_token,
#         image_carousel_template_message)    
#         return

#     if '草泥馬訓練紀錄' in event.message.text:  #-----
#         reply = phoetalk.insert_record(event)
#     elif '輸入資料' in event.message.text:        
#         reply = phoetalk.insert_record2(event)
#     elif '找租屋' in event.message.text:        
#         line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text="你要找什麼房子?"))       
#     else:
#         line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text="我難過"))
        
if __name__ == "__main__":
    app.run()