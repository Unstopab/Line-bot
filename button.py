
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    PostbackEvent,
    PostbackTemplateAction
)

from .scraper import IFoodie 

line_bot_api = LineBotApi('9rvIouCQrgODVyuKEfdDdFbaxPffXrTs9qyYuugiJoqHjITy/lcCPls0Xabr8XFzDtN2wVgNkHLmEr4RjgYLcnQjukZzDENd6U8y4gJYgcdLyNPL0nn2x24SABPLmApQ7keULkePNWQZf2AR3QG4oQdB04t89/1O/w1cDnyilFU=')  ＃機器人資料
parser = WebhookParser('b3dd7bebba7dd30ab06e25add81eb054')


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件

                if event.message.text == "我要看房！":

                    line_bot_api.reply_message(  # 回復傳入的訊息文字：「行政區」
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='台北租屋',
                                text='請輸入您想找台北市的哪一區？',  
                                actions=[
                                    PostbackTemplateAction(
                                        label='中山區',
                                        text='中山區',
                                        data='A&中山區'
                                    ),
                                    PostbackTemplateAction(
                                        label='大安區',
                                        text='大安區',
                                        data='A&大安區'
                                    ),
                                    PostbackTemplateAction(
                                        label='信義區',
                                        text='信義區',
                                        data='A&信義區'
                                    ),
                                    PostbackTemplateAction(
                                        label='內湖區',
                                        text='內湖區',
                                        data='A&內湖區'
                                    ),
                                    PostbackTemplateAction(
                                        label='士林區',
                                        text='士林區',
                                        data='A&士林區'
                                    ),
                                    PostbackTemplateAction(
                                        label='北投區',
                                        text='北投區',
                                        data='A&北投區'
                                    ),
                                    PostbackTemplateAction(
                                        label='中正區',
                                        text='中正區',
                                        data='A&中正區'
                                    ),
                                    PostbackTemplateAction(
                                        label='松山區',
                                        text='松山區',
                                        data='A&松山區'
                                    ),
                                    PostbackTemplateAction(
                                        label='大同區',
                                        text='大同區',
                                        data='A&大同區'
                                    ),
                                    PostbackTemplateAction(
                                        label='萬華區',
                                        text='萬華區',
                                        data='A&萬華區'
                                    ),
                                    PostbackTemplateAction(
                                        label='文山區',
                                        text='文山區',
                                        data='A&文山區'
                                    ),
                                    PostbackTemplateAction(
                                        label='南港區',
                                        text='南港區',
                                        data='A&南港區'
                                    ),
                                    PostbackTemplateAction(
                                        label='不限',
                                        text='不限',
                                        data='A&不限'
                                    )
                                ]
                            )
                        )
                    )


            elif isinstance(event, PostbackEvent):  # 如果有回傳值事件

                if event.postback.data[0:1] == "A":  # 如果回傳值為「行政區」

                    district = event.postback.data[2:]  # 透過切割字串取得地區文字

                    line_bot_api.reply_message(   # 回復「房屋類型」按鈕樣板訊息
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='我要看房！',
                                text='請選擇美食類別',
                                actions=[
                                    PostbackTemplateAction(  # 將第一步驟選擇的地區，包含在第二步驟的資料中
                                        label='整層住家',
                                        text='整層住家',
                                        data='B&' + district + '&整層住家'
                                    ),
                                    PostbackTemplateAction(
                                        label='獨立套房',
                                        text='獨立套房',
                                        data='B&' + district + '&獨立套房'
                                    ),
                                    PostbackTemplateAction(
                                        label='分租套房',
                                        text='分租套房',
                                        data='B&' + district + '&分租套房'
                                    ),
                                    PostbackTemplateAction(
                                        label='雅房',
                                        text='雅房',
                                        data='B&' + district + '&雅房'
                                    ),
                                    PostbackTemplateAction(
                                        label='車位',
                                        text='車位',
                                        data='B&' + district + '&車位'
                                    ),
                                    PostbackTemplateAction(
                                        label='不限',
                                        text='不限',
                                        data='B&' + district + '&不限'
                                    ),
                                    PostbackTemplateAction(
                                        label='其他',
                                        text='其他',
                                        data='B&' + district + '&其他'
                                    )
                                ]
                            )
                        )
                    )

            elif isinstance(event, PostbackEvent):  # 如果有回傳值事件

                if event.postback.data[0:1] == "B":  # 如果回傳值為「房屋類型」

                    build_type = event.postback.data[2:].split('&')  # 透過切割字串取得房屋類型文字

                    line_bot_api.reply_message(   # 回復「租金」按鈕樣板訊息
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='我要看房！',
                                text='請輸入您每個月欲付的租金？',
                                actions=[
                                    PostbackTemplateAction(  # 將第一步驟、第二步驟選擇的地區，包含在第三步驟的資料中
                                        label='5000以下',
                                        text='5000以下',
                                        data='C&' + area + build_type + '&5000以下'
                                    ),
                                    PostbackTemplateAction(
                                        label='5000-10000',
                                        text='5000-10000',
                                        data='C&' + area + build_type + '&5000-10000'
                                    ),
                                    PostbackTemplateAction(
                                        label='10000-20000',
                                        text='10000-20000',
                                        data='C&' + area + build_type + '&10000-20000'
                                    ),
                                    PostbackTemplateAction(
                                        label='20000-30000',
                                        text='20000-30000',
                                        data='C&' + area + build_type + '&20000-30000'
                                    ),
                                    PostbackTemplateAction(
                                        label='30000-40000',
                                        text='30000-40000',
                                        data='C&' + area + build_type + '&30000-40000'
                                    ),
                                    PostbackTemplateAction(
                                        label='40000-60000',
                                        text='40000-60000',
                                        data='C&' + area + build_type + '&40000-60000'
                                    ),
                                    PostbackTemplateAction(
                                        label='60000以上',
                                        text='60000以上',
                                        data='C&' + area + build_type + '&60000以上'
                                    ),
                                    PostbackTemplateAction(
                                        label='不限',
                                        text='不限',
                                        data='C&' + area + build_type + '&不限'
                                    )
                                ]
                            )
                        )
                    )

            elif isinstance(event, PostbackEvent):  # 如果有回傳值事件

                if event.postback.data[0:1] == "C":  # 如果回傳值為「租金」

                    rent = event.postback.data[2:].split('&')  # 透過切割字串取得租金文字

                    line_bot_api.reply_message(   # 回復「坪數」按鈕樣板訊息
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='我要看房！',
                                text='請輸入您想要的坪數？',
                                actions=[
                                    PostbackTemplateAction(  # 將第一步驟、第二步驟、第三步驟選擇的地區，包含在第四步驟的資料中
                                        label='10以下',
                                        text='10以下',
                                        data='D&' + area + build_type + rent + '&10以下'
                                    ),
                                    PostbackTemplateAction(
                                        label='10-20',
                                        text='10-20',
                                        data='D&' + area + build_type + rent + '&10-20'
                                    ),
                                    PostbackTemplateAction(
                                        label='20-30',
                                        text='20-30',
                                        data='D&' + area + build_type + rent + '&20-30'
                                    ),
                                    PostbackTemplateAction(
                                        label='30-40',
                                        text='30-40',
                                        data='D&' + area + build_type + rent + '&30-40'
                                    ),
                                    PostbackTemplateAction(
                                        label='40-50',
                                        text='40-50',
                                        data='D&' + area + build_type + rent + '&40-50'
                                    ),
                                    PostbackTemplateAction(
                                        label='50以上',
                                        text='50以上',
                                        data='D&' + area + build_type + rent + '&50以上'
                                    ),
                                    PostbackTemplateAction(
                                        label='不限',
                                        text='不限',
                                        data='D&' + area  + build_type + rent +  '&不限'
                                    )
                                ]
                            )
                        )
                    )

                elif event.postback.data[0:1] == "D":  # 如果回傳值為「坪數」

                    result = event.postback.data[2:].split('&')  # 回傳值的字串切割

                    house = IFoodie(
                        result[0],  # 行政區
                        result[1],  # 房屋類型
                        result[2],  # 租金
                        result[3]  # 坪數
                    )

                    line_bot_api.reply_message(  # 回復訊息文字
                        event.reply_token,
                        # 爬取該地區正在營業，且符合所選擇的美食類別的前五大最高人氣餐廳
                        TextSendMessage(text=house.scrape())
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

