# coding:utf-8
import xadmin
from .models import Menu, Actions, WoXie, HduStudent

""" 修改默认样式 """


class GlobalSetting(object):
    site_title = 'KillMe'
    site_footer = 'by vermouth @2017'


# xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)


class MenuAdmin(object):
    list_display = ('id', 'count', 'modify_time')
    search_fields = ('id', 'count', 'modify_time', 'info')


class ActionAdmin(object):
    list_display = ('id', 'action_name', 'description', "level", "rule", 'action_type')
    search_fields = ('id', 'action_name', 'description', "level", "rule", 'action_type')


class WoXieAdmin(object):
    list_display = ('id', 'name', 'tel', 'code', 'e_mail', 'english_name')
    search_fields = ('id', 'tel', 'code', 'name', 'e_mail', 'english_name')


class HduStudentAdmin(object):
    list_display = ('id', 'code', 'name', 'sex', 'college', 'major', 'grade', 'idcard', 'home', 'nation', 'age', 'xing')
    search_fields = ('id', 'code', 'name', 'sex', 'college', 'major', 'grade', 'idcard', 'home', 'nation', 'age', 'xing')


xadmin.site.register(Menu, MenuAdmin)
xadmin.site.register(Actions, ActionAdmin)
xadmin.site.register(WoXie, WoXieAdmin)
xadmin.site.register(HduStudent, HduStudentAdmin)

