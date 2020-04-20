import re

url = input("input an address")
pattern = r'^(http|https|ftp|file)://(.+?)'
Obj = re.search(pattern, url)
if Obj:
    print(url, "通信协议合法")
else:
    print(url, "通信协议不合法")
