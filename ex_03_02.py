# excise_03_02
# Try and quit
vh=input("您工作的小时数是: ")
vr=input("每小时的工资是: ")

try:
	fh=float(vh)
	fr=float(vr)
except:
	print("错啦！您输入的不是数字,您的工资没啦！")
	quit()

if fh<=10:
	salary=fh*fr
elif fh>10:
	salary=(fh-10)*(fr/2)+fr*10

print("您的工资是:",salary,"元" )


	

