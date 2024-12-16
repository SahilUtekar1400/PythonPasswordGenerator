import random

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&", "*", "-", "_"]

print("Welcome to our simple python password generator!")
nr_letters = int(input("How many letters do you want in your password?"))
nr_symbols = int(input("How many symbols do you want in your passwords?"))
nr_numbers = int(input("How many numbers do you want in your password?"))

password_list = []

for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))

for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for chars in password_list:
    password += chars

print(password)