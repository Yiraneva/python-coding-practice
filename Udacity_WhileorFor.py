#https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/777f8ccb-f361-43a1-98c4-bf918649bec0



## Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# odd_list = [ ]
# for num in num_list:
#     if num % 2 == 1:
#         odd_list.append(num)
# print(odd_list)

# result=0
# i=0
# while i <= 5-1:
#     result += odd_list[i]
#     i += 1
    
# print(result)


result = 0
count = 0
for num in num_list:
    print(num)
    if num % 2 == 1 and count < 5:
        count += 1
        result += num
    # if count >= 5:
    #     break
# print(result)
# print(count)
print("There are {} numbers added and the sum is {}.".format(count, result))



