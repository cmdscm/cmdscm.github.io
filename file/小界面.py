import tkinter as tk
from os import system
a = "fou"
b=0
# 创建主窗口
window = tk.Tk()
window.title("小程序")

# 创建标签
label = tk.Label(window, text="按下按钮！", font=("Arial", 14))
label.pack(pady=20)

# 创建按钮点击事件的处理函数
def button_click():
    global a
    if a == "fou":
        label.config(text="you are open button!")
        a="shi"
    else:
        label.config(text="you are close button!")
        a ="fou"

def button_cmd():
    global b
    system("start cmd")
# 创建按钮
button = tk.Button(window, text="点击我", command=button_click)
button.pack(pady=10)

label2 =tk.Label(window,text="按下我打开cmd",font=("Georgia",18))
label2.pack(anchor="n",padx=20,pady=30)

button = tk.Button(window,text="立刻打开",command=button_cmd)
button.pack(pady=20,padx=20)
# 设置窗口尺寸
window.geometry("400x300")

# 进入主循环
window.mainloop()
