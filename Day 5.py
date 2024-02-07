# Write a program to find the maximum and minimum values in a list.

# def sum():
#     length = int(input("Enter number: "))
#     if length==0:
#         list_1=list(range(1,length))
#     return max(list_1),min(list_1)
# print(sum())


def min_max():
    length=int(input("Enter number: "))
    count=0
    list_1 = []
    while count<length:
        x=float(input("ENter numbers: "))
        list_1.append(x)
        count=count+1
    return max(list_1),min(list_1)
print(min_max())