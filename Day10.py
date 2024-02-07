# Write a program to remove duplicates from a list.

#Method 1
def remove_dup():
    list_1=[]
    unique_list=[]
    length_list=int(input("Enter number: "))
    for a in range(length_list):
        user_input=int(input(("Enter number: ")))
        list_1.append(user_input)
    for ele in list_1:
        if ele not in unique_list:
            unique_list.append(ele)
    return unique_list,list_1
print(remove_dup())


