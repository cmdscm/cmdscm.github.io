import os
import time
import re
def fengefu(number):
    for i in range(number):
        print("--------------------------")
        time.sleep(.5)

fengefu(1)
print("    W  E  L  C  O  M  E")
fengefu(1)
print("欢迎使用 系统辅助 软件")
time.sleep(.5)
print("请问需要做什么?")
time.sleep(.5)
print("[不会使用? 可以输入 '?' 获得使用提示。]")
fengefu(2)

while True:
    caozuo = input(">>>")
    time.sleep(1)
    
    if "?" in caozuo:
        print("使用提示：")
        print('''       指令: open(<路径>)    # 作用：按照指定路径打开对应的文件，如果文件不存在则新建一个文件并打开''')
        print('''       指令: close()        # 作用：关闭当前打开的文件''')
        print('''       指令: time(<参数>)   # 作用：在指定的时间间隔后执行下一步操作，参数可以是 .n\.t\.m\.s''')
    
    if "open(" in caozuo:
        dakai = re(r"o.*?((?P<lujing>))")
        for item in dakai:
            print(item)
        # file = open(lujing, "r")
        # 在这里可以使用文件对象进行相关操作

