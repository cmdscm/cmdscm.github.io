#导入
import time
#定义字母
letter_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,
        'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,
        'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,
        't':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
#定义数字
number_dict = {}
i = 0
for j in letter_dict:
    number_dict[letter_dict[j]] = j
#定义函数
def jiami(text):
    over_text = ""
    l = 0
    print()
    print("加密中")
    time.sleep(0.5)
    for i in text:
        if i in letter_dict:
            if l == len(text) - 1:     
                over_text = over_text + str(letter_dict[i]) 
            else:
                over_text = over_text + str(letter_dict[i]) + "-"
        l += 1
    print()
    print("加密完成，结果是:")
    print()
    print(over_text)
    print()
    over_text = ""
def jiemi(text):
    over_text = ""
    l = "" #记录字母
    print()
    print("解密中")
    time.sleep(0.5)
    for i in text:
        if i in number_dict:
            if l == "":
                l = i
            elif l != "":
                l = l + i
        elif i == "-":
            if l != "":
                over_text = over_text + str(number_dict[l])
                l = ""
    print()
    print("解密完成，结果是:")
    print()
    print(over_text)
    print()
    over_text = ""
#开始
print()
print("欢迎使用A0-Z25加密解密")
print()
print("输入'加密' / '1' 或 '解密' / '2' 以操作")
print()
#程序
while True:
    answer = input(">>")
    if answer == "加密" or answer == "1":
        text = input("请输入要加密的内容:")
        jiami(text)
        print("输入'加密' / '1' 或 '解密' / '2' 以操作")
    elif answer == "解密" or answer == "2":
        text = input("请输入要解密的内容")
        jiemi(text)
        print("输入'加密' / '1' 或 '解密' / '2' 以操作")
    else:
        print("输入'加密' / '1' 或 '解密' / '2' 以操作")        
    print()