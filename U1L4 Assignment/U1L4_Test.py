import math

def volume_test():
    assert round(a_sphere,1) == 523.6, "Should be 523.6"
    print("Correct volume")

def book_test():
    assert round(tc,2) == 945.45, "Should be 945.45"
    print("Correct total cost")

###############PUT THEIR CODE HERE########################

#EXERCISE 1 
PI=3.1415

r_sphere=float(input("please enter the radius of the sphere. "))
a_sphere=PI * pow(r_sphere,3) * 4/3
print("the area of the sphere is", a_sphere)


#EXERCISE 2
cpb=24.95*0.6
#cpb is abbreviated for cost per book
noc=60
#noc is abbreviated for number of copies
shipping=(noc-1)*0.75+3
tc=round(shipping+cpb*60,2)
#tc is abbreviated for total cost
print("the total cost is", tc)


############################################################

if __name__ == '__main__':
    volume_test()
    book_test()
    print('All tests passed')