'''
Name: Brandon Smith
Date: 10/10/23
File name: break_continue.py
Description: Shows how to use break and continue in Python

'''

#ask user for positive number, error if not provided
while True:
    user_num = int(input("Enter a positive number: "))
    if user_num > 0:
        break
    print("Error: must be positive")

while True:
    user_num = int(input("Enter a positive number"))
    if user_num < 0:
        print("Error: must be positive.")
        continue
    if user_num == 0:
        print("Error: must be positive")
        continue
    break

for i in range(10):
    print(i, end = '\t')
