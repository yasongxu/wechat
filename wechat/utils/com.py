import ujson as json
import urllib2
import requests
from django.http.response import HttpResponse
from KillMe.settings import ALI_APP_CODE


def get_api_data(url):
    req = urllib2.Request(url)
    req.add_header("apikey", "65dbb2bef357f34e3af0aac3bb9b2d6f")
    resp = urllib2.urlopen(req)
    content = resp.read()
    print(content)
    if content:
        return content


def message_logger(fn):
    def wrapper(*args, **kwargs):
        print kwargs["message"]["content"]
        fn(*args, **kwargs)
        print('after')

    return wrapper


def save_log(message, reply):
    user_id = message.source


def ali_api_get(url):
    headers = {'Authorization': 'APPCODE ' + ALI_APP_CODE}
    content = requests.get(url, headers=headers, verify=False).content
    return json.loads(content)

