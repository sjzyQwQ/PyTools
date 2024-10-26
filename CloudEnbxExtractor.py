'''
希沃白板云端课件导出器
This Python file is edited by Misaka10072
Last modified: 2024/10/26
GitHub: https://github.com/sjzyQwQ/PyTools
'''

import os
import json
import sqlite3
import shutil

with sqlite3.connect("{}/Seewo/Users/User.db".format(os.getenv("AppData"))) as sqlite3connection:
    cursor = sqlite3connection.cursor()
    users = []
    index = 0
    for user in cursor.execute("SELECT UserId,UserName FROM User;"):
        users.append({})
        users[index]["UserId"] = user[0]
        users[index]["UserName"] = user[1]
        index += 1

for i in range(len(users)):
    print("{}. {} ({})".format(i + 1, users[i]["UserName"], users[i]["UserId"]))
while True:
    selection = input("请选择一个用户: ")
    try:
        selection = int(selection)
    except:
        continue
    if selection > 0 and selection <= len(users):
        break

localCoursewares = [dir for dir in os.listdir("{}/Seewo/EasiNote5/Data/{}/Courseware".format(os.getenv("AppData"), users[selection - 1]["UserId"])) if os.path.isdir("{}/Seewo/EasiNote5/Data/{}/Courseware/{}".format(os.getenv("AppData"), users[selection - 1]["UserId"], dir))]
index = 0
for courseware in localCoursewares:
    with open("{0}/Seewo/EasiNote5/Data/{1}/Courseware/{2}/{2}.json".format(os.getenv("AppData"), users[selection - 1]["UserId"], courseware), encoding="utf-8-sig") as file:
        coursewareInfo = json.load(file)
        print("{}. {} ({})".format(index + 1, coursewareInfo["Courseware"]["Name"], courseware))
        index += 1
while True:
    selection = input("请选择一个课件: ")
    try:
        selection = int(selection)
    except:
        continue
    if selection > 0 and selection <= len(localCoursewares):
        break

shutil.copytree("{}/Seewo/EasiNote5/Data/{}/Courseware/{}".format(os.getenv("AppData"), users[selection - 1]["UserId"], localCoursewares[selection - 1]), "{}/{}".format(os.getenv("temp"), localCoursewares[selection - 1]))
os.mkdir("{}/{}/Resources".format(os.getenv("Temp"), localCoursewares[selection - 1]))
os.mkdir("{}/{}/Slides".format(os.getenv("Temp"), localCoursewares[selection - 1]))
with open("{0}/{1}/{1}.json".format(os.getenv("temp"), localCoursewares[selection - 1]), encoding="utf-8-sig") as file:
    coursewareInfo = json.load(file)
    for coursewareFile in coursewareInfo["CoursewareFiles"]:
        shutil.move("{}/{}".format(os.getenv("temp"), coursewareFile["FilePath"]), "{}/{}/{}".format(os.getenv("temp"), localCoursewares[selection - 1], coursewareFile["RelativePath"]))

shutil.make_archive("{}.enbx".format(coursewareInfo["Courseware"]["Name"]), "zip", "{}/{}".format(os.getenv("temp"), localCoursewares[selection - 1]))
shutil.move("{}.enbx.zip".format(coursewareInfo["Courseware"]["Name"]), "{}.enbx".format(coursewareInfo["Courseware"]["Name"]))

shutil.rmtree("{}/{}".format(os.getenv("temp"), localCoursewares[selection - 1]))
