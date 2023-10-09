'''
Unit 1 Lesson 4 Homework
Author: Brandon Smith

Problems:

1) Ask the user for the radius of a sphere (could be a decimal number). 
Find and print the volume of a sphere with that radius

2) Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
Shipping costs $3 for the first copy and 75 cents for each additional copy. What is 
the total wholesale cost for 60 copies?

Use a variable to store the number of copies, bookstore’s cost per book, shipping 
for any number of copies, and total cost. Print the total cost on the last line.

'''

#Problem 1

PI = 3.1415

radius = float(input("Enter the radius of the sphere: "))
sphere_volume = (4/3)*PI*pow(radius,2)
print("The volume of a sphere with radius",radius,"is",sphere_volume)

#Problem 2
number_of_copies = 60
cost_per_book = 24.95
discount_cost = cost_per_book * 
shipping_cost = 3 + 0.75*number_of_copies
