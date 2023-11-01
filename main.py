from api.import_cookies import import_cookies
from parsers.parse_cookies import parse_cookies
from parsers.parse_logs import parse_logs
from api.create_user import create_user
from api.get_users import get_users
from helpers.get_dir import get_dir
from helpers.write_json import write_json
from helpers.get_cookies import get_cookies
import os
import re
import json
import subprocess

def main():
    parsed_folders = get_dir("./users", True, ".json")
    parsed_folders = list(map(lambda f : f.split(".")[0], parsed_folders))
    
    for p in parsed_folders:
        print (p)

    # Получаем папки
    folders = get_dir("./logs",files=False)
    for folder in folders:
        try:

            if folder == ".DS_Store":
                continue

            if folder in parsed_folders:
                print("\n", folder, "уже обработан")
                continue

            print(f"\nОбработка логов: {folder}")


            # Получаем имя файла
            files = get_dir(f"./logs/{folder}", files=True, ext=".txt")
            f = open("info_filenames.json")
            data = json.load(f)

            filename = None
            for file in files:
                if file in data:
                    filename = file
                    break

            
            # Читаем php
            proc = subprocess.Popen(f"php Php/src/parser.php \"{folder}\" {filename}", shell=True, stdout=subprocess.PIPE)
            res = proc.stdout.read()
            parsedUser = json.loads(res)
            print (parsedUser)

            if not parsedUser.get("username"):
                print ("Не распарсилось...")
                continue

            
            # Получаем куки
            cookies = False
            # cookies = get_cookies(folder)

            
            # Создаём профиль
            user = create_user(parsedUser, folder)
            if user and user.get("success"):
                print (f"Пользователь {parsedUser['username']} создан")
                user_id = user["ids"][0]
                write_json(f"./users/{folder}.json", parsedUser)

                # Грузим куки
                if cookies:
                    parsedUser["cookies"] = cookies
                    browser = list(parsedUser["cookies"].keys())[0]
                    res = import_cookies(user_id, parsedUser["cookies"][browser])
                    print (f"Куки: {res}\n")

            else:
                if user.get("error"):
                    print(user["error"]["text"])
                    return
                
                if user.get("failed"):
                    print (user.get("failed"))

        except:
            print ("Ошибка парсинга, пропускаю")

if __name__ == "__main__":
    main()