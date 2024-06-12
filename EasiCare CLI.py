'''
EasiCare CLI
This Python file is edited by Misaka10072
Last modified: 2024/6/12
GitHub: https://github.com/sjzyQwQ/PyTools
'''

import argparse
import requests
import time

parser = argparse.ArgumentParser(description="班级优化大师 CLI")
parser.add_argument("-T", "--at", "--accessToken", dest="accessToken", required=True, metavar='', help="Cookie: accessToken")
parser.add_argument("-t", "--ct", "--csrfToken", dest="csrfToken", metavar='', required=True, help="Header: x-csrf-token")
parser.add_argument("-m", "--cm", "--connectMagick", dest="connectMagick", metavar='', required=True, help="Cookie: connect.magick")
args = parser.parse_args()


def CLASSROOM_FETCH():  # 获取班级列表
    response = requests.post("https://care.seewo.com/app/apis.json", data='{"action":"CLASSROOM_FETCH"}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})
    return response.json()["data"]["classrooms"]


def STUDENT_FETCH_LIST(classroomId):  # 获取班级学生列表
    response = requests.post("https://care.seewo.com/app/apis.json", data='{"action":"STUDENT_FETCH_LIST","params":{"classroomId":"' + classroomId + '"}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})
    return response.json()["data"]["students"]


def GROUP_COLLECTION_GET_LIST(classId):  # 获取班级小组列表
    response = requests.post("https://care.seewo.com/app/apis.json", data='{"action":"GROUP_COLLECTION_GET_LIST","params":{"classId":"' + classId + '"}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})
    return response.json()["data"]["classTeamPlans"]


def CLASSROOM_FETCH_REPORT(timeline, classId, creatorId='', startTime="0", endTime="0"):  # 获取班级报表总体数据
    response = requests.post("https://care.seewo.com/app/apis.json", data='{"action":"CLASSROOM_FETCH_REPORT","params":{"timeline":' + timeline + ',"classId":"' + classId + '","classUid":"' + classId + '","creatorId":"' + creatorId + '","pageSize":2147483646,"page":1,"lastPageNum":0,"lastMinRowNum":0,"startTime":' + startTime + ',"endTime":' + endTime + ',"start":' + startTime + ',"end":' + endTime + '}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})
    if response.json()["code"] == 200:
        return response.json()["data"]
    elif response.json()["code"] == 404:
        return {"detail": []}


def CLASSROOM_FETCH_PERFORMANCE(timeline, classId, creatorId='', startTime="0", endTime="0"):  # 获取班级报表总体点评列表
    response = requests.post("https://care.seewo.com/app/apis.json", data='{"action":"CLASSROOM_FETCH_PERFORMANCE","params":{"timeline":' + timeline + ',"page":1,"pageSize":2147483646,"classId":"' + classId + '","classUid":"' + classId + '","creatorId":"' + creatorId + '","lastPageNum":0,"lastMinRowNum":0,"startTime":' + startTime + ',"endTime":' + endTime + ',"start":' + startTime + ',"end":' + endTime + '}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})
    return response.json()["data"]["performances"]


def STUDENT_FETCH_REPORT(timeline, classId, studentId, creatorId='', start="0", end="0"):  # 获取班级报表单个学生数据
    response = requests.post("https://care.seewo.com/app/apis.json", data='{"action":"STUDENT_FETCH_REPORT","params":{"timeline":' + timeline + ',"classId":"' + classId + '","studentId":"' + studentId + '","creatorId":"' + creatorId + '","pageSize":2147483646,"page":1,"lastPageNum":0,"lastMinRowNum":0,"start":' + start + ',"end":' + end + '}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})
    if response.json()["code"] == 200:
        return response.json()["data"]
    elif response.json()["code"] == 404:
        return {"detail": []}


def STUDENT_FETCH_PERFORMANCE(timeline, classId, studentId, creatorId='', start="0", end="0"):  # 获取班级报表单个学生点评列表
    response = requests.post("https://care.seewo.com/app/apis.json", data='{"action":"STUDENT_FETCH_PERFORMANCE","params":{"timeline":' + timeline + ',"page":1,"pageSize":2147483646,"classId":"' + classId + '","studentId":"' + studentId + '","creatorId":"' + creatorId + '","lastPageNum":0,"lastMinRowNum":0,"start":' + start + ',"end":' + end + '}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})
    return response.json()["data"]["performances"]


def MEDAL_FETCH_BY_CLASSROOM(cid):
    response = requests.post("https://care.seewo.com/app/apis.json", data='{"action":"MEDAL_FETCH_BY_CLASSROOM","params":{"cid":"' + cid + '"}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})
    return response.json()["data"]


def SET_MEDAL(type, performanceId, studentId, classId):  # 发送点评
    if type == "STUDENT_SINGLE":
        requests.post("https://care.seewo.com/app/apis.json", data='{"action":"STUDENT_SET_MEDAL_SINGLE","params":{"performanceId":"' + performanceId + '","studentId":"' + studentId + '"}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})
    elif type == "STUDENT_MULTI":
        requests.post("https://care.seewo.com/app/apis.json", data='{"action":"STUDENT_SET_MEDAL_MULTI","params":{"performanceId":"' + performanceId + '","studentsId":"' + studentId + '"}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})  # 用","连接多个studentId
    elif type == "CLASSROOM":
        requests.post("https://care.seewo.com/app/apis.json", data='{"action":"CLASSROOM_SET_MEDAL","params":{"performanceId":"' + performanceId + '","classId":"' + classId + '"}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})


def MEDAL_PERFORMANCE_DELETE(classId, performanceDetailId, performanceType):
    response = requests.post("https://care.seewo.com/app/apis.json", data='{"action":"MEDAL_PERFORMANCE_DELETE","params":{"classId":"' + classId + '","performanceDetailId":"' + performanceDetailId + '","type":' + str(performanceType) + '}}', headers={"Content-Type": "application/json", "x-csrf-token": args.csrfToken}, cookies={"accessToken": args.accessToken, "connect.magick": args.connectMagick})


def analyseReport(report):  # 解析获得的点评数据
    if len(report["detail"]) == 0:
        print("\n当前时间范围没有点评记录哦\n")
        return False
    else:
        for i in range(len(report["detail"])):
            print("{} {} {}% {}{}分".format(report["detail"][i]["name"], "表扬" if report["detail"][i]["type"] == 1 else "待改进", report["detail"][i]["percentages"], "+" if report["detail"][i]["type"] == 1 else "-", report["detail"][i]["score"]))
        return True


def analysePerformance(perfomance):
    for i in range(len(perfomance)):
        print("{}. {}{}分 {}给{}, 因为{}\t{} 由{}老师点评 {}".format(i + 1, "+" if perfomance[i]["type"] == 1 else "-", perfomance[i]["value"], "表扬" if perfomance[i]["type"] == 1 else "批评", perfomance[i]["studentName"], perfomance[i]["name"], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(perfomance[i]["postedAt"] / 1000)), perfomance[i]["teacherName"], perfomance[i]["studentName"]))


def listStudent(students, includeClass=False):
    if includeClass == True:
        print("0.全班\t\t", end='')
        displayedNum = 1
    else:
        displayedNum = 0
    for i in range(len(students)):
        print("{}. {}{}\t".format(i + 1, students[i]["studentName"], "\t" if (len(students[i]["studentName"]) < 3 and i < 10) else ''), end='')
        displayedNum += 1
        if displayedNum == 7:  # 一行显示七人
            print()
            displayedNum = 0
        elif displayedNum != 7 and i == len(students) - 1:
            print()


def classReport(referer="", sNum=0):
    def classPerformance():
        while True:
            print("时间范围：\n\t1. 今天\t2.本周\t3.上周\t4.本月\t5.自定义\n\t0.返回上一级")
            slct = int(input("请输入所要查看的时间范围：") or -1)
            if slct == 1:
                print("---今天---")
                result = analyseReport(CLASSROOM_FETCH_REPORT("1", classrooms[num - 1]["classId"]))  # 今天
                print("----------")
            elif slct == 2:
                print("---本周---")
                result = analyseReport(CLASSROOM_FETCH_REPORT("2", classrooms[num - 1]["classId"]))  # 本周
                print("----------")
            elif slct == 3:
                print("---上周---")
                result = analyseReport(CLASSROOM_FETCH_REPORT("3", classrooms[num - 1]["classId"]))  # 上周
                print("----------")
            elif slct == 4:
                print("---本月---")
                result = analyseReport(CLASSROOM_FETCH_REPORT("4", classrooms[num - 1]["classId"]))  # 本月
                print("----------")
            elif slct == 5:
                startTime = input("请输入起始时间 (Unix Timestamp, Millionsecond): ") or str(int(time.time() * 1000) - 86400000 + 1)
                endTime = input("请输入终止时间 (Unix Timestamp, Millionsecond): ") or str(int(time.time() * 1000))
                print("---自定义时间 ({} - {})---".format(startTime, endTime))
                result = analyseReport(CLASSROOM_FETCH_REPORT("7", classrooms[num - 1]["classId"], '', startTime, endTime))  # 自定义
                print("----------")
            elif slct == 0:
                print("\033c", end='')
                break
            else:
                result = False
                print("无效的时间范围, 请重试! ")
            if result == True:
                temp = slct
                while True:
                    if 0 < temp < 5:
                        performance = CLASSROOM_FETCH_PERFORMANCE(str(temp), classrooms[num - 1]["classId"])
                    elif temp == 5:
                        performance = CLASSROOM_FETCH_PERFORMANCE("7", classrooms[num - 1]["classId"], '', startTime, endTime)
                    print("1. 查看点评记录\n2. 删除点评记录\n3. 清空点评记录\n0. 返回上一级")
                    slct = int(input("请输入功能序号: ") or -1)
                    if 0 < slct < 3:
                        analysePerformance(performance)
                        if slct == 2:
                            slct = int(input("请输入要删除的点评记录: ")) - 1
                            if performance[slct]["from"]["type"] == 0:
                                MEDAL_PERFORMANCE_DELETE(classrooms[num - 1]["classId"], performance[slct]["resourceid"], "3")
                            else:
                                MEDAL_PERFORMANCE_DELETE(classrooms[num - 1]["classId"], performance[slct]["from"]["relativeId"], performance[i]["from"]["type"])
                    elif slct == 3:
                        while True:
                            decision = input("确认清空当前页面的点评记录吗? 本操作将无法撤销! (y/N): ") or 'N'
                            if decision.lower() in ['y', 'n']:
                                break
                        if decision.lower() == 'y':
                            for i in range(len(performance)):
                                if performance[i]["from"]["type"] == 0:
                                    MEDAL_PERFORMANCE_DELETE(classrooms[num - 1]["classId"], performance[i]["resourceid"], "3")
                                else:
                                    MEDAL_PERFORMANCE_DELETE(classrooms[num - 1]["classId"], performance[i]["from"]["relativeId"], performance[i]["from"]["type"])
                            break
                    elif slct == 0:
                        break
                    else:
                        print("输入的功能序号无效, 请重试! ")

    def studentPerformance():
        while True:
            print("时间范围：\n\t1. 今天\t2.本周\t3.上周\t4.本月\t5.自定义\n\t0.返回上一级")
            slct = int(input("请输入所要查看的时间范围：") or -1)
            if slct == 1:
                print("---今天---")
                result = analyseReport(STUDENT_FETCH_REPORT("1", classrooms[num - 1]["classId"], students[sNum]["studentId"]))  # 今天
                print("----------")
            elif slct == 2:
                print("---本周---")
                result = analyseReport(STUDENT_FETCH_REPORT("2", classrooms[num - 1]["classId"], students[sNum]["studentId"]))  # 本周
                print("----------")
            elif slct == 3:
                print("---上周---")
                result = analyseReport(STUDENT_FETCH_REPORT("3", classrooms[num - 1]["classId"], students[sNum]["studentId"]))  # 上周
                print("----------")
            elif slct == 4:
                print("---本月---")
                result = analyseReport(STUDENT_FETCH_REPORT("4", classrooms[num - 1]["classId"], students[sNum]["studentId"]))  # 本月
                print("----------")
            elif slct == 5:
                startTime = input("请输入起始时间 (Unix Timestamp, Millionsecond): ") or str(int(time.time() * 1000) - 86400000 + 1)
                endTime = input("请输入终止时间 (Unix Timestamp, Millionsecond): ") or str(int(time.time() * 1000))
                print("---自定义时间 ({} - {})---".format(startTime, endTime))
                result = analyseReport(STUDENT_FETCH_REPORT("7", classrooms[num - 1]["classId"], students[sNum]["studentId"], '', startTime, endTime))  # 自定义
                print("----------")
            elif slct == 0:
                print("\033c", end='')
                break
            else:
                result = False
                print("无效的时间范围, 请重试! ")
            if result == True:
                temp = slct
                while True:
                    print("1. 查看点评记录\n0. 返回上一级")
                    slct = int(input("请输入功能序号: ") or -1)
                    if slct == 1:
                        if 0 < temp < 5:
                            analysePerformance(STUDENT_FETCH_PERFORMANCE(str(temp), classrooms[num - 1]["classId"], students[sNum]["studentId"]))
                        elif temp == 5:
                            analysePerformance(STUDENT_FETCH_PERFORMANCE("7", classrooms[num - 1]["classId"], students[sNum]["studentId"], '', startTime, endTime))
                    elif slct == 0:
                        break
                    else:
                        print("输入的功能序号无效, 请重试! ")

    if referer == "class":
        print("\033c{} ({})\n\n".format(classrooms[num - 1]["classNickName"], classrooms[num - 1]["invitationCode"]), end='')  # 清屏并显示班级名称
        classPerformance()
    elif referer == "student":
        print("\033c{} ({})\n\n".format(classrooms[num - 1]["classNickName"], classrooms[num - 1]["invitationCode"]), end='')  # 清屏并显示班级名称
        studentPerformance()
    else:
        while True:
            print("\033c{} ({})\n\n".format(classrooms[num - 1]["classNickName"], classrooms[num - 1]["invitationCode"]), end='')  # 清屏并显示班级名称
            print("1. 查看班级表现\n2. 查看个人表现\n0. 返回上一级")
            slct = int(input("请输入功能序号: ") or -1)
            if slct == 1:
                classPerformance()
            elif slct == 2:
                listStudent(students)
                sNum = int(input("请输入学生序号: ") or 1) - 1
                if 0 <= sNum < len(students):
                    studentPerformance()
                else:
                    print("输入的学生序号不存在, 请重试! ")
            elif slct == 0:
                break
            else:
                print("输入的功能序号无效, 请重试! ")


while True:  # 等待输入正确的班级序号
    print("\033c", end='')  # 清屏

    classrooms = CLASSROOM_FETCH()

    for i in range(len(classrooms)):
        print("{}. {} ({}) 班主任: {}".format(i + 1, classrooms[i]["classNickName"], classrooms[i]["invitationCode"], classrooms[i]["masterName"]))
    print("0. 退出程序")
    num = int(input("请输入要查看的班级序号: ") or -1)

    if 0 < num <= len(classrooms):
        students = STUDENT_FETCH_LIST(classrooms[num - 1]["classId"])
        print("\033c", end='')
        while True:
            print("{} ({})\n\n1. 显示所有学生\n2. 显示所有小组\n3. 查看班级报表\n0. 返回上一级".format(classrooms[num - 1]["classNickName"], classrooms[num - 1]["invitationCode"]))
            slct = int(input("请输入功能序号: ") or -1)
            if slct == 1:  # 显示所有学生
                if (len(students) == 0):
                    print("\033c{} ({})\n\n".format(classrooms[num - 1]["classNickName"], classrooms[num - 1]["invitationCode"]), end='')  # 清屏并显示班级名称
                    print("这个班级还没有学生哦\n")
                else:
                    while True:
                        print("\033c{} ({})\n\n".format(classrooms[num - 1]["classNickName"], classrooms[num - 1]["invitationCode"]), end='')  # 清屏并显示班级名称
                        listStudent(students, True)
                        print("\n1. 发送点评\n2. 查看班级/个人表现\n0. 返回上一级")
                        slct = int(input("请输入功能序号: ") or -1)
                        if slct == 1:
                            times = 1
                            while True:
                                sNum = int(input("请输入学生序号 [留空以进入多选模式, 输入-1以返回上一级, 输入-2以修改发送次数 (默认为1次, 当前为{}次)]: ".format(times)) or -114514)
                                if -1 < sNum <= len(students):
                                    medal = MEDAL_FETCH_BY_CLASSROOM(classrooms[num - 1]["classId"])
                                    for i in range(len(medal)):
                                        print("{}. {} {}{}分".format(i + 1, medal[i]["name"], "表扬 +" if medal[i]["type"] == 1 else "待改进 -", medal[i]["value"]))
                                    while True:
                                        slctdMedal = int(input("请选择要发送的点评类型 (输入-1以返回上一级): ") or 0) - 1
                                        if 0 <= slctdMedal < len(medal):
                                            if sNum == 0:
                                                for i in range(times):
                                                    SET_MEDAL("CLASSROOM", medal[slctdMedal]["resourceid"], '', classrooms[num - 1]["classId"])
                                            elif 0 < sNum <= len(students):
                                                for i in range(times):
                                                    SET_MEDAL("STUDENT_SINGLE", medal[slctdMedal]["resourceid"], students[sNum - 1]["studentId"], '')
                                            break
                                        elif slctdMedal == -1 - 1:
                                            break
                                        else:
                                            print("选择的点评类型不存在, 请重试! ")
                                elif sNum == -114514:
                                    sNums = []
                                    while True:
                                        sNum = int(input("请输入第{}个学生序号 (留空以退出多选模式): ".format(len(sNums) + 1)) or -1)
                                        if 0 < sNum <= len(students):
                                            sNums.append(sNum - 1)
                                        elif sNum == -1:
                                            break
                                        else:
                                            print("输入的学生序号不存在, 请重试! ")
                                    if len(sNums) > 0:
                                        studentIds = ''
                                        for i in range(len(sNums)):
                                            studentIds += students[sNums[i]]["studentId"]
                                            if i < len(sNums) - 1:
                                                studentIds += ','
                                        medal = MEDAL_FETCH_BY_CLASSROOM(classrooms[num - 1]["classId"])
                                        for i in range(len(medal)):
                                            print("{}. {} {}{}分".format(i + 1, medal[i]["name"], "表扬 +" if medal[i]["type"] == 1 else "待改进 -", medal[i]["value"]))
                                        slctdMedal = int(input("请选择要发送的点评类型 (输入-1以返回上一级): ") or 0) - 1
                                        if 0 <= slctdMedal < len(medal):
                                            for i in range(times):
                                                SET_MEDAL("STUDENT_MULTI", medal[slctdMedal]["resourceid"], studentIds, '')
                                            break
                                        elif slctdMedal == -1 - 1:
                                            break
                                        else:
                                            print("选择的点评类型不存在, 请重试! ")
                                elif sNum == -1:
                                    break
                                elif sNum == -2:
                                    temp = times
                                    times = int(input("请输入发送次数 (>=1): ") or 1)
                                    if times < 1:
                                        times = temp
                                else:
                                    print("输入的学生序号不存在, 请重试! ")
                                break
                        elif slct == 2:
                            while True:
                                sNum = int(input("请输入学生序号: ") or -1)
                                if sNum == 0:
                                    classReport("class")
                                    break
                                elif 0 < sNum <= len(students):
                                    classReport("student", sNum - 1)
                                    break
                                else:
                                    print("输入的学生序号不存在, 请重试! ")
                        elif slct == 0:
                            print("\033c", end='')
                            break
                        else:
                            print("输入的功能序号无效, 请重试! ")
            elif slct == 2:  # 显示所有小组
                print("\033c{} ({})\n\n".format(classrooms[num - 1]["classNickName"], classrooms[num - 1]["invitationCode"]), end='')  # 清屏并显示班级名称
                groups = GROUP_COLLECTION_GET_LIST(classrooms[num - 1]["classId"])
                if len(groups) == 0:  # 对是否存在小组进行判断
                    print("这个班级还没有小组哦\n")
                else:
                    for i in range(len(groups)):
                        print("{}. {}".format(i + 1, groups[i]["planName"]))
            elif slct == 3:  # 查看班级报表
                classReport()
                print("\033c", end='')
            elif slct == 0:
                break
            else:
                print("\033c输入的功能序号无效, 请重试! ")
    elif num == 0:
        exit()
    else:
        print("序号不正确, 请重试! ")
