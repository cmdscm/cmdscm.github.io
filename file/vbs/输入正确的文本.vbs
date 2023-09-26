dim x
x=inputbox("请输入文本：","输入文本")
while(x<>"正确的文本")
	x=inputbox(x&"这个文本是错误的！","请输入正确的文本！")
wend
msgbox "输入成功"