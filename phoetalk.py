from __future__ import unicode_literals
import os

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, PostbackEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage

import random

# 我們的函數
import utils, call_database

line_bot_api = LineBotApi('9rvIouCQrgODVyuKEfdDdFbaxPffXrTs9qyYuugiJoqHjITy/lcCPls0Xabr8XFzDtN2wVgNkHLmEr4RjgYLcnQjukZzDENd6U8y4gJYgcdLyNPL0nn2x24SABPLmApQ7keULkePNWQZf2AR3QG4oQdB04t89/1O/w1cDnyilFU=')


def insert_record(event):
    
    if '草泥馬訓練紀錄' in event.message.text:
        
        try:
            record_list = utils.prepare_record(event.message.text)
            reply = call_database.line_insert_record(record_list)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply)
            )

        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='失敗了')
            )

        return True
    else:
        return False


def insert_record2(event):
    
    if '輸入資料' in event.message.text:
        
        try:
            record_list2 = utils.prepare_record2(event.message.text)
            reply = call_database.line_insert_record2(record_list2)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply)
                )

        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='失敗了')
            )

        return True
    else:
        return False
