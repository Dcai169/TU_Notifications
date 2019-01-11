from requests import post
import keys
url = "https://api.pushbullet.com"

def send_notification(type_, title, body, url_):
    data = {"type":type_,
            "title":title,
            "body":body,
            "url":url_}
    p = post(url+"/v2/pushes", data=data, headers=keys.pbkey)

    return p