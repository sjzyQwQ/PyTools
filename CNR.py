import json
import requests

national = json.loads(requests.post("https://apppc.cnr.cn/national",
                                    headers={"Content-Type": "application/json", "Host": "apppc.cnr.cn"}
                                    ).content.decode())

for detail in national["data"]["categories"][0]["detail"]:
    print(detail["name"], detail["other_info11"][0]["url"].split("?")[0])

local_list = requests.post("https://apppc.cnr.cn/local/list",
                           headers={"Content-Type": "application/json", "Host": "apppc.cnr.cn"})

for liveChannelPlace in local_list.json()["liveChannelPlace"]:
    local = json.loads(requests.post("https://apppc.cnr.cn/local", "{\"id\": " + liveChannelPlace["id"] + "}",
                                     headers={"Content-Type": "application/json",
                                              "Host": "apppc.cnr.cn"}).content.decode())
    for detail in local["data"]["categories"][0]["detail"]:
        print(detail["name"], detail["other_info11"][0]["url"].split("?")[0])
