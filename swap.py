import os
import json
import httpx
import urllib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = input("url> ")
swid = int(input("server id> "))
selftoken = input("delete token> ")
selftoken2 = input("claim token> ")

httpx.delete(f"https://ptb.discordapp.com/api/invite/{url}", headers={"Authorization": selftoken}, verify=False)
r = httpx.patch(f"https://ptb.discordapp.com/api/guilds/{swid}/vanity-url", headers={"Authorization": selftoken2}, json={"code": url}, verify=False)
print(f"{r.json} {r.json()} {r.status_code}")
os.system("pause")