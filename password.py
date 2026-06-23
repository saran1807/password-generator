import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
special=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']
password=[]
total=int(input("Enter the length of the password :"))
char=int(input("Enter the number of letters to be in your password :"))
number=int(input("Enter the number digits to be in your password :"))
special_characters=int(input("Enter the number of special characters to be in your password :"))
if total<(char+number+special_characters):
    print("Your Total characters is lesser than the info given.")
    exit()
for length in range (1,char+1):
    password.append(random.choice(letters))
for length in range (1,number+1):
    password.append(random.choice(numbers))
for length in range (1,special_characters+1):
    password.append(random.choice(special))
random.shuffle(password)
password_string=""
for char in password:
    password_string+=str(char)
print(f"Your Password is : {password_string}")