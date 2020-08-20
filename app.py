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

app = Flask(__name__)

line_bot_api = LineBotApi('q0O8k8sblfmpz42xRnGNC1B5gAjVUcWLLBr4HQfTvsNws++RQ1gvdIDbvjla/SFhHPXUAeeNVt0rC+RRoE7KKm2DDcrx7ZK45FdkEgekUvMeM+QNp83B//jFTZGO4EScK27bgYgNyB1/irf2h+eh+AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5c2adda5ca21f4451e92a65dfc24a287')


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

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()