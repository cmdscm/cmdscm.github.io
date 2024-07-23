import requests
from tkinter import *
def fanyi(value):
    cando = True
    if value == '':
        return
    url="https://fanyi.baidu.com/sug"
    sj={"kw": str(value),
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'}
    ydm =requests.post(url,data=sj)
    dicttext = dict(ydm.json())
    try:
        del dicttext['errno']
        del dicttext['logid']
        dicttext = dicttext['data']
    except:
        dicttext = []
    if dicttext == []:
        dicttext = list(dicttext)
        dicttext.append(value)
        cando = False
    showtext = ''
    if cando:
        for i in dicttext:
            if len(i['k']) == len(value):
                showtext = showtext+i['v']
    else:
        showtext = dicttext[0]
    answertext.config(state='normal')
    answertext.delete(1.0,END)
    answertext.insert(1.0,showtext)
    answertext.config(state='disabled')
root = Tk()
h = root.winfo_screenheight()
w = root.winfo_screenwidth()
win_str = '%dx%d+%d+%d' % (300,300,(w-300)/2,(h-300)/2)
root.geometry(win_str)
root.resizable(0,0)
root.title('单词翻译器')
titlelbl = Label(root,text='单词翻译器',font=('黑体',20))
titlelbl.pack(pady=2)
tiplbl = Label(root,text='输入翻译的单词将翻译成英语',bg='skyblue',fg='white',font=('粗体',13))
tiplbl.pack(pady=2)
wordstr = StringVar()
wordinput = Entry(root,textvariable=wordstr)
wordinput.pack(pady=3)
updatebtn = Button(root,text='翻译',width=10,command=lambda:fanyi(wordstr.get()))
updatebtn.pack(pady=2)
tip2lbl = Label(root,text='翻译结果',bg='lightgreen',fg='green',font=('粗体',12))
tip2lbl.pack(fill='y',ipady=4,pady=4)
answertext = Text(root,bg='lightblue',relief='solid')
answertext.insert(1.0,'翻译结果会在这里出现')
answertext.config(state='disabled')
answertext.place(relwidth=0.8,relx=0.1,relheight=0.4,rely=0.55)
root.mainloop()

