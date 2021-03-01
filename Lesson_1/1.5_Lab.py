#Debugging Activity
# Change int function to be interpretting string of int
# When changing var name, change symbol so change in whole program 
# Casting int -> str, have to concatenate two strings, not string and int

favorite_number_str = input("What is your favorite number: ")
birth_month_number_str = input("What month number where you born in: ")
lucky_number = int(favorite_number_str) + int(birth_month_number_str)
lucky_number_str = str(lucky_number)
print("Your lucky number is " + lucky_number_str) # TypeError: can only concatenate str (not "int") to str
