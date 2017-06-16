# coding:utf-8
from ctrip_user import get as woxie_user
from constellation import demo as demo_func
from tuling import tu_ling as tu_ling_func
from trains import search_train as search_train_func
from hdu import get as hdu_student_func
from jian_dan import get as jian_dan_func
from yunpan import search as yun_pan_func


class TextActions(object):
    def __init__(self):
        self.name = ""

    @staticmethod
    def woxie_user(key):
        return woxie_user(key)

    @staticmethod
    def hdu_student(key):
        return hdu_student_func(key)

    @staticmethod
    def demo(key):
        return demo_func(key)

    @staticmethod
    def tu_ling(key):
        return tu_ling_func(key)

    @staticmethod
    def search_train(key):
        return search_train_func(key)

    @staticmethod
    def jian_dan(key):
        return jian_dan_func(key)

    @staticmethod
    def yun_pan(key):
        return yun_pan_func(key)

    @property
    def description(self):
        return {
            "woxie_user": {"name": "我携用户查询", "level": 1, "rule": "携程"},
            "hdu_student": {"name": "Hdu学籍信息查询", "level": 1, "rule": "杭电"},
            "demo": {"name": "测试案例", "level": 1, "rule": "测试"},
            "tu_ling": {"name": "图灵机器人", "level": 1, "rule": "图灵"},
            "search_train": {"name": "火车票查询", "level": 1, "rule": "*"},
            "jian_dan": {"name": "煎蛋图片top10", "level": 1, "rule": "煎蛋"},
            "yun_pan": {"name": "网盘搜索资源", "level": 1, "rule": "网盘"},
        }
