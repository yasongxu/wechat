# coding:utf-8

from wechat.models import WoXie

"""
get ctrip ops　user info
"""


def get(key):
    d = {"status": False, "content": ""}
    try:
        result = WoXie.objects.filter(name__contains=key)
        if result.exists():
            phone_list = []
            user_list = []
            str_f = ""
            for i in result:
                if "1" in i.tel:
                    if i.tel not in phone_list or i.name not in user_list:
                        phone_list.append(i.tel)
                        user_list.append(i.name)
                        str_ll = "姓名：" + i.name + "\n" + "手机号码：" + i.tel + "\n"
                        str_f += str_ll
            d["status"] = True
            d["content"] = str_f
        else:
            d["status"] = False
            d["content"] = "没有此人信息"
    except Exception, e:
        d["status"] = False
        d["content"] = str(e)
    return d
