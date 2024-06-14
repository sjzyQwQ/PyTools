'''
ClassIsland to ZongziTek 黑板贴
This Python file is edited by Misaka10072
Last modified: 2024/6/15
GitHub: https://github.com/sjzyQwQ/PyTools
'''

import json
import time
import datetime

Weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def newLesson(day: str, Subject: str, StartTime: str, EndTime: str, IsSplitBelow: bool = False, IsStrongClassOverNotificationEnabled: bool = False):
    Timetable[day].append({"Subject": Subject, "StartTime": StartTime, "EndTime": EndTime, "IsSplitBelow": IsSplitBelow, "IsStrongClassOverNotificationEnabled": IsStrongClassOverNotificationEnabled})


def generateTimetable():
    currentTimeLayout = Profiles["TimeLayouts"][currentClassPlan["TimeLayoutId"]]["Layouts"]
    classTime = []
    IsSplit = []
    for num in range(len(currentTimeLayout)):
        if currentTimeLayout[num]["TimeType"] == 0:
            classTime.append(num)
            IsSplit.append(False)
        elif currentTimeLayout[num]["TimeType"] == 2:
            IsSplit[len(classTime) - 1] = True
    for num in range(len(classTime)):
        Second = {"Start": time.strptime(currentTimeLayout[classTime[num]]["StartSecond"], "%Y-%m-%dT%H:%M:%S+08:00"), "End": time.strptime(currentTimeLayout[classTime[num]]["EndSecond"], "%Y-%m-%dT%H:%M:%S+08:00")}
        currentSubject = Profiles["Subjects"][currentClassPlan["Classes"][num]["SubjectId"]]
        newLesson(Weekday[currentClassPlan["TimeRule"]["WeekDay"]], currentSubject["Name"], time.strftime("%H:%M:%S", Second["Start"]), time.strftime("%H:%M:%S", Second["End"]), True if IsSplit[num] else False)


def save(mode):
    file = open("Timetable.json", mode)
    json.dump(Timetable, file)


try:
    file = open("Settings.json")
    Settings = json.load(file)
except FileNotFoundError:
    print("没有找到ClassIsland的配置文件\n可能的原因:\n\t1. 未完成ClassIsland的初始化\n\t2. 未将本程序置于ClassIsland目录中")
finally:
    file.close()

SelectedProfile = Settings["SelectedProfile"]
SingleWeekStartTime = time.strptime(Settings["SingleWeekStartTime"], "%Y-%m-%dT%H:%M:%S")

if (datetime.date.today() - datetime.date(SingleWeekStartTime[0], SingleWeekStartTime[1], SingleWeekStartTime[2])).days % 14 < 7:  # 相对单周
    IsSingleWeek = True
else:  # 相对双周 (datetime.date.today()-datetime.date(SingleWeekStartTime[0],SingleWeekStartTime[1],SingleWeekStartTime[2])).days%14>7
    IsSingleWeek = False

with open("Profiles/" + SelectedProfile) as file:
    Profiles = json.load(file)

Timetable = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": [], "Temp": []}

for id in Profiles["ClassPlans"]:
    currentClassPlan = Profiles["ClassPlans"][id]
    if currentClassPlan["IsEnabled"]:
        if IsSingleWeek and currentClassPlan["TimeRule"]["WeekCountDiv"] in [0, 1]:  # 相对单周
            generateTimetable()
        elif not IsSingleWeek and currentClassPlan["TimeRule"]["WeekCountDiv"] in [0, 2]:  # 相对双周
            generateTimetable()

try:
    save("x")
except FileExistsError:
    while True:
        option = input("文件已存在，是否覆盖保存 (y/N): ")
        if option.lower() == 'y':
            save("w")
            break
        elif option.lower() == 'n':
            print("注意: 由于文件已存在, 取消保存! ")
            break
finally:
    file.close()