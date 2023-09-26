#xpath解析
#对主页面分析
#抓取主页面所有链接地址

from lxml import etree

#要加载数据
f = open('xpath解析辅助.html',mode="r",encoding="utf-8")

yema=f.read()
##加载数据返回节点
et = etree.HTML(yema)

result = et.xpath("/html")
result = et.xpath("/html/body/*/li/a/@href")#杠表示一层html节点,
#text()表示提取标签中的文本信息,*表示任意的，通配的,@表示
#属性
print(result)
result = et.xpath("//li/a/@href")#//表示任意位置
print(result)
result = et.xpath("//li[@class='a']/a/@href")#[@xx='xx']
#是属性的限定
print(result)
result = et.xpath("/html/body/ul/li")
print()
for item in result:
    href=item.xpath("./a/@href")[0]#.表示当前这个元素
    text=item.xpath("./a/text()")[0]#.表示当前这个元素
    print(text,href)