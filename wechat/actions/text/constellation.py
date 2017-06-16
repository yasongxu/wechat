# coding:utf-8
from wechat.utils.com import json, get_api_data


def get(key):
    d = {"status": False, "content": ""}
    try:
        url = 'http://apis.baidu.com/bbtapi/constellation/constellation_query?consName=' + key + '&type=today'
        data = {}
        result = json.loads(get_api_data(url))
        data["date"] = str(result["date"])
        data["name"] = result["name"]
        data["all"] = str(result["all"])
        data["color"] = result["color"]
        data["number"] = str(result["number"])
        data["QFriend"] = result["QFriend"]
        data["summary"] = result["summary"]
        d["status"] = True
        reply = '日期： ' + data["date"] + '\n' + '星座： ' + data["name"] + '\n' + '综合指数： ' + \
                data["all"] + '\n' + '幸运颜色： ' + data["color"] + '\n' + '幸运数字： ' + \
                data["number"] + '\n' + '速配星座： ' + data["QFriend"] + '\n' + '总结： ' + data["summary"] + '\n'

        d["content"] = reply
    except Exception, e:
        import traceback
        traceback.print_exc()
        d["status"] = False
        d["content"] = str(e)
    return d


def demo(key):
    d = {"status": False, "content": ""}
    try:
        d["status"] = True
        d["content"] = "demo"
    except Exception, e:
        d["status"] = False
        d["content"] = str(e)
    return d