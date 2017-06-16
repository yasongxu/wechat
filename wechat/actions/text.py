# coding:utf-8
import inspect
from django.http import HttpResponse
from wechat.utils.com import json


class Demo(object):
    def xxx(self, num):
        print(num)


def all_actions():
    members = inspect.getmembers(Demo, predicate=inspect.ismethod)
    actions = [x[0] for x in members]
    return HttpResponse(json.dumps(actions))