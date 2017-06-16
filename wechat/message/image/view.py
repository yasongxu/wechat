# coding:utf-8
import requests
import base64
from io import BytesIO
import json
import multiprocessing
# 图片检测


def image_func(message, session):
    result = []
    pool = multiprocessing.Pool(processes=40)
    pic_url = message.img
    result.append(pool.apply_async(face_to_face, (pic_url, )))

    res_dic = {"人脸": face_to_face(pic_url), "植物": plant(pic_url), "汽车": car(pic_url)}
    reply = ""
    for i in res_dic:
        if res_dic[i] != "无":
            reply += "\n-------" + i + "检测结果" + "-------\n" + res_dic[i] + "\n"
    if reply == "":
        reply == "未检测到任何元素"
    return reply


def face_to_face(pic_url):
    str_f = ""
    try:
        api_key = '64bfc6eba2d0e323e9c1ff6852f00400'
        api_script = 'Cj4c8bY1AjWmuVanzDC8yLntcn7U01aJ'
        url = "http://apicn.faceplusplus.com/v2/detection/detect?url=" + pic_url + "&api_secret=" + api_script + "&api_key=" + api_key
        r = requests.get(url).json()
        content = r["face"][0]["attribute"]
        age = str(content["age"]["value"]) + "岁"
        gender = content["gender"]["value"]
        if gender == "Female":
            gender = "女性"
        else:
            gender = "男性"
        race = content["race"]["value"]
        smile = str(content["smiling"]["value"]) + "%"
        str_f += "💂\n" + "年龄：" + age + "\n" + "性别：" + gender + "\n" + "人种：" + race + "\n" + "微笑度：" + smile + "\n"
    except:
        str_f = "无"
    return str_f


def plant(pic_url):
    try:
        buffered = BytesIO(requests.get(pic_url).content)
        img_base64 = base64.b64encode(buffered.getvalue())
        url = "http://plantgw.nongbangzhu.cn/plant/recognize"
        headers = {'Authorization': 'APPCODE ' + "8c72c6deb55342b59a1c06a4c28f80c1",
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        content = requests.post(url, headers=headers, data={"img_base64": img_base64}).content
        content = json.loads(content)
        reply = ""
        if content["Status"] == 0:
            results = content["Result"]
            for i, result in enumerate(results[:2]):
                reply += "🌱\n" + "植物名称：" + result["Name"] + "\n" + "别名：" + \
                         result[
                             "AliasName"] + "\n" + "所属科类：" + result[
                             "Family"] + "\n" + "所属属名：" + result["Genus"] + "\n"
            return reply
        else:
            return "无"
    except:
        return "无"


def car(pic_url):
    try:
        buffered = BytesIO(requests.get(pic_url).content)
        img_base64 = base64.b64encode(buffered.getvalue())
        url = "http://carrec.market.alicloudapi.com/CarSeeFromBase64"
        headers = {'Authorization': 'APPCODE ' + "8c72c6deb55342b59a1c06a4c28f80c1",
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        content = requests.post(url, headers=headers, data={"image_base64": img_base64}).content
        content = json.loads(content)
        reply = ""
        if content["message"] == "OK":
            results = content["result"]["cars"][0]["car"]
            for i, result in enumerate(results[:2]):
                reply += "🚗\n" + "汽车品牌：" + result.get("brand_name", "") + "\n" + "系列名：" + \
                         result.get("series_name", "")+ "\n"
            return reply
        else:
            return "无"
    except:
        return "无"