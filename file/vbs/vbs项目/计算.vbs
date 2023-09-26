dim a,op,b
a=inputbox("输入第一个数字")
op=inputbox("输入计算方法")
b=inputbox("输入第二个数字")
a=cdbl(a)
b=cdbl(b)
if op="+" then msgbox a+b
if op="-" then msgbox a-b
if op="*" then msgbox a*b
if op="/" then msgbox a/b