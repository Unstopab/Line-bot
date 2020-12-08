from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import call_database

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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="你好阿")) #event.message.text是使用者傳來的訊息，前面這行程式碼是回傳使用者傳來的訊息

    
    if '紀錄啦' in event.message.text:  #-----
        
        try:
            # record_list = prepare_record(event.message.text) #這一段我還在測試中 是要用來寫入資料庫的><
            reply = line_insert_record(event.message.text)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply)
            )
            
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='失敗了')   #-----
            )


if __name__ == "__main__":
    app.run()