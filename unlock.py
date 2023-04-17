import base64
vmess = input("Enter vmess URL: ")
url = vmess.split("://")
data = base64.b64decode(url[1]).decode('utf-8')
if(url[0] == "vmess"):
    print(data)
else:
    print("..")
