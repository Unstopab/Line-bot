from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)

import json
from linebot.exceptions import (
    InvalidSignatureError
)
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ImageCarouselTemplate,ImageCarouselColumn,PostbackAction
# )

from linebot.models import *
import utils, call_database, phoetalk

app = Flask(__name__)

line_bot_api = LineBotApi('9rvIouCQrgODVyuKEfdDdFbaxPffXrTs9qyYuugiJoqHjITy/lcCPls0Xabr8XFzDtN2wVgNkHLmEr4RjgYLcnQjukZzDENd6U8y4gJYgcdLyNPL0nn2x24SABPLmApQ7keULkePNWQZf2AR3QG4oQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b3dd7bebba7dd30ab06e25add81eb054')  #line_bot_api跟handler，就是接line-bot裡面的參數


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
    if '圖片' in event.message.text:
        image_carousel_template_message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://hp1.591.com.tw/house/active/2020/12/06/160724847605069017_210x158.crop.jpg',
                action=PostbackAction(
                    label='postback1',
                    display_text='我要看房!',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://hp2.591.com.tw/house/active/2020/10/25/160361445000724103_210x158.crop.jpg',
                action=PostbackAction(
                    label='postback2',
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

    if '按鈕' in event.message.text:

        #這邊改成找房子的各個條件

        #請輸入您想找台北市的哪一區？中山區、大安區、信義區、內湖區、士林區、北投區、中正區、松山區、大同區、萬華區、文山區、南港區、不限

        district=TextSendMessage(
            text = "請輸入您想找台北市的哪一區？",
            quick_reply = QuickReply(
                items = [
                    QuickReplyButton(
                        action = MessageAction(label = "中山區", text = "中山區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "大安區", text = "大安區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "信義區", text = "信義區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "內湖區", text = "內湖區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "士林區", text = "士林區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "北投區", text = "北投區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "中正區", text = "中正區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "松山區", text = "松山區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "大同區", text = "大同區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "萬華區", text = "萬華區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "文山區", text = "文山區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "南港區", text = "南港區")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "不限", text = "不限")
                        )
                    ]))




        #輸入您想要的房屋類型(整層住家、獨立套房、分租套房、雅房、車位、不限、其他)

        build_type=TextSendMessage(
            text = "請輸入您想要的房屋類型？",
            quick_reply = QuickReply(
                items = [
                    QuickReplyButton(
                        action = MessageAction(label = "整層住家", text = "整層住家")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "獨立套房", text = "獨立套房")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "分租套房", text = "分租套房")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "雅房", text = "雅房")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "車位", text = "車位")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "其他", text = "其他")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "不限", text = "不限")
                        )
                    ]))


        #輸入您每個月欲付的租金(5000以下、5000-10000、10000-20000、20000-30000、30000-40000、40000-60000、60000以上、不限)

        rent=TextSendMessage(
            text = "請輸入您每個月欲付的租金？",
            quick_reply = QuickReply(
                items = [
                    QuickReplyButton(
                        action = MessageAction(label = "5000以下", text = "5000以下")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "5000-10000", text = "5000-10000")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "10000-20000", text = "10000-20000")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "20000-30000", text = "20000-30000")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "30000-40000", text = "30000-40000")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "40000-60000", text = "40000-60000")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "60000以上", text = "60000以上")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "不限", text = "不限")
                        )
                    ]))

        #輸入您想要的坪數(10以下、10-20、20-30、30-40、40-50、50以上、不限)

        ping=TextSendMessage(
            text = "請輸入您想要的坪數？",
            quick_reply = QuickReply(
                items = [
                    QuickReplyButton(
                        action = MessageAction(label = "10以下", text = "10以下")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "10-20", text = "10-20")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "20-30", text = "20-30")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "30-40", text = "30-40")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "40-50", text = "40-50")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "50以上", text = "50以上")
                        ),
                    QuickReplyButton(
                        action = MessageAction(label = "不限", text = "不限")
                        )
                    ]))


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