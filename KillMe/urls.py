# coding:utf-8
from django.conf.urls import url, include
# from django.contrib import admin
from wechat.basic.robot import m_v
from wechat.menu.view import refresh as refresh_menu
from wechat.actions.view import all_actions as refresh_actions
from wechat.basic.user import refresh_user
from xadmin.plugins import xversion
import xadmin

xadmin.autodiscover()


xversion.register_models()

urlpatterns = [
    url(r'admin/', include(xadmin.site.urls)),
    url(r'^robot/', m_v()),
    url(r'^refresh_menu/', refresh_menu),
    url(r'^refresh_actions/', refresh_actions),
    url(r'^refresh_user/', refresh_user),
]