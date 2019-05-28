print('小姐姐我们一起学习!')
x=3
print(x)
if x > 10:
    print("jsfksjdkfl")
if x <= 10:
    print("that's it")



def simpleOp():
	#简单计算
	inputnbr1=input("Enter a Number： ")
	x=float(inputnbr1)
	print(x)

	inputsign1=input("Enter a Sign")
	print(x,inputsign1)

	inputnbr2=input("Enter another number: ")
	y=float(inputnbr2)
	print(x,inputsign1,y)

	result=0

	if inputsign1=="+":
		result=x+y
	elif inputsign1=="-":
		result=x-y
	elif  inputsign1=="*":
		result=x*y
	elif inputsign1=="/":
		result=x/y

	print(x,inputsign1,y,"=",result)


simpleOp()
