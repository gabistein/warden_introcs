# flow of control 
# siimple if statement
x = 5
if x > 0: # <conditional> <boolean expression> :
    print("x is positive")

#Example 2
animal = input("What is your favorite animal?")
if (animal == 'cat') or (animal == 'dog'):
    print("A great pet!")
else: # No boolean expression every other case falls here
    print("Good choice")

# Example 3, elif 
if animal == 'cat':
    print("i love cats")
elif animal == 'dog': # has to come after if 
    print('I have a pet dog')
elif animal == 'rat':
    print('i want a pet rat')
else:
    print('good choice')