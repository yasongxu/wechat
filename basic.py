# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage, VoiceMessage, EventMessage, ImageMessage
from cats.myapis import *
from cats.get_api import *
from apply.wuwu import *
from apply.crawl.get_pic import *

# 实例化 WechatBasic
wechat_instance = WechatBasic(
    token="**",
    appid="**",
    appsecret="***"
)


@csrf_exempt
def index(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')
        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")

    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')

    # 获取解析好的微信请求信息
    message = wechat_instance.get_message()

    # 关注事件以及不匹配时的默认回复
    response = wechat_instance.response_text(
        content=(
            '感谢您的关注！\n回复【功能】两个字查看支持的功能，还可以回复任意内容开始聊天'
        ))
    try:
        if isinstance(message, TextMessage):
            # 当前会话内容
            content = message.content.strip()
            if content == '**':
                reply_text = (
                    ''
                )

            elif '身份证' in content:
                idcard = content.strip('身份证')
                dd = id_card(idcard)
                ttt = '性别： ' + dd["sex"] + '\n' + '生日： ' + dd["birthday"] + '\n' + '户口地址： ' + dd["address"] + '\n'
                reply_text = (ttt)

            elif '煎蛋' in content:
                reply_text = get_response_news()
                response = wechat_instance.response_news(reply_text)

            elif phonecheck(content):
                dd = phone_add(content)
                ttt = '省份： ' + dd["province"] + '\n' + '城市： ' + dd["city"] + '\n' + '供应商： ' + dd["supplier"] + '\n'
                reply_text = (ttt)

            elif check_train(content):
                dd = get_trains_xml(check_train(content))
                if dd == '当前余票情况:\n':
                    dd += "无可乘班次/输入异常"
                reply_text = (dd)
            else:
                reply_text = (tuling(content))
            response = wechat_instance.response_text(content=reply_text)
        elif isinstance(message, VoiceMessage):
            reply_text = '语音信息我听不懂/:P-(/:P-(/:P-('
            response = wechat_instance.response_text(content=reply_text)

        elif isinstance(message, ImageMessage):
            reply_text = facetoface(message.picurl)
            print(reply_text)
            response = wechat_instance.response_text(content=reply_text)

        elif isinstance(message, EventMessage):
            if message.type == 'subscribe':  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
                reply_text = ('等你很久了，快来体验一下吧！^_^')

            elif message.type == "click":
                if message.key == "3_weather":
                    reply_text = ('     回复：煎蛋\n💧随机get妹子图(10张)....\n💧隐藏功能\n💧仅老司机交流，谨慎回复!')
                    # reply_text = ('回复：星座名称 \n例如：白羊座')
                elif message.key == "7_train":
                    reply_text = ('回复:   出发日期 **到**    \n例如：0506 上海到杭州   \n\n'
                                  '注意：\n🌕上午00:00-12:00\n🌓下午12:00-18:00\n🌑'
                                  '晚上18:00-24:00\n若班次太多，可指定时间段\n'
                                  '如：0506 上海到杭州 上午\n\n班次过多，则只显示班次和出发时间')

                elif message.key == "2_chat":
                    reply_text = ('来聊五毛钱的吧!\n\n已经接入图灵机器人，有问必答，来聊聊天吧例如：\n'
                                  '💧讲个笑话\n💧我很无聊\n💧你喜欢我吗？\n💧你是傻逼吗！！？\n')
                elif message.key == "1_music":
                    reply_text = ('发一张照片来测测吧！')
                else:
                    reply_text = message.key
            else:
                reply_text = ('你在说什么？')
            response = wechat_instance.response_text(content=reply_text)
        return HttpResponse(response, content_type="application/xml")
    except:
        traceback.print_exc()


