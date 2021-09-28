import pyautogui
import random
from time import sleep
numbers = input("Количество символов > ")
z = 000000
n = 999999
if numbers == "4":
    z = 0000
    n = 9999
elif numbers == "6":
    z = 000000
    n = 999999
elif numbers == "8":
    z = 00000000
    n = 99999999
elif numbers == "10":
    z = 0000000000
    n = 9999999999
elif numbers == "12":
    z = 000000000000
    n = 999999999999
elif numbers == "14":
    z = 00000000000000
    n = 99999999999999
elif numbers == "16":
    z = 0000000000000000
    n = 9999999999999999
elif numbers == "18":
    z = 000000000000000000
    n = 999999999999999999
else:
    print("Ввелли невозможное количество символов в пароле")
sleep(3)
passwords = list()
while True:
    chars = '+-/|()<>^%№"`_*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = random.randint(z,n)
    password0 = "" 
    for i in range(int(numbers)):
        password0 += random.choice(chars)
    passwords.append(str(password))
    passwords.append(str(password0))
    if password in passwords:
        password = random.randint(z,n)
    if password0 in passwords:
        password0 += random.choice(chars)
    pyautogui.typewrite(str(password))
    pyautogui.press("enter")
    pyautogui.typewrite(str(password0))
    pyautogui.press("enter")
