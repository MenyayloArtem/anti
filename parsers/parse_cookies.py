import re

def parse_cookies(path,file):
    temp_file = file.replace(r'google', "chrome")
    browser = re.search(r'(chrome)|(edge)|(opera)|(firefox)', temp_file.lower())
    if browser:
        browser = browser.group(0)

    with open(f"{path}/{file}", "r", errors="ignore") as f:
        
        cookies = []
        for line in f.readlines():
            if line:
                line = line.split("\t")
                cookies.append({
                    "domain" : line[0],
                    "httpOnly" : line[1],
                    "secure" : line[3],
                    "key" : line[5],
                    "value" : line[4]
                })
        return {
            "browser" : browser,
            "cookies" : cookies
        }