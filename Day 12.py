# Write a program to reverse a given string.
# Tests Cases:
# 1. Test for an empty string.
# 2. Test string with spaces.
# 3. Test string with no spaces.
input_str=input("Enter a string: ")
if input_str:
    reverse_str=''
    for char in input_str:
        reverse_str=char+reverse_str
    print(reverse_str)
else:
    print("Empty string")


