import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '*', '+', '(', ')']

print("Welcome to the Password Generator!")
letters_count = int(input("How many letters would you like in your password? "))
numbers_count = int(input("How many numbers would you like in your password? "))
symbols_count = int(input("How many symbols would you like in your password? "))

pass_list = []
for _ in range(0, letters_count):
    ran_letter = random.choice(letters)
    pass_list.append(ran_letter)
for _ in range(0, numbers_count):
    ran_number = random.choice(number)
    pass_list.append(ran_number)
for _ in range(0, symbols_count):
    ran_symbol = random.choice(symbols)
    pass_list.append(ran_symbol)
random.shuffle(pass_list)

password = ""
for word in pass_list:
    password += word
print("Your password is: ", password)
