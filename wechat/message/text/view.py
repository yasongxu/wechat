# coding:utf-8
from django.dispatch import receiver
from wechat.basic.singals import view_init
from django.db.models import Q
from wechat.actions.text.view import TextActions
from wechat.models import Actions


def index(message, session):
    message = message.content
    default_actions = Actions.objects.filter(action_type="text", rule="*").order_by('level')
    rule_actions = Actions.objects.filter(~Q(rule="*")).filter(action_type="text")
    is_pass = False
    for action in default_actions:
        func = getattr(TextActions, action.action_name)
        result = func(message)
        if result["status"]:
            return result["content"]
        else:
            is_pass = False
    if not is_pass:
        for a in rule_actions:
            if a.rule in message:
                func = getattr(TextActions, a.action_name)
                res = func(message.strip(a.rule))
                if res["status"]:
                    return res["content"]
                else:
                    continue
            else:
                continue

    if not is_pass:
        return TextActions.tu_ling(message)






