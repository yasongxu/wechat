# coding:utf-8
import random


def get(r):
    try:
        random_int = random.randint(1, 11)
        r_text = [[u'煎蛋精选', u'妹子图top10', u'http://114.215.94.123/static/images/jiandan/' + str(random_int) + ".jpg",
                   u'http://114.215.94.123/jiandan/']]
        return {"status": True, "content": r_text}
    except Exception, e:
        return {"status": False, "content": str(e)}


