from os import system, name
import time


def clear():
    # Win
    if name == 'nt':
        _ = system('cls')
    # GNU Linux, Unix, and etc.
    else:
        _ = system('clear')

clear()
num = input("Please enter your decimal here: ")
bin = 0
divisionControl = int(num)

total = []
# Error handler
if (int(num) < 0):
    print("This is not a positive number.\n")
# Yes this is not a positive number but it can still be convertible to binary number system.
# Calculate
for i in range(1,99):
    bin = int(divisionControl) % 2
    divisionControl = int(divisionControl) // 2
    if(int(divisionControl) == 0):
        break
    total.append(str(bin))
# Reverse Numbers
total.reverse()
#Output
clear()
print("Your input decimal is ", num)
print("Your binary is ")
print("1", end="", sep="")
for i in total:
    print(str(i), sep="", end="")
# Place list datas
print()
time.sleep(3)
exec(open('Binary_Calculator.py').read())


