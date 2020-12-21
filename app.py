from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ImageCarouselTemplate
)

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
                image_url='https://example.com/item1.jpg',
                action=PostbackAction(
                    label='postback1',
                    display_text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item2.jpg',
                action=PostbackAction(
                    label='postback2',
                    display_text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
)
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