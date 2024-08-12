## IMPORTS
import time



## -----------------------------------------

## Starting + Questions
print("Starting")
time.sleep(2)
user = input("Enter your username: ")
time.sleep(1)
password = input("Enter the password: ")
print("Processing Request")

## USER LOGIC
if user == "Downhillgfx" or user == "downhillgfx":
    print("Username confirmed.")
else:
    print("Incorrect Username")

## PASSWORD LOGIC
if password == "test123123":
    print("Password Confirmed")
else:
    print("Incorrect Password")

time.sleep(2)

# Loop Space
for i in range(2):
    print("-------------------------")

# Granted Access
if password == "test123123" and (user == "Downhillgfx" or user == "downhillgfx"):
    print("Granted Access")
else:
    print("GET OUT")
