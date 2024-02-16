import random
import string
import csv
import os

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))
num_passwords = int(input("Enter the number of passwords to generate: "))

file_exists = os.path.isfile('passwords.csv')

with open('passwords.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(['Username', 'Password',"No. of Chacacters"])
    for _ in range(num_passwords):
        username = input("Enter the username: ")
        password = generate_password(length)
        writer.writerow([username, password,length])
        print(f"Password for {username} is {password}.")
        print(f"Password for {username} saved successfully.")

print("All passwords saved in passwords.csv file.")
