import time

loading = ['\\', '|', '/', '-']
        
input = input("You tryna load?")

if input == "yes" :
    for char in loading:
        print(f'\r{char}', end='')
        time.sleep(0.1)    
else:
    print("You're not tryna load damn.")

