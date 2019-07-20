#注意每一个 if 和 elif的顺序。只有上一个false，才会往下走。
#https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/5a45f230-6087-4d0e-9e1a-3ddd4fc664e3

points = 174  # use this input to make your submission

# write your if statement here
if points<=50:
    prize='wooden rabbit'
    result="Congratulations! You won a {}!".format(prize)

elif points<=150:
    prize='no prize'    
    result='Oh dear, no prize this time.'

elif points<=180:
    prize='wafer-thin mint'
    result="Congratulations! You won a {}!".format(prize)
    
else:
    prize='penguin'
    result="Congratulations! You won a {}!".format(prize)
    

    
    
    
print(result)