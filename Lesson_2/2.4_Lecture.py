# Our lists can be any type, the values in a list are elements or items
# Syntax for the list: <variable_name> = [<item>, . . . , <item>]
# all items within our list are the same 
# len(<list>), gives us the length of the list 
# Index, the spot where each element in our list, list[0]-gives 0 element
# When you try to get an element but the list is not long enough, you will index out of bound error
a_list = [1,2,3]
# print(a_list[5])
# Nested  Lists:
a_list = ['a', 'b', 'c', ['d', 'e']]
print(len(a_list[3]))

#Examples

list_1 = [1, 2, 3, 4, 5, [9,10,11]]

# How do I print the first element of the list? 
# print(<list name>[#])
print(list_1[0])

# How to get the length of the nested list?
print(len(list_1[5]))

# How do I get the 2nd element in the nessted list? 
print((list_1[5])[1])

a_list = ['a','b','c','d','e']
print(a_list[len(a_list)-6])