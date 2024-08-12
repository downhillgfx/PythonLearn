import time

print("Starting")
time.sleep(2)
user = input("Enter your username: ")
time.sleep(1)
password = input("Enter the password: ")
print("Processing Request")
if user == "Downhillgfx":
    print("Username confirmed.")
else:
  print("Incorrect Username")
if user == "test123123":
  print("Password Confirmed")
else:
  print("Incorrect Password")

time.sleep(2)
