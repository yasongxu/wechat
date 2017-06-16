# coding:utf-8

from wechat.models import HduStudent


def get(key):
    d = {"status": False, "content": ""}
    try:
        str_f = ""
        result = HduStudent.objects.filter(name=key)
        if result.exists():
            for i in result:
                str_ll = "姓名："+i.name+"\n"+"性别："+i.sex+"\n"+"学号："+i.code+"\n"+"学院："+i.college+"\n"+"专业："+i.major+"\n"+"民族："+i.nation+"\n"+"籍贯："+i.home+"\n"+"身份证号:"+i.idcard+"\n"
                str_f += str_ll
            d["status"] = True
            d["content"] = str_f
        else:
            d["status"] = True
            d["content"] = "查不到该学生信息"
    except Exception, e:
        d["status"] = False
        d["content"] = str(e)
    return d