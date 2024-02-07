# Write a function to count the number of vowels in a given string.

def count_vowels():
    str1="this is an owl"
    count=0
    for a in str1:
        if a=="a"or a=="e" or a=="o" or a=="i"or a=="u":
            count=count+1
    return count

print(count_vowels())