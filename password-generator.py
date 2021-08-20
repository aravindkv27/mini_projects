import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# random_letters=random.randint(0,nr_letters+1)
# print(letters[random_letters])

random_letters=random.sample(letters,nr_letters)
random_numbers=random.sample(numbers,nr_numbers)
random_symbols=random.sample(symbols,nr_symbols)

password=random_numbers+random_letters+random_symbols

#f_password=''.join(password)
#final_password=list(f_password)

random.shuffle(password) #shuffling a list using random.shuffle function. 
print(''.join(password))  #converting the list into string using list comprehension.