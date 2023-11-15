# f strings in Python

variable_1 = "Boss"
variable_2 = 5
variable_3 = "cat"
print(f"{variable_1} is a {variable_2} year old {variable_3}")


# String functions (upper, lower, strip, capitalize )

print("Winston".upper())

cat_name = "MiLLie"
cat_name_centered = cat_name.center(20,"*")
print(cat_name_centered)
cat_name_new = cat_name.replace("M","W")
print(cat_name_new)
print(cat_name.lower())
print(cat_name.capitalize())

cat_name2 = "        Winston                           " 
print(cat_name2.strip())

# Accessing single characters within a string
### M  i  L  L  i  e  ####
### 0  1  2  3  4  5  ####
### -6 -5 -4 -3 -2 -1 #### 

print(cat_name[2])
print(cat_name[-1])
print(cat_name[-4])
print(cat_name[-6])
# print(cat_name[100000]) #IndexError, also known as out of range error

# Number of occurences of a character in a string
print(cat_name_new.count("L"))
print(cat_name_new.count("l"))
# Example: number of spaces in a string
my_sentence = "The quick brown fox jumps over the lazy dog."
num_spaces = my_sentence.count(" ")
print(num_spaces)

# Accessing multiple characters in a string(slicing)
# syntax possiblities:
# string[start:stop], string[start:], string[:stop]
# string[:], string[start:stop:step], string[::step]
# up to but not including the last index

my_string = "This is a string"
### T  h  i  s   i  s   a   s  t  r  i  n  g ###
### 0  1  2  3 4 5  6 7 8 9 10 11 12 13 14 15

# string[start:stop], string[start:], string[:stop]
print(my_string[2:3])
print(my_string[6:14])
print(my_string[0:16])
print(my_string[0:17]) # No error thrown
print(my_string[0:100000])

print(my_string[8:])
print(my_string[100000:]) # No error, blank line printed

print(my_string[:8])
print(my_string[:1000000])


### T  h  i  s   i  s   a   s  t  r  i  n  g ###
### 0  1  2  3 4 5  6 7 8 9 10 11 12 13 14 15

# string[:], string[start:stop:step], string[::step]

print(my_string[:])
print(my_string[0:12:2])
print(my_string[0:20:2])
print(my_string[::2])
#backward string

print(my_string[::-1])

