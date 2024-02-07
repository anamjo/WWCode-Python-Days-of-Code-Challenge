# create a program that swaps the value of two variables.

def swap_var(a,b):
    print("Initial values of a and b are:", a, b)
    x=a  #x=2,a=2
    a=b   #b=3,a=3
    b=x
    print("Final values of a and b are:",a,b)
    return a,b


swap_var(2,3)