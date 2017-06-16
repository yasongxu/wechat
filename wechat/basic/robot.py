# coding:utf-8
from werobot import WeRoBot
from werobot.contrib.django import make_view
from KillMe.settings import token, APP_ID, APP_SECRET
from wechat.message.text.view import index as text_func
from wechat.message.image.view import image_func
from wechat.event.subscribe import subscribe_event
from wechat.event.face import face_to_face
from wechat.event.chat import chat_func
from wechat.event.star import star_func
from wechat.event.train import train_func
from wechat.event.wangpan import wang_func

robot = WeRoBot(
    token=token,
    APP_ID=APP_ID,
    APP_SECRET=APP_SECRET)

client = robot.client


@robot.text
def handler_text(message, session):
    reply = text_func(message, session)
    return reply


@robot.image
def handle_image(message, session):
    reply = image_func(message, session)
    return reply


@robot.subscribe
def handler_subscribe(message, session):
    return subscribe_event(message, session)


@robot.key_click("1_face")
def face(message, session):
    return face_to_face(message, session)


@robot.key_click("2_chat")
def chat(message, session):
    return chat_func(message, session)


@robot.key_click("6_star")
def star(message, session):
    return star_func(message, session)


@robot.key_click("7_train")
def train(message, session):
    return train_func(message, session)


@robot.key_click("8_wangpan")
def wang(message, session):
    return wang_func(message, session)


def m_v():
    return make_view(robot)