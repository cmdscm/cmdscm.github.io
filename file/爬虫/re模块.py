import re

a = re.findall(r"\d+","204kdkdkdfk353")#list
b=re.search(r"\d+","204kdkdkdfk353")#first
print(a)
print(b.group())
c=re.finditer(r"\d+","ev54b5nm7nb")#迭代器
for item in c:
    print(item.group())

#预加载

obj = re.compile(r"\d+")

#直接字符串

obj.findall()
obj.finditer()
obj.search()


#正则表达式

#1.普通字符
#2.元字符：\d数字\w数字英文下划线
#\D除数字以外的内容   \W除数字英文下划线的内容
#[abc]匹配a,b,c
#[^abc]除了a,b,c以外的内容
# . 除了换行符都能
#3.量词
#控制元字符出现次数
#+ 元字符出现一次或多次
#* 尽可能多的匹配，元字符出现0次或多次
#？ 出现0次或一次

#实验网址：https://tool.oschina.net/regex

#.*? 将可能少的匹配 惰性匹配 匹配到距离xxx最近的xxx

#