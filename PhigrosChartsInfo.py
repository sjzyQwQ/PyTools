import os
import json

p = input('请输入Json谱面文件（夹）的路径：')
if os.path.isfile(p):
    f = open(p, 'r')
    j = json.loads(f.read())
    f.close()
    notes = 0
    time = 0
    for i in j['judgeLineList']:
        notes += len(i['notesAbove']) + len(i['notesBelow'])
    print('BPM: {0}\t物量：{1}'.format(j['judgeLineList'][0]['bpm'], notes))
elif os.path.isdir(p):
    os.chdir(p)
    for i in os.listdir():
        f = open(i, 'r')
        j = json.loads(f.read())
        f.close()
        notes = 0
        for l in j['judgeLineList']:
            notes += len(l['notesAbove']) + len(l['notesBelow'])
        print('谱面：{0}\tBPM: {1}\t物量：{2}'.format(i, j['judgeLineList'][0]['bpm'], notes))
else:
    print('输入的路径好像不对……？检查一下重试吧！')
