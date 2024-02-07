# Write a program to check if a number is positive, negative, or zero.

def num_check(num):
    if num>0:
        print("{} is postive".format(num))
    elif num<0:
        print("{} is negative".format(num))
    else:
        print("{} is equal to 0".format(num))
num_check(0.0)