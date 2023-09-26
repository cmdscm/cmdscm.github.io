import time
xuanze=0
cgtg = 0
def living(ktdj):
    if xuanze == ktdj:
        if "blue" in wpl and "green" not in wpl:
            print("---------------------------------")
            print('''你来到了客厅，发现那把蓝色的钥匙刚好能打开客厅的箱子。
            你打开后，只见里面有一把绿色的钥匙。''')
            print("---------------------------------")
            wpl.append("green")
            xzd.clear
            xzd.append("客厅")
        if "blue" not in wpl:
            print("---------------------------------")
            print('''你选择 在客厅寻找线索 。
            你在客厅中找到了一把红色的钥匙和一个箱子,箱子上面写着 blue''')
            print("---------------------------------")
            wpl.append("red")
        xzd.clear()
        xzd.append("客厅")
def chufang(cfdj):
    if xuanze == cfdj:
        if "red" not in wpl:
            print("---------------------------------")
            print('''你选择 前往餐厅 。
            你在餐厅找到了一个箱子，上面写着 red''')         
            print("---------------------------------")
        else:
            print("---------------------------------")
            print('''你来到了餐厅，你发现那把红色的钥匙刚好能打开餐厅的箱子
            你打开后，发现里面有一把蓝色的钥匙''')
            print("---------------------------------")
            wpl.append("blue")
        xzd.clear()
        xzd.append("餐厅")
def study(sfdj):
    if xuanze == sfdj:
        if "green" not in wpl:
            print("---------------------------------")
            print('''你选择 前往书房 。
            你在书房找到了一个箱子，上面写着 green''')
            print("---------------------------------")
        else:
            print("---------------------------------")
            print('''你来到了书房，你发现那把绿色的钥匙刚好能打开书房的箱子
            你打开后，发现里面有一把钥匙，旁边有一张纸条，上面写着：这就是打开门的钥匙''')
            print("---------------------------------")
            wpl.append("finish")
        xzd.clear()
        xzd.append("书房")
def door(mdj):
    if xuanze == mdj:
        if "finish" not in wpl:
            print("---------------------------------")
            print('''你选择 前去查看门
            只见门上的锁孔旁边写着一行字
            一个密室的本质就是一环套一环，每个线索都息息相关。''')
            print("---------------------------------")
        else:
            print("---------------------------------")
            print('''你来到门前，欣喜若狂的把钥匙插入锁孔，随着“咔哒"一声响,你逃了出去''')
            print("---------------------------------")
            cgtg = 1
        xzd.clear()
        xzd.append("门")
xzd=[]
xzd.clear()
print ("-------------------------------")
print("")
print("密室逃脱文字版1.0")
print("")
print ("-------------------------------")
print("")
input("按下任意键开始游戏")
print("")
a=input("请先输入你的名字:")
print("")
print("--------------------------------")
ci=5
while ci > 0 :
    print(ci)
    ci -= 1
    time.sleep(1)
print("-----------------------------")
print("----      游戏开始      -----")
print("-----------------------------")
print("你叫",a)
time.sleep(1)
print('''你一觉醒来,发现自己来到了一个陌生的房子里面，你现在位于这座房子的客厅，旁边分别是
厨房、书房以及被锁上的门。''')
time.sleep(0.5)
wpl=[]
xzd=["客厅"]
cgtg= 0
while cgtg==0:
    if "客厅" in xzd:
        print('''你现在有4个选择:
        1.在客厅寻找线索
        2.前往餐厅
        3.前往书房
        4.前去查看门''')
        xuanze = int(input("请做出你的选择（输入序号即可）："))
        living(1)
        chufang(2)
        study(3)
        door(4)
    if "餐厅" in xzd:
        print('''你现在有3个选择:
        1.前往客厅
        2.在餐厅寻找线索
        3.前往书房''')
        xuanze = int(input("请做出你的选择（输入序号即可）："))
        living(1)
        chufang(2)
        study(3)
    if "书房" in xzd:
        print('''你现在有3个选择:
        1.前往客厅
        2.前往餐厅
        3.在书房寻找线索''')
        xuanze = int(input("请做出你的选择（输入序号即可）："))
        living(1)
        chufang(2)
        study(3)
    if "门" in xzd:
        if "finish" in wpl:
            xuanze=1
            break
        else:
            print('''你现在有2个选择:
            1.前往客厅
            2.在门处寻找线索''')
            xuanze = int(input("请做出你的选择（输入序号即可）："))
            living(1)
            door(2)
time.sleep(1)
print("---------------------------------")
print("")
print("恭喜通关")
print("") 
print("---------------------------------")
input("按下任意键退出")