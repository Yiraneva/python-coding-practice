# 1> if 里面 define 的 st 是 global 的， 但是 def 里面的 st 是 local 的
# 2> 注意缩进要对齐
# 3> st = "a if C else b" 对， st = "a if C else st = b" 错，不要if else statement里面再重复赋值
#
# Example file for working with conditional statements
#



def main():
    x, y = 1000, 100
    # conditional flow uses if, elif, else  
    if x<y:
        st = "x is less than y."
    elif x==y:
        st = "x is equal to y"
    else:
        st = "x is greater than y"
    print(st)

    # conditional statements let you use "a if C else b"
    
    st = "x is greater than y" if (x>y) else "x is less than or equals to y"
    print(st)



if __name__ == "__main__":
    main()



        # conditional flow uses if, elif, else  
    st = "a"
    print(st)

    # conditional statements let you use "a if C else b"
print(st)




