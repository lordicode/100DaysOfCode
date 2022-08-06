import os
import random
import csv

print("Welcome to the password generator!")
print("It can generate and store the passwords for each service!\n")
# get the name of the service to generate and save password for
service = input("What is the site?")
# how long you want you password to be? Will give a warning if less <= 8
length = int(input("How long do you want the password to be?"))
# TODO: <= 8 symbols warning and logic

# generates a random string of 1024 bytes that is cryptographically secure
secure_string = str(os.urandom(1024))
# array of all characters you don't want to see on a password, can be expanded, but it will make the password less secure
disallow_characters = ["\\", " ", "x"]
# remove \ because it will appear too often and predictably
for char in disallow_characters:
    secure_string = secure_string.replace(char, "")
# cut the string
start = random.randint(0, int(len(secure_string) / 2))
end = start + length
resulting_password = secure_string[start:end]
print(f"You password for {service} is: ", resulting_password)

header = ['service', 'pwd']
data = [service, resulting_password]
with open("list.csv", 'a') as append_file:
    writer = csv.writer(append_file)
    writer.writerow(header)
    writer.writerow(data)

print("All data is written successfully!")
