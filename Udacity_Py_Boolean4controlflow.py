points = 174

if points <= 50:
    prize = "wooden rabbit"
elif points <= 150:
    prize = None
elif points <= 180:
    prize = "wafer-thin mint"
else:
    prize = "penguin"

if points:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)