# coding:utf-8

from wechat.utils.com import json, ali_api_get
from KillMe.settings import ALI_Net_Disk_Url


def search(j):
    try:
        file_types = {"文件夹": "folder.jpg", "文件": "file.png", "压缩包": "zip.png"}
        url = ALI_Net_Disk_Url + "?page=1&q=" + j
        content = ali_api_get(url)
        all_list = content["showapi_res_body"]["pagebean"]["contentlist"]
        reply = []
        for i, r in enumerate(all_list[:4]):
            if "tags" in r:
                r["file_type"] = r["tags"][0]
            title_text = "[" + r["file_type"] + "] " + j + " " + r["category"] + "资源下载" + str(i + 1)
            if i == 0:
                pic_url = "http://114.215.94.123/static/images/wangpan/baiduyun.png"
            else:
                pic_url = "http://114.215.94.123/static/images/wangpan/download.png"
            x = [title_text, "", pic_url, r["url"]]
            reply.append(x)
        return {"status": True, "content": reply}
    except Exception, e:
        return {"status": True, "content": str(e)}

