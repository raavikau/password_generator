import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

letters_count = int(input("How many letters would you like in your password? \n"))
numbers_count = int(input("How many numbers would you like in your password? \n"))

pass_list = []
for i in range(0, letters_count):
    ran_letter = random.choice(letters)
    pass_list.append(ran_letter)
for j in range(0, numbers_count):
    ran_number = random.choice(number)
    pass_list.append(ran_number)

print("Your password is", pass_list)

