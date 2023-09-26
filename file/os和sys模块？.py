from os import system
from os import listdir

#system("start cmd")

import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com",465)
smtp_obj.login("1348713675@qq.com","654gyq321")
smtp_obj.set_debuglevel(1)

msg = MIMEText("这是一个用于测试的信,如果你收到了,麻烦向1348713675@qq.com回信,回一个1就行","plain","utf-8")
msg["from"] = Header("人","utf-8")
msg["to"] = Header("收到邮件的幸运儿","utf-8")
msg["Subject"] = Header("一封测试信","utf-8")

smtp_obj.sendmail("1348713675@qq.com",["2942738375@qq.com","154802554@qq.com"],
msg.as_string())