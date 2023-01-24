'''
Minecraft Modpack Creator
This Python file is edited by Misaka10072
Last modified: 2023/1/25
GitHub: https://github.com/sjzyQwQ/PyTools
'''

import os
import json
import zipfile

manifest={}

manifest["manifestType"]="MinecraftModpack" # 不要修改
manifest["manifestVersion"]=1 # 不要修改

manifest["name"]="demopy" # 整合包名称
manifest["version"]="version" # 整合包版本
manifest["author"]="Misaka10072" # 整合包作者

manifest["overrides"]="overrides" # 可以修改成自己喜欢的名字

manifest["minecraft"]={}
manifest["minecraft"]["version"]="1.19.3" # 游戏版本
manifest["minecraft"]["modLoaders"]=[]

manifest["minecraft"]["modLoaders"].append({})
manifest["minecraft"]["modLoaders"][0]["id"]="fabric-0.14.3" # 加载器名称-加载器版本
manifest["minecraft"]["modLoaders"][0]["primary"]=True

manifest["files"]=[]

# 以下可选（添加后可以从CurseForge下载Mod，减小整合包占用空间，不需要请将其注释）
manifest["files"].append({})
manifest["files"][0]["projectID"]=0
manifest["files"][0]["fileID"]=0
manifest["files"][0]["required"]=True

if os.path.exists("{0}".format(manifest["name"]))==False:
    os.mkdir("{0}".format(manifest["name"]))
if os.path.exists("{0}/{1}".format(manifest["name"],manifest["overrides"]))==False:
    os.mkdir("{0}/{1}".format(manifest["name"],manifest["overrides"]))

f=open("{0}/manifest.json".format(manifest["name"]),"w")
f.write(json.dumps(manifest))
f.close()

print("请在{0}/{1}/{2}放入您需要添加在整合包内的内容，目录结构见项目README.md\n添加好后按回车键开始制作整合包……".format(os.getcwd(),manifest["name"],manifest["overrides"]))
input()

modPack=zipfile.ZipFile("{0}.zip".format(manifest["name"]),"w")
os.chdir("{0}".format(manifest["name"]))
for root,dir,file in os.walk("."):
    if len(file)>0:
        for i in file:
            modPack.write("{0}/{1}".format(root,i))
    else:
        modPack.write("{0}".format(root))
modPack.close()
os.chdir("..")

print("整合包制作完成！文件路径：{0}/{1}.zip".format(os.getcwd(),manifest["name"]))