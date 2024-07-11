roman_str = input("Enter Roman Number: ")

roman = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

num = 0

roman_str = roman_str.replace("IV","IIII")
roman_str = roman_str.replace("IX","VIIII")
roman_str = roman_str.replace("XL","XXXX")
roman_str = roman_str.replace("XC","LXXXX")
roman_str = roman_str.replace("CD","CCCC")
roman_str = roman_str.replace("CM","DCCCC")
my_str = list(roman_str)
for char in my_str:
    num = num + roman[char]

print("Integer Value is: ",num)