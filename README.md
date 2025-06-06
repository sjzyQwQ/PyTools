# PyTools

一些用Python写的小工具

1. [Minecraft Modpack Creator](MinecraftModpackCreator.py)

   ——我的世界整合包生成器

   > 修改必要参数，并根据提示将您需要的文件添加到整合包中
   >
   > **`overrides`文件夹（名称以自己设置的为准）中的目录结构需要与`.minecraft`文件夹一致**
   >
   > 如：
   > ```
   > .minecraft
   > ├─ config
   > │  └─ demo
   > ├─ mods (在manifest.json中已添加的Mod无需放入)
   > │  ├─ Fabric-API.jar
   > │  └─ Mod_Menu.jar
   > └─ options.txt
   > ```

2. [Phigros Charts Info](PhigrosChartsInfo.py)

   ——Phigros铺面信息查看器

   > 输入Json铺面文件或文件夹的路径后，自动输出铺面的BPM和物量

3. [GB 11643](GB%2011643.py)

   ——公民身份号码生成器

   > 根据提示输入符合`GB/T 2260`规范的6位数字地址码
   >
   > 即可随机生成对应地区的`MOD 11-2`检验有效的身份证号
   >
   > **（本程序仅供学习使用）**

4. [EasiCare CLI](EasiCare%20CLI.py)

   ——班级优化大师 CLI

   > 班级优化大师的CLI版本
   >
   > 暂时不支持使用密码登录
   >
   > 填入指定参数即可使用
   >
   > - 较官方GUI版/网页版增加内容:
   >   - 修改点评发送次数
   >   - 清空指定页面的点评记录
   >   - 自动获取经验
   >   - 自动签到 (希沃白板)

5. [ClassIsland to ZongziTek 黑板贴](ci2bbs.py)

   > 可以将[ClassIsland](https://github.com/ClassIsland/ClassIsland)档案转换为[ZongziTek 黑板贴](https://github.com/STBBRD/ZongziTEK-Blackboard-Sticker)课程表

6. [希沃白板云端课件导出器](CloudEnbxExtractor.py)

   > 便捷地获取老师们下载过的课件

7. [CNR广播直播M3U8抓取器](CNR.py)

   > 自动抓取[广播直播·央广网](https://www.cnr.cn/gbzb/)提供的所有M3U8文件

8. 暂时没有

   > 目前只有七个工具哦