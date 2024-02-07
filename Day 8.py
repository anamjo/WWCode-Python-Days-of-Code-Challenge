# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def upper_lower(str_1):
    count_u=0
    count_l=0
    for a in str_1:
        if a.islower():
            count_l=count_l+1
        elif a.isupper():
            count_u=count_u+1
    return count_l,count_u
str_1=input("Enter string: ")
print(upper_lower(str_1))

# Alternate Solution with dictionary

def upper_lower(str_1):
    count_dict={"uppercase":0,"lowercase":0}
    for a in str_1:
         if a.islower():
             count_dict["lowercase"]=count_dict["lowercase"]+1
         elif  a.isupper():
             count_dict["uppercase"]=count_dict["uppercase"]+1
    return count_dict

print(upper_lower("AARohi"))


# count_dict={"uppercase":6,"lowercase":8}
# print(count_dict["uppercase"])