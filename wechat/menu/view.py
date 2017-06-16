# coding:utf-8
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wechat.utils.com import json
from wechat.basic.robot import client
from wechat.models import Menu


@csrf_exempt
def refresh(request):
    d = {"status": False, "content": ""}
    try:
        menus = json.loads(request.body)
        result = client.create_menu(menus)
        if result["errcode"] == 0:
            new_menus = client.get_menu()
            last_count = Menu.objects.all().count()
            Menu.objects.create(info=json.dumps(new_menus, ensure_ascii=False), count=last_count + 1)
            d["status"] = True
            d["content"] = new_menus
        else:
            d["content"] = result["errmsg"]
    except Exception, e:
        d["content"] = str(e)
    return HttpResponse(json.dumps(d, ensure_ascii=False))


