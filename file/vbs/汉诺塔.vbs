dim n
n=3
hnt "A","B","C",n
Function hnt(a,b,c,d)
	if d=1 then
		msgbox a&"->1->"&c
	else
		hnt a,c,b,d-1
		msgbox a&"->"&n&"->"&c
		hnt b,a,c,d-1
	end if
End Function