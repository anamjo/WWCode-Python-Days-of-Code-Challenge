# Write a program to count the occurrences of a specific character in a string.
import random
str_1=input("ENter string: ")
char=random.choice(str_1)
count=0
for a in str_1:
    if a==char:
        count=count+1
print("No.of occurences of ",char,"is",count)

