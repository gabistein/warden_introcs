# Game show
prizes = ['car', 'vacation', 'kitchen appliance', '$100', 'boat', 'bike', 'truck']
n = input('Pick a number 0 - 9 to get a prize \n')
print(prizes[int(n)])

# Quiz
food = ['donuts', 'pancakes', 'bacon', 'waffles', 'eggs', 'bagels']
score = [0,0,0,0,0,0]

print('Please answer each question with "y" for "yes" and "n" for "no".')
user_input = input('Do you like food with holes? \n')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

user_input = input('Do you eat meat? \n')
if user_input == 'y':
    score[2] = score[2] + 1

user_input = input("Do you like sweet things? \n")
if user_input == 'y':
    score[0] = score[0] + 1
    score[1] = score[1] + 1
    score[3] = score[3] + 1 

#Find the winning item
max = max(score)
max_index = score.index(max)
print(food[max_index])
# Add remaining questions here, and adjust scores similar to the above.