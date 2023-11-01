from fake_useragent import UserAgent
import re
def create_json(data, folder):


    platform = data.get("operationSystem")

    if platform:
        el = str(re.search(r'(windows)|(macos)|(linux)', platform.lower()).group(0))
        platform = el
    else:
        platform = None

    username = data.get("username")
    timezone = data.get("timeZone")
    cpu = data.get("cores")
    memory = data.get("ram")

    defua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"

    cookies = data.get("cookies")

    if cookies:
        browser = list(cookies.keys())
        browser = list(filter(lambda b : not re.search(r'(opera)', b), browser))

        ua = None
        if len(browser):
            ua = UserAgent(browsers=browser, os=platform)
            ua = ua.random
    else:
        ua = defua

    data = {
    "common": {
        "platform": platform if platform else 'windows',
        "browserType": "anty",
        "useragent": {
            "mode": "manual",
            "value": ua if ua else defua
        },
        "webrtc": {
            "mode": "altered",
            "ipAddress": None
        },
        "canvas": {
            "mode": "noise"
        },
        "webgl": {
            "mode": "real"
        },
        "webglInfo": {
            "mode": "random"
        },
        "geolocation": {
            "mode": "real",
            "latitude": None,
            "longitude": None
        },
        "cpu": {
            "mode": "manual",
            "value": cpu if cpu else 4
        },
        "memory": {
            "mode": "manual",
            "value": memory if memory else 4
        },
        "timezone": {
            "mode": "manual",
            "value": timezone
        },
        "locale": {
            "mode": "auto",
            "value": None
        }
    },
    "items": [
        {
            "name": f"{folder} ::: {username}",
            "tags": [],
            "mainWebsite": "",
            "notes": {
                "content": None,
                "color": "blue",
                "style": "text",
                "icon": None
            },
            "proxy": None,
            "statusId": 0,
            "doNotTrack": False
        }
    ]
}
    return data