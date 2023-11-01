from helpers.get_dir import get_dir
from parsers.parse_cookies import parse_cookies
import os

def get_cookies (folder):
    path = f"./logs/{folder}/Cookies"
    need_cookies = os.path.isdir(path)

    if need_cookies:
        cookiesFiles = get_dir(path, files=True, ext=".txt")
        cookies = {}

        for file in cookiesFiles:
            
            data = (parse_cookies(path, file))
            
            if (not cookies.get(f"{data['browser']}")):
                cookies[f"{data['browser']}"] = data["cookies"]
            else:
                cookies[f"{data['browser']}"].extend(data["cookies"])
        
        return cookies
    else:
        return False