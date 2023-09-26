dim zscj ,lscj
zscj = 90
lscj = 95
dim cj(50)
dim m
m=0
while(m<5)
	cj(m)=inputbox("ÇëÊäÈë³É¼¨£º")
	m=m+1
wend
pj=0
i=0
while(i<5)
	pj=pj+cj(i)
	i=i+1
wend
msgbox pj/5



