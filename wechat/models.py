# coding:utf-8

from django.db import models


class Menu(models.Model):
    info = models.TextField(u'按钮详情', blank=True, null=True)
    modify_time = models.DateTimeField(u'刷新时间', auto_now_add=True)
    count = models.IntegerField(u'刷新次数', blank=True, null=True)
    backup = models.TextField(u'测试字段', blank=True, null=True)

    def to_dict(self):
        return dict([(attr, str(getattr(self, attr))) for attr in [f.name for f in self._meta.fields]])

    class Meta:
        ordering = ("-id",)
        verbose_name_plural = verbose_name = u'按钮组'


""" 优先级：1为最高"""


class Actions(models.Model):
    action_type = models.CharField(u'类型', blank=True, null=True, max_length=100)
    action_name = models.CharField(u'名称', blank=True, null=True, max_length=100)
    level = models.IntegerField(u'优先级', blank=True, null=True)
    rule = models.CharField(u'匹配规则', blank=True, null=True, max_length=100)
    description = models.CharField(u'中文描述', blank=True, null=True, max_length=100)
    back = models.CharField(u'back', blank=True, null=True, max_length=100)

    def to_dict(self):
        return dict([(attr, str(getattr(self, attr))) for attr in [f.name for f in self._meta.fields]])

    class Meta:
        ordering = ("-id",)
        verbose_name_plural = verbose_name = u'所有动作'


class WoXie(models.Model):
    code = models.CharField(u'编号', blank=True, null=True, max_length=256)
    name = models.CharField(u'名字', blank=True, null=True, max_length=256)
    e_mail = models.CharField(u'电子邮箱', blank=True, null=True, max_length=256)
    tel = models.CharField(u'电话', blank=True, null=True, max_length=256)
    fenji = models.CharField(u'分机', blank=True, null=True, max_length=256)
    seat = models.CharField(u'座位', blank=True, null=True, max_length=256)
    state = models.CharField(u'坐席', blank=True, null=True, max_length=256)
    english_name = models.CharField(u'英文名', blank=True, null=True, max_length=256)

    def to_dict(self):
        return dict([(attr, str(getattr(self, attr))) for attr in [f.name for f in self._meta.fields]])

    class Meta:
        ordering = ("-id",)
        verbose_name_plural = verbose_name = u'我携'


class HduStudent(models.Model):
    code = models.CharField(u'编号', blank=True, null=True, max_length=256)
    name = models.CharField(u'名字', blank=True, null=True, max_length=256)
    sex = models.CharField(u'性别', blank=True, null=True, max_length=256)
    college = models.CharField(u'学院', blank=True, null=True, max_length=256)
    major = models.CharField(u'专业', blank=True, null=True, max_length=256)
    grade = models.CharField(u'年级', blank=True, null=True, max_length=256)
    grade_now = models.CharField(u'当前年级', blank=True, null=True, max_length=256)
    sort = models.CharField(u'类别', blank=True, null=True, max_length=256)
    state = models.CharField(u'是否在校', blank=True, null=True, max_length=256)
    state_xueji = models.CharField(u'学籍状态', blank=True, null=True, max_length=256)
    idcard = models.CharField(u'身份证号', blank=True, null=True, max_length=256)
    home = models.CharField(u'生源地', blank=True, null=True, max_length=256)
    nation = models.CharField(u'民族', blank=True, null=True, max_length=256)
    age = models.CharField(u'年龄', blank=True, null=True, max_length=256)
    month = models.CharField(u'月份', blank=True, null=True, max_length=256)
    year = models.CharField(u'年份', blank=True, null=True, max_length=256)
    xing = models.CharField(u'姓氏', blank=True, null=True, max_length=256)

    def to_dict(self):
        return dict([(attr, str(getattr(self, attr))) for attr in [f.name for f in self._meta.fields]])

    class Meta:
        ordering = ("-id",)
        verbose_name_plural = verbose_name = u'Hdu学籍'


class MessageLog(models.Model):
    user_id = models.CharField(u'用户id', blank=True, null=True, max_length=256)
    user_name = models.CharField(u'用户名', blank=True, null=True, max_length=256)
    request = models.CharField(u'发送内容', blank=True, null=True, max_length=256)
    response = models.CharField(u'返回内容', blank=True, null=True, max_length=256)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    def to_dict(self):
        return dict([(attr, str(getattr(self, attr))) for attr in [f.name for f in self._meta.fields]])

    class Meta:
        ordering = ("-id",)
        verbose_name_plural = verbose_name = u'消息日志'


