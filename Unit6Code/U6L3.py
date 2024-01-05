# swapping with tuples

a = 5
b = 10
print(f"a: {a}, b: {b}")

(a,b) = (b,a)
print(f"a: {a}, b: {b}")

# assigning multiple values at once

c,d = 15,20
print(f"c: {c}, d: {d}")

# enumeration

nfc_north = ['Lions','Vikings','Packers','Bears']
for index,team in enumerate(nfc_north):
	print(f"Team {index+1}: {team}")

# limitation of nesting lists and tuples

my_list = [1,2,(3,4)]
print(my_list)
# valid
my_list[1] = -2
print(my_list)
# invalid
# my_list[2][0] = -3 cannot modify tuples like this

# valid
my_list[2] = 3
print(my_list)

my_tuple = (1,2,[3,4])
print(my_tuple)
# invalid
# my_tuple[0] = -1
# my_tuple[2] = [-3,-4]
my_tuple[2][1] = -4
print(my_tuple)


#to-do in CodeHS for homework for Tuesday
# 8.3.6
# 8.3.8
# 8.3.9
