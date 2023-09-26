import time
letter_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,
        'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,
        'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,
        't':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
#定义数字
number_dict = {}
i = 0
for j in letter_dict:
    number_dict[letter_dict[j]] = j
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
        print( i + "," +l + "," + over_text)
    print()
    print("解密完成，结果是:")
    print()
    print(over_text)
    print()
    over_text = ""
jiemi("0-3-4")