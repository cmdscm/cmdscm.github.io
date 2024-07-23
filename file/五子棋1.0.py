import pygame
import sys
from tkinter import *
from tkinter import messagebox

def game_init():
    global window,WIN_W,WIN_H,blockx,blocky,click_list,state,margin_left,margin_top,gameover
    pygame.init()
    pygame.display.set_caption('五子棋')
    blockx,blocky = 20,20
    WIN_W,WIN_H = blockx*14+80,blocky*14+80
    click_list = []# 已点击的列表
    state = True# True=黑 False=白
    margin_left,margin_top = 40,40
    gameover = False
    window = pygame.display.set_mode((WIN_W,WIN_H))
    draw_init()
    pygame.display.flip()

def draw_init():
    window.fill('#fe9933')# 棋盘颜色
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    for x in range(0,15):# 绘制行
        setText(str(x+1),posx=margin_left-10,posy=x*20+margin_top,fontsize=10)
        pygame.draw.line(window,'black',(margin_left,x*blockx+margin_top),(WIN_W-margin_left,x*blockx+margin_top))
        setText(str(x+1),posx=WIN_W-margin_left+10,posy=x*20+margin_top,fontsize=10)
    for y in range(0,15):# 绘制列
        setText(letter[y],posx=y*20+margin_left,posy=margin_top-10,fontsize=10)
        pygame.draw.line(window,'black',(y*blocky+margin_left,margin_top),(y*blocky+margin_left,WIN_H-margin_top))
        setText(letter[y],posx=y*20+margin_left,posy=WIN_H-margin_top+10,fontsize=10)
    pygame.draw.circle(window,'black',(margin_left+7*blockx,margin_top+7*blocky),3)
    pygame.draw.circle(window,'black',(margin_left+3*blockx,margin_top+3*blocky),3)
    pygame.draw.circle(window,'black',(WIN_W-margin_left-3*blockx,margin_top+3*blocky),3)
    pygame.draw.circle(window,'black',(WIN_W-margin_left-3*blockx,WIN_H-margin_top-3*blocky),3)
    pygame.draw.circle(window,'black',(margin_left+3*blockx,WIN_H-margin_top-3*blocky),3)
    setButton(window,(WIN_W/2,blocky/2,blockx*4,blocky),'yellow','重新开始')
    if click_list == []:
        return
    for num,i in enumerate(click_list):
        color = 'white'
        if num % 2 == 0:
            color = 'black'
        pygame.draw.circle(window,color,((i[0]+1)*20,(i[1]+1)*20),6)

def setText(
        text:str,textcolor:str|tuple|list|None='black',background:str|tuple|list|None=None,
        posx:int|float|None=10,posy:int|float|None=10,fontsize=15
        ):# 注意:posx,posy为中心坐标,不是左上角坐标!
    try:
        showfont = pygame.font.Font('E:\\vscode5月27日下载\\文件\\python\\pygame-file\\unifont-12.1.04.ttf',fontsize)
    except:
        showfont = pygame.font.SysFont(pygame.font.get_fonts()[0],fontsize)
    showtext = showfont.render(text,True,textcolor,background)
    textw,texth = showtext.get_size()
    window.blit(showtext,(posx-textw/2,posy-texth/2))
    return

def setButton(surface,rect:tuple|list,backgroundcolor:str|None='white',text:str|None='Text',textcolor:str|tuple|list|None='black',
            fontsize:int|float|None=15):
    setx,sety = rect[0]-rect[2]/2,rect[1]-rect[3]/2
    pygame.draw.rect(surface,backgroundcolor,(setx,sety,rect[2],rect[3]),0,5)
    pygame.draw.rect(surface,'black',(setx,sety,rect[2],rect[3]),2,5)
    setText(text,textcolor,posx=rect[0],posy=rect[1],fontsize=fontsize)

def isWin1(pos:tuple|list,state,xy:str='x'):
    x,y = pos[0],pos[1]
    left,right = True,True
    xi,yi = 1,0
    if xy == 'y':
        xi,yi = 0,1
    num = 1
    while left or right:
        if left and (x+xi,y+yi,state) in click_list:
            num += 1
        else:
            left = False
        if right and (x-xi,y-yi,state) in click_list:
            num += 1
        else:
            right = False
        if xy == 'x':
            xi += 1
        else:
            yi += 1
    if num > 4:
        return game_over(state)
    elif xy == 'x':
        return isWin1(pos,state,'y')
    else:
        return isWin2(pos,state)

def isWin2(pos:tuple|list,state,xy:str='x'):
    x,y = pos[0],pos[1]
    left,right = True,True
    xi,yi = 1,1
    if xy == 'y':
        xi,yi = -1,1
    num = 1
    while left or right:
        if left and (x+xi,y+yi,state) in click_list:
            num += 1
        else:
            left = False
        if right and (x-xi,y-yi,state) in click_list:
            num += 1
        else:
            right = False
        if xy == 'x':
            xi += 1
            yi += 1
        else:
            yi += 1
            xi -= 1
    if num > 4:
        return game_over(state)
    elif xy == 'x':
        return isWin2(pos,state,'y')
    else:
        return False

class btn_gui(Frame):# 结束界面-按钮布局
    def __init__(self,master=None):
        super().__init__(master) #super代表父类的定义
        self.master = master
        self.place(relheight=0.4,relwidth=1,rely=0.5)
        self.creaft()
    def creaft(self):
        # 创建新组件
        quitbtn = Button(self,text='退出游戏',command=lambda:self.quitAll())
        quitbtn.place(relheight=0.5,relwidth=0.4,relx=0.05,rely=0.25)
        resetbtn = Button(self,text='重新开始',command=lambda:self.reset())
        resetbtn.place(relheight=0.5,relwidth=0.4,relx=0.55,rely=0.25)
    def reset(self):
        self.master.destroy()
        game_init()
    def quitAll(self):
        self.master.destroy()
        pygame.quit()
        sys.exit()

def game_over(winner:bool):#赢家/动画次数
    global gameover
    gameover = True
    root = Tk()
    root.resizable(False,False)
    root.title('游戏结束!')
    rootw = root.winfo_screenwidth()
    rooth = root.winfo_screenheight()
    centerx = int((rootw - 300)/2)
    centery = int((rooth - 300)/2)
    root.geometry(f'300x300+{centerx}+{centery}')
    if winner:
        title = Label(root,text='黑棋胜利!',font=('黑体',20))
    else:
        title = Label(root,text='白棋胜利!',font=('黑体',20))
    btn_gui(root)
    title.place(relheight=0.2,relwidth=1,relx=0,rely=0)
    root.mainloop()

game_init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousex,mousey = pygame.mouse.get_pos()
            if WIN_W/2-blockx*2-1 < mousex < WIN_W/2+blockx*2+1 and mousey < blocky+1:
                game_init()
                continue
            mousex += 10
            mousey += 10
            if margin_left-2 < mousex < WIN_W-margin_left+15 and margin_top-2 < mousey < WIN_H-margin_top+15:
                mx,my = int(mousex/20)-1,int(mousey/20-1)
                if (mx,my,True) in click_list or (mx,my,False) in click_list:
                    continue
                click_list.append((mx,my,state))
                color = 'white'
                if state:
                    color = 'black'
                pygame.draw.circle(window,color,((mx+1)*20,(my+1)*20),6)
                iswin = isWin1((mx,my),state,'x')
                if iswin == False:
                    state = not state
                else:
                    continue
        elif not gameover and event.type == pygame.MOUSEMOTION:
            mousex,mousey = pygame.mouse.get_pos()
            mousex += 10
            mousey += 10
            if margin_left < mousex < WIN_W-margin_left+10 and margin_top < mousey < WIN_H-margin_top+10:
                mx,my = int(mousex/20),int(mousey/20)
                if (mx-1,my-1,True) in click_list or (mx-1,my-1,False) in click_list:
                    continue
                draw_init()
                color = 'white'
                if state:
                    color = 'black'
                pygame.draw.circle(window,color,(mx*20,my*20),6)
        pygame.display.update()