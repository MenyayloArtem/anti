import re
import json
from helpers.get_dir import get_dir

def parse_logs(folder):
    files = get_dir(f"./logs/{folder}", files=True, ext=".txt")


    f = open("info_filenames.json")
    data = json.load(f)

    filename = None
    for file in files:
        if file in data:
            filename = file
            break
    
    # print(filename)
    
    path = f"./logs/{folder}/{filename}"

    keys = ["UserName", "TimeZone", "Operation System", "Current Language", "ScreenSize"]
    parseHard = False
    hardStr = ""
    res = {}

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file.readlines():
                if not parseHard:
                    for key in keys:
                        if key in line:
                            line = line.split(":",1)
                            line = line[1].strip()
                            res[key] = line
                        
                        if "Hardwares" in line:
                            parseHard = True
                else:
                    if (line != "\n"):
                        hardStr += line
                    else:
                        break

            
                        
        hardStr = hardStr.split("\n")

        if res.get("Operation System") :
            el = res["Operation System"]
            el = str(re.search(r'(windows)|(macos)|(linux)', el.lower()).group(0))
            res["Operation System"] = el
        else:
            res["Operation System"] = None
            

        for line in hardStr:
            if "Cores" in line:
                line = line.split(",",1)
                line = line[1].strip()
                line = line.split(" ")
                res["Cores"] = line[0]
            
            if "RAM" in line:
                line = (re.search(r'(\d+ bytes)|(RAM: \d+)', line)).group(0)
                num = int(re.search(r'\d+', line).group(0))
                num = round(num / 1024 / 1024 / 1024)
                res["RAM"] = num

        string = res["ScreenSize"]
        sizes = re.findall(r'\d+', string)
        res["ScreenSize"] = f"{sizes[0]}x{sizes[1]}"

        return res
    except Exception:
        # raise Exception
        print ("Ошибка при парсинге логов, пропускаю")
        return False