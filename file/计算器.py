import pygame
import sys
from tkinter import messagebox
pygame.init()
BTN_W,BTN_H = 70,50
WIN_W,WIN_H = BTN_W*5,BTN_H*7
window = pygame.display.set_mode((WIN_W,WIN_H))
pygame.display.set_caption('计算器')
window.fill('#222222')
pygame.display.flip()
fontsize = 30
displaysize = fontsize / 2
memory_list = []# 记忆数字(用于M+M-MRMCC)
canround = True# 允许四舍五入
input_text = []# 输入列表
result_list = []# 结果列表
otherSymbols = ['(',')']# 其他符号(判断用)
operator = ['+','-','x','÷']# 运算符
numbers = ['1','2','3','4','5','6','7','8','9','0']
btntext = (('MR','+','-','x','÷'),
            ('M+',1,2,3,'±'),
            ('M-',4,5,6,'←'),
            ('MC',7,8,9,'='),
            ('C','%',0,'.'))
def draw_init():
    global btntext,btnfont
    try:
        btnfont = pygame.font.Font('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\unifont-12.1.04.ttf',30)
    except:
        sysfont = pygame.font.get_fonts()[0]
        btnfont = pygame.font.SysFont(sysfont,30)
    window.fill('#222222');pygame.draw.rect(window,'white',(1,1,WIN_W-2,BTN_H*2-5),0,10)
    for c,cindex in enumerate(btntext):
        for r,rindex in enumerate(cindex):
            xpos,ypos = r*BTN_W,BTN_H*2+c*BTN_H
            if rindex == '=':btnw,btnh = BTN_W,BTN_H*2
            else:btnw,btnh = BTN_W,BTN_H
            btnw -= 2;btnh -= 2;pygame.draw.rect(window,'lightgray',(xpos+1,ypos-1,btnw,btnh),0,5)
            btntext = btnfont.render(str(rindex),True,'black')
            btntextx,btntexty = btntext.get_size()
            xpos = xpos+btnw/2-btntextx/2;ypos = ypos+btnh/2-btntexty/2
            window.blit(btntext,(xpos,ypos))
def changenumber(inputlist:list,delete=False):
    if inputlist == []:
        return
    for i in range(len(inputlist)):
        ttl = len(inputlist)-1
        num = ttl-i
        letter = inputlist[num]
        if letter in operator and i != 0 and i != ttl:
            beforenum = inputlist[num+1]
            afternum = inputlist[num-1]
            if delete:
                if afternum in operator and letter == '-':
                    inputlist.pop(num)
                    return inputlist
            elif beforenum in numbers or beforenum == '%':
                if afternum in numbers or afternum == '%':
                    inputlist.insert(num+1,'-')
                    return inputlist
        elif i == ttl and letter != '-':
            inputlist.insert(0,'-')
            return inputlist
        elif i == ttl and letter == '-':
            return changenumber(inputlist,True)
    return inputlist
def countnumber(inputlist:list,repeat=0):
    num = 0
    for i in operator:
        if i not in inputlist:
            num += 1
    if num >= 4:
        return inputlist
    # print('countnumber %d'%repeat)
    returnlist = []
    firststr = ''
    secondstr = ''
    operators = ''
    ispercent = False# 不是百分数
    isfirst = True# 是第一个算式
    isminus = False# 不是负数
    num = 0
    try:
        for i in inputlist:
            if i in operator and num != 0 and isfirst:
                operators = i
                isfirst = False
            elif isfirst:
                firststr = firststr + i
            elif i in operator and inputlist[num-1] in operator:
                if isfirst:
                    firststr = firststr + '-'
                else:
                    secondstr = secondstr + '-'
            elif i in operator and num != 0 and not isfirst:
                if operators == '+':
                    firststr = float(firststr) + float(secondstr)
                elif operators == '-':
                    firststr = float(firststr) - float(secondstr)
                elif operators == 'x':
                    firststr = float(firststr) * float(secondstr)
                elif operators == '÷':
                    firststr = float(firststr) / float(secondstr)
                strlist = str(firststr).split('.')
                if len(strlist) != 1 and strlist[len(strlist)-1] == '0':
                    firststr = str(firststr)[:len(str(firststr))-2]
                countlist = []
                for i in firststr:countlist.append(i)
                for i in inputlist[num:]:countlist.append(i)
                return countnumber(countlist,repeat+1)
            else:
                secondstr = secondstr + i
                isminus = False
            num += 1
        if firststr[len(firststr)-1] == '%':
            ispercent = True
            firststr = firststr[:len(firststr)-1]
        if len(firststr.split('.')) == 1:
            firststr = int(firststr)
        else:
            firststr = float(firststr)
        if ispercent:
            firststr = firststr / 100
            ispercent = False
        if secondstr[len(secondstr)-1] == '%':
            ispercent = True
            secondstr = secondstr[:len(secondstr)-1]
        if len(secondstr.split('.')) == 1:
            secondstr = int(secondstr)
        else:
            secondstr = float(secondstr)
        if ispercent:
            secondstr = secondstr / 100
            ispercent = False
        if operators == '+':
            returnnum = str(firststr + secondstr)
        elif operators == '-':
            returnnum = str(firststr - secondstr)
        elif operators == 'x':
            returnnum = str(firststr * secondstr)
        elif operators == '÷':
            returnnum = str(firststr / secondstr)
        lennum = len(returnnum.split('.'))
        if lennum != 1:
            if returnnum.split('.')[lennum-1] == '0':
                returnnum = returnnum[:len(returnnum)-2]
            elif len(returnnum.split('.')[lennum-1]) > 4 and canround:
                returnnum = round(returnnum)
        for i in returnnum:
            returnlist.append(i)
    except:
        messagebox.showerror(messagebox='countnumber错误!'
        ,title='错误')
    return returnlist
def add_input(text):
    textlen = len(input_text)
    if text == '%':
        if input_text==[] or input_text[textlen-1] in operator or input_text[textlen-1]=='.':
            return
        for i in range(textlen):
            if input_text[textlen-i-1] == '%':
                return
            elif input_text[textlen-i-1] in operator:
                input_text.append('%')
            else:
                input_text.append('%')
            return
    if text in numbers:
        if input_text==[] or input_text[textlen-1]!='%':
            input_text.append(text)
    elif text in operator and input_text!= []:
        if input_text[len(input_text)-1] not in operator:
            input_text.append(text)
    elif input_text != [] and text == '.' and input_text[len(input_text)-1] in numbers:
        input_text.append(text)
def clickbtn(rectx):
    global Candraw,input_text,memory_list
    if input_text!=[]and input_text[0]=='0':input_text=input_text[1:]
    if rectx >= BTN_W*4 and mousey >= WIN_H-BTN_H*2:
        pygame.draw.rect(window,'lightblue',(rectx+1,WIN_H-BTN_H*2-1,BTN_W-2,BTN_H*2-2),0,5)
        pygame.draw.rect(window,'blue',(rectx+1,WIN_H-BTN_H*2-1,BTN_W-2,BTN_H*2-2),2,5)
        clicktext = btnfont.render('=',True,'blue')
        textw,texth = clicktext.get_size()
        textx = rectx + (BTN_W-2)/2 - textw/2
        texty = (WIN_H-BTN_H*2-1) + (BTN_H*2-2)/2 - texth/2
        window.blit(clicktext,(textx,texty))
        Candraw = True
        pygame.display.update()
        if input_text==[]or input_text[len(input_text)-1] in operator or input_text[len(input_text)-1] == '.':
            return
        try:
            if result_list != []:
                input_text = result_list
            else:
                input_text = countnumber(input_text)
        except:
            messagebox.showerror(message='错误原因:countnumber(input_text)',title='错误')
            input_text.clear()
        return
    elif rectx >= BTN_W*4 and WIN_H-BTN_H*3 > mousey >= WIN_H-BTN_H*4:
        input_text = changenumber(input_text)
    elif rectx >= BTN_W*4 and mousey >= WIN_H-BTN_H*3 and input_text != []:
        input_text.pop()
    for i in range(1,6):
        if mousey >= WIN_H - BTN_H * i:
            addtext = str(btntext[5-i][int(rectx/BTN_W)])
            if input_text!=[]and input_text[len(input_text)-1]== ')' and addtext in numbers:
                return
            if rectx != 0 or addtext == '.' or addtext == '%':
                add_input(addtext)
            elif rectx == 0:
                if addtext == 'C':
                    input_text.clear()
                    input_text.append('0')
                    memory_list.clear()
                elif addtext=='MC':
                    memory_list.clear()
                elif addtext == 'MR':
                    input_text.clear()
                    if memory_list == []:
                        input_text.append('0')
                    else:
                        for k in memory_list:
                            input_text.append(k)
                elif addtext == 'M+':
                    lt = countnumber(input_text)
                    if memory_list == [] and lt != []:
                        memory_list = lt
                    elif lt != []:
                        memory_list.append('+')
                        memory_list = memory_list + lt
                        memory_list = countnumber(memory_list)
                elif addtext == 'M-':
                    lt = countnumber(input_text)
                    if memory_list == [] and lt != []:
                        memory_list.append('0','-')
                    elif lt != []:
                        memory_list.append('-')
                    memory_list = memory_list + lt
                    memory_list = countnumber(memory_list)
            try:
                drawx = rectx+1
                drawy = WIN_H-BTN_H*i-1
                pygame.draw.rect(window,'lightblue',(drawx,drawy,BTN_W-2,BTN_H-2),0,5)
                pygame.draw.rect(window,'blue',(drawx,drawy,BTN_W-2,BTN_H-2),2,5)
                clicktext = btnfont.render(addtext,True,'blue')
                textw,texth = clicktext.get_size()
                textx = rectx + (BTN_W-2)/2 - textw/2
                texty = (WIN_H-BTN_H*i-1) + (BTN_H-2)/2 - texth/2
                window.blit(clicktext,(textx,texty))
                Candraw = True
                pygame.display.update()
            except:
                messagebox.showerror('错误','响应鼠标时出现错误')
            return
def showinput(inputlist):
    global displaysize,fontsize
    textlen = len(inputlist)
    if textlen > int(WIN_H/displaysize) and displaysize > 10:
        fontsize -= 10
        displaysize -= 5
    elif displaysize < 15 and textlen <= 23:
        fontsize = 30
        displaysize = 15
    shownumber(inputlist,10,fontsize,displaysize,istag='t')
    try:
        if inputlist[textlen-1] not in operator:
            for i in inputlist:
                if i in operator:
                    showresult(inputlist)
                    return
    except:
        return
    return
def shownumber(num_list,show_h,fontsize,font_w,color='black',istag='f'):
    isnum = False
    usecolor = color
    try:
        font = pygame.font.Font('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\unifont-12.1.04.ttf',30)
    except:
        sysfont = pygame.font.get_fonts()[0]
        font = pygame.font.SysFont(sysfont,30)
    num = 0
    for i in num_list:
        if istag == 't':
            if not isnum:
                usecolor = 'black'
            if i in numbers:
                isnum = True
                usecolor = 'black'
            elif i in operator and isnum:
                isnum = False
                usecolor = 'red'
        text = font.render(i,True,usecolor)
        window.blit(text,(WIN_W-(len(num_list)-num)*font_w,show_h))
        num += 1
def showresult(numlist):
    global displaysize,fontsize
    returnlist = countnumber(numlist)
    shownumber(returnlist,BTN_H+10,fontsize,displaysize,'blue')
Candraw = False
isclose = False
draw_init()
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            pygame.key.set_repeat(1000,20)
            try:
                if chr(event.key) in operator or chr(event.key) in numbers or chr(event.key) in otherSymbols:
                    if input_text[len(input_text)-1] == ')':
                        continue
            except:
                pass
            if event.key == pygame.K_1:
                input_text.append('1')
            elif event.key == pygame.K_2:
                input_text.append('2')
            elif event.key == pygame.K_3:
                input_text.append('3')
            elif event.key == pygame.K_4:
                input_text.append('4')
            elif event.key == pygame.K_5:
                input_text.append('5')
            elif event.key == pygame.K_6:
                input_text.append('6')
            elif event.key == pygame.K_7:
                input_text.append('7')
            elif event.key == pygame.K_8:
                input_text.append('8')
            elif event.key == pygame.K_9:
                input_text.append('9')
            elif event.key == pygame.K_0:
                input_text.append('0')
            elif event.key == pygame.K_PERCENT and input_text != []:
                input_text.append('%')
            elif event.key == pygame.K_PERIOD and input_text != []:
                input_text.append('.')
            elif event.key == pygame.K_MINUS and input_text != []:
                input_text.append('-')
            elif event.key == pygame.K_EQUALS:
                if result_list != []:
                    input_text = result_list
                else:
                    input_text=countnumber(input_text)
            elif event.key == pygame.K_BACKSPACE and input_text != []:
                input_text.pop()
            pygame.draw.rect(window,'white',(1,1,WIN_W-2,BTN_H*2-5),0,10)
            displaynumber = round((WIN_W-2)/displaysize)
            if input_text!=[]and input_text[0]=='0':input_text=input_text[1:]
            showinput(input_text)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousex,mousey = event.pos
            btntext = (('MR','+','-','x','÷'),
            ('M+',1,2,3,'±'),
            ('M-',4,5,6,'←'),
            ('MC',7,8,9,'='),
            ('C','%',0,'.'))
            if mousey >= BTN_H*2:
                if mousex <= BTN_W:
                    clickbtn(0)
                elif mousex <= BTN_W*2:
                    clickbtn(BTN_W)
                elif mousex <= BTN_W*3:
                    clickbtn(BTN_W*2)
                elif mousex <= BTN_W*4:
                    clickbtn(BTN_W*3)
                elif mousex <= BTN_W*5:
                    clickbtn(BTN_W*4)
            pygame.display.update()
        elif Candraw and event.type == pygame.MOUSEBUTTONUP:
            Candraw = False
            draw_init()
            showinput(input_text)
        elif not isclose:
            pygame.display.update()
# ---