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