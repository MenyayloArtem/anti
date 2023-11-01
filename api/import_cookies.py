from helpers.get_token import get_token
import requests

token = get_token()

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type" : "application/json"
}

def import_cookies(id, cookies):
    url = f"https://sync.anty-api.com/?actionType=importCookies&browserProfileId={id}"
    json = {
        "cookies" : cookies
    }
    res = requests.post(url, json=json, headers=headers).json()
    return res
