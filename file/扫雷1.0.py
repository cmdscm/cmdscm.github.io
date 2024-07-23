import pygame
import random
from tkinter import *
import sys
import re
import os

'''
扫雷1.0
运用txt文件保存数据
可切换难度
缺点:读取麻烦
'''

def game_init(isset=False):# 游戏初始化
    global mine_num,mine_place,showfont,titlefont,allcolor,tag_mine,gameend,BTN_S,WIN_H,WIN_W,window,tags,open_place,after_click,X_NUM,Y_NUM,margin_top,margin_left,margin_bottom,is_setup,game_grade
    if not isset:
        obj = re.compile(r'\d(?P<value>.*)\d')
        with open('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\扫雷\\FindMine.txt','r+',encoding='UTF-8') as file:
            text = file.read()
            t = obj.finditer(text)
            tlist = []
            for i in t:
                tlist.append(i.group())
            if text == '' or len(tlist) < 3:
                file.seek(0)
                file.truncate()# 清空文件
                file.write('game_grade = 简单\nmine_num = 10\nX_NUM = 09\nY_NUM = 09')
                mine_num = 10# 地雷数
                X_NUM,Y_NUM = 9,9# 横轴格数 纵轴格数
                game_grade = '简单'# 游戏难度
            else:
                print(tlist)
                mine_num = int(tlist[0])# 地雷数
                X_NUM = int(tlist[1])# 横轴格数
                Y_NUM = int(tlist[2])#  纵轴格数
                game_grade = text[13:15]# 游戏难度
    mine_place = []# 地雷位置
    open_place = []# 已经打开的位置
    allcolor = ['lightblue','orangered','darkblue','blue','brown','pink','blue','red','black']# 显示数字颜色
    tag_mine = []# 已经标记的位置
    gameend = False# 游戏是否结束
    BTN_S = 20# 按钮尺寸
    WIN_W,WIN_H = BTN_S*(X_NUM+4),BTN_S*(Y_NUM+7)# 窗口尺寸
    margin_top = 3# 上外边距
    margin_left = 2# 左外边距
    margin_bottom = WIN_H-BTN_S*(Y_NUM+margin_top)# 下外边距
    is_setup = False# 是否打开设置窗口
    tags = 0# 已经标记的雷数
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
    window.fill('lightgray')
    pygame.display.set_caption('扫雷')
    pygame.display.flip()

def make_mine(xnum,ynum):# 生成地雷
    n = 0
    minelist = []
    for i in range(ynum):
        minelist.append([])
        for j in range(xnum):
            minelist[i].append(False)
    while n<mine_num:
        a,b = random.randint(0,ynum-1),random.randint(0,xnum-1)
        if minelist[a][b] != True:
            minelist[a][b] = True
            n += 1
    return minelist

def draw_init(isset=False):# 渲染游戏画面
    global mine_place,mine_title
    if isset:
        game_init(isset)
    else:
        game_init()
    mine_place = make_mine(X_NUM,Y_NUM)
    pygame.draw.rect(window,'gray',(BTN_S*margin_left,BTN_S*margin_top,BTN_S*X_NUM,BTN_S*Y_NUM))
    for c,cindex in enumerate(mine_place):
        for r,rindex in enumerate(cindex):
            xpos,ypos = (r+margin_left)*BTN_S,(c+margin_top)*BTN_S
            btns = BTN_S 
            pygame.draw.rect(window,'blue',(xpos,ypos,btns-1,btns-1),0,2)
    title1 = showfont.render(f'总雷数:{mine_num}    已标记:  ',True,'blue')
    mine_title = showfont.render(str(tags),True,'darkblue')
    tip1 = showfont.render('找出所有雷即可获胜',True,'black')
    tip2 = showfont.render('按下ESC键打开游戏设置',True,'black')
    window.blit(tip1,(WIN_W/2-tip1.get_size()[0]/2,WIN_H-BTN_S*3))
    window.blit(tip2,(WIN_W/2-tip2.get_size()[0]/2,WIN_H-BTN_S*1.5))
    window.blit(title1,(WIN_W/2-title1.get_size()[0]/2,BTN_S))
    window.blit(mine_title,(WIN_W/2+title1.get_size()[0]/2,BTN_S))

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

def clickbtn(xbtn,ybtn,mpress='L',mine_num=0):# 渲染点击画面
    global tags,tag_mine
    if mpress == 'L':# 左键
        pygame.draw.rect(window,'lightblue',(BTN_S*(margin_left+xbtn),BTN_S*(margin_top+ybtn),BTN_S-1,BTN_S-1),0,2)
        if mine_place[ybtn][xbtn]:
            pygame.draw.circle(window,'black',(BTN_S*(margin_left+0.5+xbtn),BTN_S*(margin_top+0.5+ybtn)),BTN_S/2-1)
            return gameover(False)
        textcolor = allcolor[mine_num]
        showtext = showfont.render(str(mine_num),True,textcolor)
        fw,fh = showtext.get_size()
        txp = BTN_S*(margin_left+0.5+xbtn)-fw/2
        typ = BTN_S*(margin_top+0.5+ybtn)-fh/2
        window.blit(showtext,(txp,typ))
    elif mpress == 'R':# 右键
        if (xbtn,ybtn) in tag_mine:
            tag_mine.remove((xbtn,ybtn))
            tags -= 1
            pygame.draw.rect(window,'blue',(BTN_S*(margin_left+xbtn),BTN_S*(margin_top+ybtn),BTN_S-1,BTN_S-1),0,2)
        else:
            tag_mine.append((xbtn,ybtn))
            pygame.draw.rect(window,'red',(BTN_S*(margin_left+xbtn),BTN_S*(margin_top+ybtn),BTN_S-1,BTN_S-1),0,2)
            tags += 1
        mine_title = showfont.render(str(tags),True,'darkblue','lightgray')
        title1 = showfont.render('总雷数:10    已标记:  ',True,'blue')
        pygame.draw.rect(window,'lightgray',(WIN_W/2+title1.get_size()[0]/2,BTN_S,BTN_S*2,BTN_S))
        window.blit(mine_title,(WIN_W/2+title1.get_size()[0]/2,BTN_S))
    return

def gameover(iswin):# 游戏结束显示
    global gameend
    gameend = True
    tip_w = 11*BTN_S
    tip_h = 7*BTN_S
    pygame.draw.rect(window,'yellow',(WIN_W/2-tip_w/2,WIN_H/2-tip_h/2,tip_w,tip_h),0,5)
    pygame.draw.rect(window,'black',(WIN_W/2-tip_w/2,WIN_H/2-tip_h/2,tip_w,tip_h),5,5)
    if iswin:
        text = titlefont.render('You win',True,'black')
    else:
        text = titlefont.render('You lose',True,'black')
    tw,th = text.get_size()
    txp = WIN_W/2-tw/2
    typ = WIN_H/2-th/2-BTN_S
    window.blit(text,(txp,typ))
    text2 = showfont.render('点击以重新开始',True,'black','yellow')
    tw,th = text2.get_size()
    txp = WIN_W/2-tw/2
    typ = WIN_H/2+BTN_S*2
    window.blit(text2,(txp,typ))

class gui(Frame):
    def __init__(self,master=None):
        super().__init__(master) #super代表父类的定义
        self.master = master
        self.place(relheight=0.5,relwidth=1)
        self.creaft()
    def creaft(self):
        #创建新组件
        self.grade = StringVar()
        self.grade.set(game_grade)
        self.minenum = IntVar()
        self.minenum.set(mine_num)
        self.x = IntVar()
        self.x.set(X_NUM)
        self.y = IntVar()
        self.y.set(Y_NUM)
        self.tip_grade = Label(self,text='当前难度为:'+self.grade.get(),font=('黑体',15))
        self.tip_grade.pack(pady=5)
        # 注意:如果不加lambda:则会直接触发函数!
        self.easy_btn = Radiobutton(self,text='简单', value='简单', variable=self.grade, command=lambda:self.GUI_btnclick()).place(relwidth=1/3,rely=0.3)
        self.normal_btn = Radiobutton(self,text='正常',value='正常',variable=self.grade, command=lambda:self.GUI_btnclick()).place(relwidth=1/3,rely=0.3,relx=1/3)
        self.hard_btn = Radiobutton(self,text='困难', value='困难', variable=self.grade, command=lambda:self.GUI_btnclick()).place(relwidth=1/3,rely=0.3,relx=2/3)
        self.minenumtext = Label(self,text='当前雷数:'+str(self.minenum.get()),font=('黑体',12))
        self.minenumtext.place(relwidth=0.5,rely=0.6,relx=0)
        self.xy = Label(self,text=f'当前范围:{str(self.x.get())}x{str(self.y.get())}',font=('黑体',12))
        self.xy.place(relwidth=0.5,rely=0.6,relx=0.5)
    def GUI_btnclick(self):
        global X_NUM,Y_NUM,mine_num,game_grade
        g = self.grade.get()
        self.tip_grade.config(text='当前难度为:'+g)
        if g == '简单':
            X_NUM,Y_NUM = 9,9
            mine_num = 10
            game_grade = g
        if g == '正常':
            X_NUM,Y_NUM = 15,15
            mine_num = 20
            game_grade = g
        if g == '困难':
            X_NUM,Y_NUM = 25,25
            mine_num = 30
            game_grade = g
        self.minenum.set(mine_num)
        self.x.set(X_NUM)
        self.y.set(Y_NUM)
        self.minenumtext.config(text='当前雷数:'+str(self.minenum.get()))
        self.xy.config(text=f'当前范围:{str(self.x.get())}x{str(self.y.get())}')
        return
    
def setUpWindow():
    global game_grade
    g = game_grade
    root = Tk()
    root.resizable(False,False)
    root.title('游戏设置')
    rootw = root.winfo_screenwidth()
    rooth = root.winfo_screenheight()
    centerx = int((rootw - 300)/2)
    centery = int((rooth - 300)/2)
    root.geometry(f'300x300+{centerx}+{centery}')
    app = gui(master=root)
    quitbtn = Button(root,text='保存设置',command=root.destroy)
    quitbtn.place(relheight=0.15,relwidth=0.25,relx=0.7,rely=0.8)
    root.mainloop()
    if game_grade != g:
        return True
    return False
draw_init()
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\扫雷\\FindMine.txt','w+',encoding='UTF-8') as file:
                if len(str(X_NUM)) < 2:
                    X_NUM = '0'+str(X_NUM)
                if len(str(Y_NUM)) < 2:
                    Y_NUM = '0'+str(Y_NUM)
                file.write(f'game_grade = {game_grade}\nmine_num = {mine_num}\nX_NUM = {X_NUM}\nY_NUM = {Y_NUM}')
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not is_setup:
            if gameend:
                draw_init(True)
            else:
                mousex,mousey = pygame.mouse.get_pos()
                if BTN_S*margin_left < mousex < WIN_W-BTN_S*margin_left and BTN_S*margin_top < mousey < WIN_H-margin_bottom:
                    test_click(mousex,mousey,pygame.mouse.get_pressed())
                    if after_click != []:
                        afterClick(after_click)
                    if len(open_place) == X_NUM*Y_NUM-mine_num:
                        gameover(True)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and not is_setup:# 按下ESC键
                is_setup = True
                getset = setUpWindow()
                if getset:
                    draw_init(True)
                is_setup = False
        pygame.display.update()