import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num_letters = int(input("How many letters would you like in your password? \n"))
password = ''
for _ in range(1, num_letters+1):
    ran_letters = random.choice(letters)
    password+= ran_letters
print("Your password is", password)
