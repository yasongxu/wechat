# coding:utf-8
import time
from wechat.utils.com import json, get_api_data


def search_train(j):
    if not check_train(j)["status"]:
        d = {"status": False, "content": ""}
        return d
    try:
        result = get_train(j)
        str_f = '当前余票情况:\n'
        if result:
            for i in result:
                seat_str = ''
                str_this = '🚄车次：' + i['trainNo'] + '\n' + \
                           '出发时间：' + i['startTime'] + '\n' + \
                           '到达时间：' + i['endTime'] + '\n' + \
                           '运行时间：' + i['duration'] + '\n'
                for k in i['seatInfos']:
                    if k["remainNum"] <> 0:
                        seat_str += '座位：' + k['seat'] + '(' + k['seatPrice'] + '元)' + '\n' + '剩余：' + str(
                            k['remainNum']) + '\n'
                str_this = str_this + seat_str + "\n"
                str_f += str_this + "----------\n"
            if len(str_f) > 2000:
                str_f = '🚄当前余票情况:\n车次：   出发时间\n'
                for i in result:
                    str_this = i['trainNo'] + '   ' + i['startTime'] + '\n'
                    str_f += str_this
            return {"status": True, "content": str_f}
        else:
            return {"status": True, "content": str_f+"baidu api store 又要手动验证了"}
    except:
        return {"status": True, "content": str_f+"baidu api store 又要手动验证了"}


# 火车票查询
def get_train(h):
    all_data = []
    am_data = []
    pm_data = []
    night_data = []
    try:
        url = 'http://apis.baidu.com/qunar/qunar_train_service/s2ssearch?version=1.0&from=' + h[0] + '&to=' + h[
            1] + '&date=' + h[2]
        print(url)
        result = json.loads(get_api_data(url))
        contents = result["data"]["trainList"]
        for i in contents:
            single = {}
            single["seatInfos"] = i["seatInfos"]
            num = 0
            all_num = 0
            for j in single["seatInfos"]:
                all_num += 1
                if j["remainNum"] == 0:
                    num += 1
            if num == all_num:
                continue
            if i["trainType"] == "高速动车":
                single["trainType"] = "高铁"
            elif i["trainType"] == "动车组":
                single["trainType"] = "动车"
            else:
                single["trainType"] = "普通列车"
            single["trainNo"] = i["trainNo"]
            single["from"] = i["from"]
            single["to"] = i["to"]
            single["startTime"] = i["startTime"]
            single["endTime"] = i["endTime"]
            single["duration"] = i["duration"]
            all_data.append(single)
            if single["startTime"] >= "00:00" and single["startTime"] <= "12:00":
                am_data.append(single)
            elif single["startTime"] >= "12:00" and single["startTime"] <= "18:00":
                pm_data.append(single)
                print single
            else:
                night_data.append(single)

        if h[3] == "上午":
            return am_data
        elif h[3] == "下午":
            return pm_data
        elif h[3] == "晚上":
            return night_data
        else:
            return all_data
    except:
        return all_data


# 检测火车票查询格式正确


def check_train(key):
    try:
        re = key.split(" ")
        address = re[1].split("到")
        month_s = re[0][0:2]
        day_s = re[0][2:4]
        re[0] = "2017-" + month_s + "-" + day_s
        if is_valid_date(re[0]):
            address.append(re[0])
            if len(re) == 3:
                address.append(re[2])
            else:
                address.append("all")
            return {"status": True, "content": address}
    except:
        return {"status": False, "content": ""}


# 判断是否是一个有效的日期字符串


def is_valid_date(data_str):
    try:
        time.strptime(data_str, "%Y-%m-%d")
        return True
    except:
        return False