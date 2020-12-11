import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"

all = lower + upper + numbers + symbols

length = int(input("Enter length: "))
password = "".join(random.sample(all, length))
print("Your Generated password is : {0}".format(password))
