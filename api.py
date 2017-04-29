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
        result = json.loads(get_apidata(url))
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
        traceback.print_exc()
        return all_data


# 构建火车票查询结果的xml
def get_trains_xml(j):
    try:
        datas = get_train(j)
        str_f = '当前余票情况:\n'
        for i in datas:
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
            for i in datas:
                # seat_str = ''
                str_this = i['trainNo'] + '   ' + i['startTime'] + '\n'
                str_f += str_this
        return str_f
    except:
        traceback.print_exc()
        return str_f


# 人脸检测
def facetoface(pic_url):
    str_f = ""
    try:
        API_KEY = '**'
        API_SECRET = 'Cj4c8bY1AjWmuVanzDC8yLntcn7U01aJ'
        url = "http://apicn.faceplusplus.com/v2/detection/detect?url=" + pic_url + "&api_secret=" + API_SECRET + "&api_key=" + API_KEY
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
        str_f += "检测结果：\n" + "年龄：" + age + "\n" + "性别：" + gender + "\n" + "人种：" + race + "\n" + "微笑度：" + smile + "\n"
        return str_f
    except:
        traceback.print_exc()
        str_f = "未检测到人脸"
        return str_f



