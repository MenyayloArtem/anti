from helpers.get_headers import get_headers
import requests

users = []

def fetch_users(page):
    url = f"https://dolphin-anty-api.com/browser_profiles?page={page}"
    headers = get_headers()
    res = requests.get(url=url, headers=headers).json()
    return res.get("data")

def get_users(page = 1):
    print (f"Запрос пользователей: страница {page}")
    fetched_users = fetch_users(page)
    users.extend(fetched_users)

    if (len(fetched_users) >= 50):
        get_users(page + 1)
    else:
        print ("Пользователи успешно получены")
        return users
