# coding:utf-8
from robot import client


def refresh_user(request):
    followers = client.get_followers()
    print(followers)
