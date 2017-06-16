# coding:utf-8
from wechat.utils.com import json, get_api_data
import requests
# 图灵机器人


# 图灵机器人
def tu_ling(h):
    key = "69cdc5c5fb4e42a491b60a65f6b26058"
    user_id = "vermouth1994"
    try:
        url = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+h+'&userid='+user_id
        result = json.loads(requests.get(url).content)
        return result["text"]
    except:
        return "臣妾无法理解您的指示"