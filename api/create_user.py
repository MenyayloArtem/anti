from helpers.create_json import create_json
from helpers.get_token import get_token
import requests
token = get_token()

url = "https://dolphin-anty-api.com/browser_profiles/mass"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type" : "application/json"
}

def create_user(data, folder):
    try:
        data = create_json(data, folder)
        res = requests.post(url=url, json=data, headers=headers).json()
        return res
    except Exception:
        raise (Exception)
        return False