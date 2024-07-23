import pygame
import random
from tkinter import *
from tkinter import messagebox
import sys
import re
import os
import time

'''
扫雷2.0
在1.0基础上增加部分设置\动画
新增计时器功能
缺点:无法自定义主题颜色,不能保持窗口置顶
'''
btn_commands = []
def creaftBTN(surface,rect:tuple,width:int,bgcolor,fontcolor,text,command,bdradius):
    global btn_commands,window
    btn_commands.append([rect,command])
    pygame.draw.rect(surface,bgcolor,rect,width,border_radius=bdradius)
    try:
        font = pygame.font.Font('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\unifont-12.1.04.ttf',13)
    except:
        font = pygame.font.SysFont(pygame.font.get_fonts()[0],13)
    blit_text = font.render(text,True,fontcolor)
    fx,fy = blit_text.get_size()
    window.blit(blit_text,(rect[0]+rect[2]/2-fx/2,rect[1]+rect[3]/2-fy/2))

def str_to_list(string,num=0):# 将读取数据转换为列表
    t = re.finditer(r'[\[](?P<value>.*)[\]]',string)
    t_list = []
    for i in t:
        t_list.append(i.group())
    t_list = t_list[num]
    if t_list[1] == '(':
        t_list = t_list[2:len(t_list)-1].split('), (')
        t_list[len(t_list)-1] = t_list[len(t_list)-1][:len(t_list[len(t_list)-1])-1]
        type_now = '('
    else:
        t_list = str(t_list[2:len(t_list[1])-2]).split('], ')
        type_now = '['
    if t_list == ['']:
        return []
    return_list = []
    for i in range(len(t_list)):
        if type_now == '(':
            dd = t_list[i].split(', ')
            return_list.append((int(dd[0]),int(dd[1])))
            continue
        elif i == 0:
            dd = t_list[i].split(', ') 
        else:
            dd = t_list[i][1:].split(', ')
        for j in range(len(dd)):
            if dd[j][0] == 'F':
                dd[j] = False
            else:
                dd[j] = True
        return_list.append(dd)
    return return_list

def read_data(file,text,tlist):
    global mine_num,X_NUM,Y_NUM,game_grade,style_num,open_place,mine_place,tag_mine
    if text == '' or len(tlist) < 3:
        file.seek(0)
        file.truncate()# 清空文件
        file.write('game_grade = 1\nstyle = 1\nmine_num = 10\nX_NUM = 09\nY_NUM = 09')
        mine_num = 10# 地雷数
        X_NUM,Y_NUM = 9,9# 横轴格数 纵轴格数
        game_grade = 1# 游戏难度
        style_num = 1# 当前主题
        return
    try:
        mine_num = int(tlist[0])# 地雷数
        X_NUM = int(tlist[1])# 横轴格数
        Y_NUM = int(tlist[2])# 纵轴格数
        game_grade = int(text[13:14])# 游戏难度
        style_num = int(text[23:24])# 游戏主题
    except:
        return read_data(file,'',tlist)
    _obj = re.compile(r'[\[](?P<value>.*)[\]]')
    # 1.正则匹配串前加了r就是为了使得里面的特殊符号不用写反斜杠了。
    # 2.[ ]具有去特殊符号的作用,也就是说[ [ ]和[ ] ]里的[]只是平凡的中括号
    t = _obj.finditer(text)
    t_list = []
    for i in t:
        t_list.append(i.group())
    if t_list == []:
        return
    a = messagebox.askyesno('提示','是否继续上次保存的游戏?')
    if not a:
        return
    try:
        open_place = str_to_list(t_list[0])
        mine_place = str_to_list(t_list[1])
        tag_mine = str_to_list(t_list[2])
    except:
        messagebox.showerror('错误','在加载过程中出现问题')
        return read_data(file,'',tlist)
    return

def game_init(isset=False):# 游戏初始化
    global mine_num,mine_place,showfont,titlefont,allcolor,tag_mine,gameend,BTN_S,WIN_H,WIN_W,window,tags,open_place,after_click,X_NUM,Y_NUM,margin_top,margin_left,margin_bottom,is_setup,game_grade,difficulty,styles,style_num,COUNT,counts,isAnimation
    difficulty = ['简单','正常','困难','自定义']# 游戏难度
    # 主题样式(主题名,背景颜色,雷未开颜色,雷已开颜色,字体颜色,字体颜色2)
    styles = [
        ('默认','lightgray','blue','lightblue','blue','darkblue'),
        ('碧绿','#44EE44','darkgreen','#11FF11','darkgreen','#557755'),
        ('炫紫','#FF00FF','#AA00AA','#DD77DD','#990099','#880088'),
        ('黑白','white','black','white','black','black'),
        ('浅褐','brown','#AA4400','#997700','#FF9900','#EEAA00'),
        ('混合','orange','darkgreen','#DD77DD','blue','red'),
        ]
    if not isset:
        obj = re.compile(r'\d(?P<value>.*)\d')
        tlist = []
        with open('E:/vscode5月27日下载/文件/python/pygame-file/扫雷/FindMine.txt',mode='r+') as file:
            text = file.read()
            t = obj.finditer(text)
            for i in t:
                tlist.append(i.group())
            read_data(file,text,tlist) 
        try:
            tags = len(tag_mine)# 已经标记的雷数  
        except:     
            mine_place = []# 地雷位置
            open_place = []# 已经打开的位置
            tag_mine = []# 已经标记的位置
            tags = len(tag_mine)
    else:
        tags = 0# 已经标记的雷数        
        mine_place = []# 地雷位置
        open_place = []# 已经打开的位置
        tag_mine = []# 已经标记的位置
    isAnimation = False
    counts = 0# 当前时间
    COUNT = pygame.USEREVENT + 1# 自定义计时事件
    allcolor = [styles[style_num-1][3],'orangered','darkblue','blue','brown','pink','blue','red','black']# 显示数字颜色
    gameend = False# 游戏是否结束
    BTN_S = 20# 按钮尺寸
    WIN_W,WIN_H = BTN_S*(X_NUM+4),BTN_S*(Y_NUM+7)# 窗口尺寸
    margin_top = 3# 上外边距
    margin_left = 2# 左外边距
    margin_bottom = WIN_H-BTN_S*(Y_NUM+margin_top)# 下外边距
    is_setup = False# 是否打开设置窗口
    after_click = []# 之后点击的雷位置
    pygame.init()
    try:
        showfont = pygame.font.Font('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\unifont-12.1.04.ttf',15)
        titlefont = pygame.font.Font('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\unifont-12.1.04.ttf',40)
    except:
        showfont = pygame.font.SysFont(pygame.font.get_fonts()[0],15)
        titlefont = pygame.font.SysFont(pygame.font.get_fonts()[0],40)
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    window = pygame.display.set_mode((WIN_W,WIN_H))
    window.fill(styles[style_num-1][1])
    pygame.display.set_caption('扫雷')
    pygame.display.flip()

def make_mine(xnum,ynum):# 生成地雷
    n = 0
    minelist = []
    for i in range(ynum):
        minelist.append([])
        for j in range(xnum):
            minelist[i].append(False)
    while n<mine_num and n < xnum*ynum-1:
        a,b = random.randint(0,ynum-1),random.randint(0,xnum-1)
        if minelist[a][b] != True:
            minelist[a][b] = True
            n += 1
    return minelist

def draw_init(isset=False):# 渲染游戏画面
    global mine_place,mine_title
    if isset:
        game_init(isset)
        pygame.time.set_timer(COUNT,0)
    else:
        game_init()
    if mine_place == []:
        mine_place = make_mine(X_NUM,Y_NUM)
    pygame.draw.rect(window,'gray',(BTN_S*margin_left,BTN_S*margin_top,BTN_S*X_NUM,BTN_S*Y_NUM))
    for c,cindex in enumerate(mine_place):# 序号 内容
        for r,rindex in enumerate(cindex):
            xpos,ypos = (r+margin_left)*BTN_S,(c+margin_top)*BTN_S
            btns = BTN_S 
            pygame.draw.rect(window,styles[style_num-1][2],(xpos,ypos,btns-1,btns-1),0,2)
    settip = showfont.render('当前用时: 无    当前标记: 无',True,styles[style_num-1][5])
    window.blit(settip,(WIN_W/2-settip.get_size()[0]/2,BTN_S*1.5))
    tip1 = showfont.render('ESC|游戏设置    F1|游戏说明',True,styles[style_num-1][4])
    window.blit(tip1,(WIN_W/2-tip1.get_size()[0]/2,WIN_H-BTN_S*1.5))
    creaftBTN(window,(WIN_W/2-btns*2,WIN_H-btns*3,btns*4,btns),1,'black','black','重新开始','draw_init(True)',2)
    pygame.display.update()
    if open_place != []:
        for i in open_place:
            clickbtn(i[0],i[1],justthis=True)
    if tag_mine != []:
        for j in tag_mine:
            clickbtn(j[0],j[1],'R',justthis=True)

def findMineNum(xbtn,ybtn,doAddMine=False):# 返回周围雷数
    global after_click,open_place
    mineNumber = 0
    for y in range(-1,2):
        for x in range(-1,2):
            if x == 0 and y == 0:
                continue
            if -1 < xbtn+x < X_NUM and -1 < ybtn+y < Y_NUM:           
                if doAddMine:
                    if (xbtn+x,ybtn+y) not in open_place:
                        open_place.append((xbtn+x,ybtn+y))
                        m_num = findMineNum(xbtn+x,ybtn+y)
                        clickbtn(xbtn+x,ybtn+y,mine_num=m_num)
                        if m_num == 0:
                            after_click.append((xbtn+x,ybtn+y))
                else:
                    if mine_place[ybtn+y][xbtn+x]:
                        mineNumber += 1
    if doAddMine:
        return
    return mineNumber

def test_click(mx,my,mpress=[True,False,False]):# 检测并判断点击
    global open_place,after_click
    xbtn = int(mx/BTN_S)-margin_left
    ybtn = int(my/BTN_S)-margin_top
    if mpress[0]:# 左键
        if (xbtn,ybtn) not in open_place and (xbtn,ybtn) not in tag_mine:
            open_place.append((xbtn,ybtn))
            if mine_place[ybtn][xbtn]:
                return clickbtn(xbtn,ybtn)
            m_num = findMineNum(xbtn,ybtn)
            clickbtn(xbtn,ybtn,mine_num=m_num)
            if m_num == 0:
                return findMineNum(xbtn,ybtn,True)
    elif mpress[2]:# 右键
        if (xbtn,ybtn) not in open_place:
            clickbtn(xbtn,ybtn,'R')
    return

def afterClick(clicklist:list):
    global after_click
    for i in clicklist:
        findMineNum(i[0],i[1],True)
        after_click.remove(i)
    if after_click != []:
        return afterClick(after_click)
    return

def clickbtn(xbtn,ybtn,mpress='L',mine_num=0,justthis=False):# 渲染点击画面
    global tags,tag_mine
    if mpress == 'L':# 左键
        pygame.draw.rect(window,styles[style_num-1][3],(BTN_S*(margin_left+xbtn),BTN_S*(margin_top+ybtn),BTN_S-1,BTN_S-1),0,2)
        if mine_place[ybtn][xbtn]:
            pygame.draw.circle(window,'black',(BTN_S*(margin_left+0.5+xbtn),BTN_S*(margin_top+0.5+ybtn)),BTN_S/2-1)
            return gameover(False)
        minenum = mine_num
        if justthis:
            minenum = findMineNum(xbtn,ybtn)
        if styles[style_num-1][0] == '黑白' and mine_num != 0:
            textcolor = 'black'
        else:
            textcolor = allcolor[minenum]
        showtext = showfont.render(str(minenum),True,textcolor)
        fw,fh = showtext.get_size()
        txp = BTN_S*(margin_left+0.5+xbtn)-fw/2
        typ = BTN_S*(margin_top+0.5+ybtn)-fh/2
        window.blit(showtext,(txp,typ))
    elif mpress == 'R':# 右键
        if justthis:
            pygame.draw.rect(window,'red',(BTN_S*(margin_left+xbtn),BTN_S*(margin_top+ybtn),BTN_S-1,BTN_S-1),0,2)
        elif (xbtn,ybtn) in tag_mine:
            tag_mine.remove((xbtn,ybtn))
            tags -= 1
            pygame.draw.rect(window,styles[style_num-1][2],(BTN_S*(margin_left+xbtn),BTN_S*(margin_top+ybtn),BTN_S-1,BTN_S-1),0,2)
        else:
            tag_mine.append((xbtn,ybtn))
            pygame.draw.rect(window,'red',(BTN_S*(margin_left+xbtn),BTN_S*(margin_top+ybtn),BTN_S-1,BTN_S-1),0,2)
            tags += 1
        setNowTip(True)
    return

class grade_gui(Frame):# 设置界面-难度样式
    def __init__(self,master=None):
        super().__init__(master) #super代表父类的定义
        self.master = master
        self.place(relheight=0.5,relwidth=1)
        self.creaft()
    def creaft(self):
        # 创建新组件
        self.grade = StringVar()
        self.grade.set(difficulty[game_grade-1])
        self.minenum = IntVar()
        self.minenum.set(mine_num)
        self.x = IntVar()
        self.x.set(X_NUM)
        self.y = IntVar()
        self.y.set(Y_NUM)
        self.tip_grade = Label(self,text=f'当前难度: {self.grade.get()}',font=('黑体',15),anchor='w')
        self.tip_grade.place(relwidth=0.6,relx=0.1,rely=0.05,relheight=0.15)
        # 注意:如果不加lambda:则会直接触发函数!
        self.issetnow = False
        self.setbtn = Button(self,text='自定义',command=lambda:self.gradesetGUI())
        self.setbtn.place(relwidth=0.2,relx=0.75,rely=0.05,relheight=0.15)
        self.easy_btn = Radiobutton(self,text='简单', value='简单', variable=self.grade, command=lambda:self.GUI_btnclick()).place(relwidth=1/3,rely=0.3)
        self.normal_btn = Radiobutton(self,text='正常',value='正常',variable=self.grade, command=lambda:self.GUI_btnclick()).place(relwidth=1/3,rely=0.3,relx=1/3)
        self.hard_btn = Radiobutton(self,text='困难', value='困难', variable=self.grade, command=lambda:self.GUI_btnclick()).place(relwidth=1/3,rely=0.3,relx=2/3)
        self.minenumtext = Label(self,text='当前雷数:'+str(self.minenum.get()),font=('黑体',12))
        self.minenumtext.place(relwidth=0.5,rely=0.55,relx=0)
        self.xy = Label(self,text=f'当前范围:{str(self.x.get())}x{str(self.y.get())}',font=('黑体',12))
        self.xy.place(relwidth=0.5,rely=0.55,relx=0.5)
    def GUI_btnclick(self):
        global X_NUM,Y_NUM,mine_num,game_grade
        g = self.grade.get()
        if g == difficulty[0]:
            X_NUM,Y_NUM = 9,9
            mine_num = 10
            game_grade = 1
        elif g == difficulty[1]:
            X_NUM,Y_NUM = 15,15
            mine_num = 20
            game_grade = 2
        elif g == difficulty[2]:
            X_NUM,Y_NUM = 25,25
            mine_num = 30
            game_grade = 3
        elif g == difficulty[3]:
            game_grade = 4
        self.tip_grade.config(text=f'当前难度: {g}')
        self.minenum.set(mine_num)
        self.x.set(X_NUM)
        self.y.set(Y_NUM)
        self.minenumtext.config(text='当前雷数:'+str(self.minenum.get()))
        self.xy.config(text=f'当前范围:{str(self.x.get())}x{str(self.y.get())}')
        return
    def gradesetGUI(self):
        global mine_num,X_NUM,Y_NUM
        if self.issetnow:
            return
        self.issetnow = True
        self.setGUI = Tk()
        setguiw = self.setGUI.winfo_screenwidth()
        setguih = self.setGUI.winfo_screenheight()
        centerx = int((setguiw - 300)/2)
        centery = int((setguih - 250)/2)
        self.setGUI.geometry(f'300x250+{centerx}+{centery}')
        self.setGUI.numLabel = Label(self.setGUI,text=f'总雷数:{mine_num}',font=('黑体',12))
        self.setGUI.numLabel.place(relwidth=0.6,relx=0.2,relheight=0.1,rely=0)
        self.setGUI.numScale = Scale(self.setGUI,from_=2,to=99,length=10,orient=HORIZONTAL,command=self.gradesetGUIset,variable=mine_num)
        self.setGUI.numScale.place(relwidth=0.8,relx=0.1,relheight=0.2,rely=0.08)
        self.setGUI.numScale.set(mine_num)
        self.setGUI.xynumLabel = Label(self.setGUI,text=f'范围:{X_NUM}X{Y_NUM}',font=('黑体',12))
        self.setGUI.xynumLabel.place(relwidth=0.6,relx=0.2,relheight=0.1,rely=0.28)
        self.setGUI.xnumScale = Scale(self.setGUI,from_=9,to=40,length=10,orient=HORIZONTAL,command=self.gradesetGUIset)
        self.setGUI.xnumScale.place(relwidth=0.8,relx=0.1,relheight=0.2,rely=0.4)
        self.setGUI.xnumScale.set(X_NUM)
        self.setGUI.ynumScale = Scale(self.setGUI,from_=5,to=30,length=10,orient=HORIZONTAL,command=self.gradesetGUIset)
        self.setGUI.ynumScale.place(relwidth=0.8,relx=0.1,relheight=0.2,rely=0.6)
        self.setGUI.ynumScale.set(Y_NUM)
        self.setGUI.quitbtn = Button(self.setGUI,text='保存当前设置',command=lambda:self.gradesetGUIquit()).place(relwidth=0.4,relx=0.3,relheight=0.15,rely=0.85)
        self.setGUI.title('自定义')
        self.setGUI.protocol('WM_DELETE_WINDOW',self.gradesetGUIquit)# 无论通过什么方式关闭都将执行该函数
        self.setGUI.mainloop()
    def gradesetGUIquit(self):
        global mine_num
        if X_NUM*Y_NUM < mine_num:
            mine_num = 2
            self.GUI_btnclick()
        self.issetnow = False
        self.setGUI.destroy()
    def gradesetGUIset(self,v):
        global mine_num,X_NUM,Y_NUM,game_grade
        mine_num = self.setGUI.numScale.get()
        X_NUM = self.setGUI.xnumScale.get()
        Y_NUM = self.setGUI.ynumScale.get()
        self.setGUI.numScale.config(to=X_NUM*Y_NUM-1)
        game_grade = 4
        if self.grade.get() != difficulty[3]:
            self.grade.set(difficulty[3])
        self.setGUI.numLabel.config(text=f'总雷数:{mine_num}')
        self.setGUI.xynumLabel.config(text=f'范围:{X_NUM}X{Y_NUM}')
        self.GUI_btnclick()

class color_gui(Frame):# 设置界面-主题样式
    def __init__(self,master=None):
        super().__init__(master) #super代表父类的定义
        self.master = master
        self.place(relheight=0.5,relwidth=1,rely=0.4)
        self.creaft()
    def creaft(self):
        # 创建新组件
        self.title = Label(self,text=f'当前主题: {styles[style_num-1][0]}',anchor='w',font=('黑体',15))
        self.title.place(relwidth=0.6,relheight=0.15,relx=0.1,rely=0)
        self.stylenum = IntVar()
        self.stylenum.set(style_num)
        self.blue_btn = Radiobutton(self,text=styles[0][0],value=1,variable=self.stylenum,command=lambda:self.display()).place(relwidth=1/3,relheight=0.2,relx=0,rely=0.2)
        self.green_btn = Radiobutton(self,text=styles[1][0],value=2,variable=self.stylenum,command=lambda:self.display()).place(relwidth=1/3,relheight=0.2,relx=1/3,rely=0.2)
        self.purple_btn = Radiobutton(self,text=styles[2][0],value=3,variable=self.stylenum,command=lambda:self.display()).place(relwidth=1/3,relheight=0.2,relx=2/3,rely=0.2)
        self.black1_btn = Radiobutton(self,text=styles[3][0],value=4,variable=self.stylenum,command=lambda:self.display()).place(relwidth=1/3,relheight=0.2,relx=0,rely=0.4)
        self.brown_btn = Radiobutton(self,text=styles[4][0],value=5,variable=self.stylenum,command=lambda:self.display()).place(relwidth=1/3,relheight=0.2,relx=1/3,rely=0.4)
        self.all_btn = Radiobutton(self,text=styles[5][0],value=6,variable=self.stylenum,command=lambda:self.display()).place(relwidth=1/3,relheight=0.2,relx=2/3,rely=0.4)
    def display(self):
        global style_num
        style_num = self.stylenum.get()
        self.title.config(text=f'当前主题: {styles[style_num-1][0]}')

def setUpWindow():# 设置窗口
    global game_grade,root
    before_list = [game_grade,X_NUM,Y_NUM,mine_num,style_num]
    root = Tk()
    root.resizable(False,False)
    root.title('游戏设置')
    rootw = root.winfo_screenwidth()
    rooth = root.winfo_screenheight()
    centerx = int((rootw - 300)/2)
    centery = int((rooth - 300)/2)
    root.geometry(f'300x300+{centerx}+{centery}')
    gradeGUI = grade_gui(master=root)
    colorGUI = color_gui(master=root)
    quitbtn = Button(root,text='保存设置',command=root.destroy)
    quitbtn.place(relheight=0.15,relwidth=0.25,relx=0.7,rely=0.8)
    root.mainloop()
    if [game_grade,X_NUM,Y_NUM,mine_num,style_num] != before_list:
        return True
    return False

def ruleWindow():# 说明窗口
    global game_grade,root
    before_list = [game_grade,X_NUM,Y_NUM,mine_num,style_num]
    root = Tk()
    root.resizable(False,False)
    root.title('游戏说明')
    rootw = root.winfo_screenwidth()
    rooth = root.winfo_screenheight()
    centerx = int((rootw - 300)/2)
    centery = int((rooth - 300)/2)
    root.geometry(f'300x300+{centerx}+{centery}')
    rule = Text(root,width=20,height=9)
    soll = Scrollbar(root)
    rule.place(relheight=0.75,relwidth=0.9,relx=0.05,rely=0.05)
    soll.place(relx=0.95,relheight=0.75,rely=0.05)
    soll.config(command=rule.yview)
    rule.insert(END,'\t—— 扫雷 游戏说明 —— \n\n')
    rule.insert(END,'|游戏介绍|\n\n     本游戏默认难度为简单,在指定的雷区内埋了9个雷,雷区由9x9个方格组成.\n\n')
    rule.insert(END,'|游戏规则|\n\n     玩家需要将所有没有埋雷的方格全部挖开(点击)即可胜利,如果在此过程中挖开了埋有雷的方格即失败.\n\n')
    rule.insert(END,'|游戏设置|\n\n     此游戏的难度分为简单\普通\困难 和 自定义,同时样式也有六种,在游戏界面按下ESC键即可进入设置页面设置.\n\n')
    rule.insert(END,'|关于游戏|\n\n     此游戏为 @聪明的电八 改编自扫雷\n')
    rule.config(yscrollcommand=soll.set,state='disabled')
    quitbtn = Button(root,text='关闭说明',command=root.destroy)
    quitbtn.place(relheight=0.125,relwidth=0.25,relx=0.7,rely=0.85)
    root.mainloop()
    if [game_grade,X_NUM,Y_NUM,mine_num,style_num] != before_list:
        return True
    return False

def setNowTip(isForTags=False):# 渲染上方提示
    global counts
    if not isForTags:
        counts += 1
    pygame.draw.rect(window,styles[style_num-1][1],(0,BTN_S*1.5,WIN_W,BTN_S))
    nowTip = showfont.render(f'当前用时: {counts}秒    当前标记: {tags}个',True,styles[style_num-1][5],styles[style_num-1][1])
    window.blit(nowTip,(WIN_W/2-nowTip.get_size()[0]/2,BTN_S*1.5))

def btn_events(mx,my):
    for i in btn_commands:
        if i[0][0]+i[0][2] > mx > i[0][0] and i[0][1]+i[0][3] > my > i[0][1]:
            pygame.draw.rect(window,'black',(i[0][0],i[0][1],i[0][2],i[0][3]),1,2)
            pygame.draw.rect(window,'gray',(i[0][0],i[0][1],i[0][2],i[0][3]),0,2)
            pygame.display.update()
            pygame.time.delay(50)
            return eval(i[1])

def gameover(iswin:bool=False,animation:bool=False,update:int=0):# 游戏结束显示
    global gameend,counts,isAnimation
    if animation:
        update += 1
    else:
        pygame.time.set_timer(COUNT,0)
        gameend = True
        isAnimation = True
        return gameover(iswin,True,0)
    if update < 7:
        tip_h = update*BTN_S
        tip_w = update*BTN_S
    elif update < 11:
        tip_h = 7*BTN_S
        tip_w = update*BTN_S
    else:
        tip_h = 7*BTN_S
        tip_w = 11*BTN_S
    pygame.draw.rect(window,'yellow',(WIN_W/2-tip_w/2,WIN_H/2-tip_h/2,tip_w,tip_h),0,5)
    pygame.draw.rect(window,'black',(WIN_W/2-tip_w/2,WIN_H/2-tip_h/2,tip_w,tip_h),5,5)
    if iswin:
        titletext = 'You Win'
    else:
        titletext = 'You Lose'
    if update < 11:
        fontsize = update*3
    else: 
        fontsize = 40
    try:
        text = pygame.font.Font('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\unifont-12.1.04.ttf',fontsize).render(titletext,True,'black')
    except:
        text = pygame.font.SysFont(pygame.font.get_fonts()[0],fontsize).render(titletext,True,'black')
    tw,th = text.get_size()
    txp = WIN_W/2-tw/2
    typ = WIN_H/2-th/2-BTN_S
    window.blit(text,(txp,typ))
    if update == 11:
        text2 = showfont.render(f'用时: {counts}秒',True,'black','yellow')
        counts = 0
        tw,th = text2.get_size()
        txp = WIN_W/2-tw/2
        typ = WIN_H/2+BTN_S/2
        window.blit(text2,(txp,typ))
        text3 = showfont.render('点击以重新开始',True,'black','yellow')
        tw,th = text3.get_size()
        txp = WIN_W/2-tw/2
        typ = WIN_H/2+BTN_S*2
        window.blit(text3,(txp,typ))
        isAnimation = False
        return
    else:
        pygame.display.update()
        pygame.time.delay(50)
        return gameover(iswin,True,update)

def game_quit():# 退出游戏
    global X_NUM,Y_NUM
    write_data = f'game_grade = {game_grade}\nstyle = {style_num}\nmine_num = {mine_num}\nX_NUM = {X_NUM}\nY_NUM = {Y_NUM}'
    if open_place == [] or gameend:
        with open('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\扫雷\\FindMine.txt','w+',encoding='UTF-8') as file:
            file.write(write_data)
        pygame.quit()
        return sys.exit()
    is_quit = messagebox.askyesnocancel('提示','是否保存当前游戏进度?')
    if is_quit == None:   
        return
    if len(str(X_NUM)) < 2:
        X_NUM = '0'+str(X_NUM)
    if len(str(Y_NUM)) < 2:
        Y_NUM = '0'+str(Y_NUM)
    with open('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\扫雷\\FindMine.txt','w+',encoding='UTF-8') as file:
        if is_quit:
            write_data = write_data + f'\n{str(open_place)}\n{str(mine_place)}\n{str(tag_mine)}'
        file.write(write_data)
    pygame.quit()
    return sys.exit()

draw_init()
pygame.display.update()

while True:
    if isAnimation:
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not is_setup:
            if gameend:# 游戏结束
                draw_init(True)
                continue
            mousex,mousey = pygame.mouse.get_pos()
            if BTN_S*margin_left < mousex < WIN_W-BTN_S*margin_left and BTN_S*margin_top < mousey < WIN_H-margin_bottom:
                if open_place == []:
                    start_time = time.strftime('%H-%M-%S')
                    setNowTip(True)
                    pygame.time.set_timer(COUNT,1000)
                test_click(mousex,mousey,pygame.mouse.get_pressed())
                if after_click != []:
                    afterClick(after_click)
                if len(open_place) == X_NUM*Y_NUM-mine_num:
                    gameover(True)
            elif btn_commands != []:
                btn_events(mousex,mousey)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and not is_setup:# 按下ESC键
                is_setup = True
                getset = setUpWindow()
                if getset:
                    draw_init(True)
                is_setup = False
            elif event.key == pygame.K_F1 and not is_setup:# 按下F1键
                is_setup = True
                getset = ruleWindow()
                if getset:
                    draw_init(True)
                is_setup = False
        elif event.type == COUNT:
            setNowTip()
        pygame.display.update()