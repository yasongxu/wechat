# coding:utf-8
import inspect
from django.http import HttpResponse
from wechat.utils.com import json
from wechat.models import Actions
from text.view import TextActions
from image.view import ImageActions


def all_actions(request):
    d = {"status": False, "content": ""}
    try:
        ta = TextActions()
        ia = ImageActions()
        text_members = inspect.getmembers(TextActions, predicate=inspect.isfunction)
        image_members = inspect.getmembers(ImageActions, predicate=inspect.isfunction)
        for x in text_members:
            print x[0]
        text_actions = [{"action_type": "text", "action_name": x[0], "description": ta.description[x[0]]["name"],
                         "level": ta.description[x[0]]["level"], "rule": ta.description[x[0]]["rule"]} for x in
                        text_members]
        image_actions = [{"action_type": "image", "action_name": y[0], "description": ia.description[x[0]],
                          "level": ta.description[x[0]]["level"], "rule": ta.description[x[0]]["rule"]} for y in
                         image_members]
        actions = text_actions + image_actions
        for a in actions:
            existed = Actions.objects.filter(action_name=a["action_name"], action_type=a["action_type"])
            if existed:
                existed.update(description=a["description"], level=a["level"], rule=a["rule"])
            else:
                Actions.objects.create(action_type=a["action_type"], description=a["description"],
                                       action_name=a["action_name"], level=a["level"], rule=a["rule"])
        d["status"] = True
        d["content"] = actions
    except Exception, e:
        import traceback
        traceback.print_exc()
        d["status"] = False
        d["content"] = str(e)
    return HttpResponse(json.dumps(d))