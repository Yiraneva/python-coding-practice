#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  # while x<5 :
  #   print(x)
  #   x= x+1


  # define a for loop
  for x in range(5,10):
    print(x)

  # use a for loop over a collection
  days = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for d in days:
    print (d)
      
 
  # use the break and continue statements
  for x in range(5,10):
    if x==7: 
      break
    print(x)
  
  for d in days:
    if d == "Sat":
      continue
    elif d== "Sun":
      continue
    print(d)

  for rest in days:
    if rest == 'Sat' or rest == 'Sun':
      continue
    print(rest)

  #using the enumerate() function to get index 
  # assignment for ranran
  # print "Today is ___, day _ of the week"
  # ___ is the item, _ is the index
  days = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for i, d in enumerate(days):
    print (i, d)

    # print("Today is", d, ", day", i, "of the week.")
    # print(f'Today is {d}, day {i+1} of the week.')
    print('Today is {}, day {} of the week.'.format(d, i+1))

if __name__ == "__main__":
  main()
