#https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/cdf7d89f-d9a4-4e3b-ac64-cfca225d37fb

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for item in basket_items:
    if item in fruits:
        fruit_count += basket_items.get(item)
     
    if item not in fruits:
        not_fruit_count += basket_items.get(item)

#if the key is in the list of fruits, add to fruit_count.

#if the key is not in the list, then add to the not_fruit_count


print(fruit_count, not_fruit_count)