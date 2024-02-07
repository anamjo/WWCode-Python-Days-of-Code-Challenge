# Write a program to check if a number is even or odd.

def odd_even(num):
    try:
        num=int(num)
        if num%2==0:
            print("{} is even".format(num))
        else:
            print("{} is odd".format(num))
    except ValueError:
        print("Error: Please enter a valid integer.")



user_input=input("ENter a number: ")
odd_even(user_input)
