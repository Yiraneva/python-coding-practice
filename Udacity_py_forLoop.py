

#知识点：
# .append list
# .replace list
# .lower string

# https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/5c057e68-4556-4f47-885b-1c964003df27


#https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/90abdb2f-ca75-4290-a5db-8942822f9d48


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames=[]

# write your for loop here
for name in names:
    usernames.append(name.replace(' ','_').lower())
    
print(usernames)
    

