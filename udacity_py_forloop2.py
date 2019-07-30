# Modify Usernames with Range

#这第一个练习是我抄课件做的...

#https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/90abdb2f-ca75-4290-a5db-8942822f9d48


usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(0,4): #此处参考答案： for i in range(len(usernames))  避免使用 magic number(0, 4)
    usernames[index] = usernames[index].replace(' ', '_').lower()
    
print(usernames)



#倒数第二题：for loop 里套 if statement
# string is also a list！
#获取一个list里的element的function： list[]

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0]=='<' and token[-1]=='>':
         count+=1

print(count)



#最后一题：记得用 {}.format()

items = ['first string', 'second string']
html_str = "<ul>\n"  

for item in items:
    html_str+='<li>' + item + '</li>\n' # 参考答案：html_str += "<li>{}</li>\n".format(item)
html_str += '</ul>'
print(html_str)