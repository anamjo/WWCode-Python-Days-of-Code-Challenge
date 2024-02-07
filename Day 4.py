# Write a program to find the sum of all elements in a list.

def sum():
    length = int(input("Enter number: "))
    sum=0
    list_1=list(range(1,length))
    for a in list_1:
        sum=sum+a
    print(list_1)
    return sum

print(sum())




