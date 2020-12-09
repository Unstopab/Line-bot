from __future__ import unicode_literals
import os

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, PostbackEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage

import configparser

import random

# 我們的函數
import utils, call_database

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))


def insert_record(event):
    
    if '草泥馬訓練紀錄' in event.message.text:
        
        try:
            record_list = utils.prepare_record(event.message.text)
            reply = CallDatabase.line_insert_record(record_list)

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
