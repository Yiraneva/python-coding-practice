#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return(x*x*x)

# function with default value for an argument
def power(num, x=1):
    result=1
    for x in range(x):
        result=result * num
    return result

print(power(2))
print(power(2,3))

#function with variable number of arguments
def multiAdd(*arguments):
    result=1 # 赋值？
    for x in arguments:
        result=result + x

    return result


#Exerecise: 
#print(func1)
#print(func2(20,30))
#func2(10,20)  why there is no "none" as return?
#cube(3) why this run nothing?

# print -> return?
# print(cube(3))

print(multiAdd(1, 2, 3, 5))
