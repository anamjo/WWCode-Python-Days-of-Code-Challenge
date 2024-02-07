# Write a program to print the multiplication table of a given number.

def multiplication():
    try:
        user_input=int(input("Enter the number: "))
        if user_input==0:
            raise ValueError("Error: user_input can't be 0")
        n=int(input("Enter the number till you want the table: "))
        if n==0:
            raise ValueError("Error: n can't be 0")
        for a in range(1,n+1):
            result=a*user_input
            print (result)
    except ValueError as ve:
        print(ve)
print(multiplication())

