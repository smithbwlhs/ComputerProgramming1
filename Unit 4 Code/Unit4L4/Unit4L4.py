'''Unit 4 Lesson 4
Review of functions, scope, and learn about
return values'''

# A function that initializes a variable
def e():
    v = 5
    print(v)

# A function that accesses a variable outside its scope
def f():
    print(v)

# A function that accesses more than one variable
# outside its scope
def g():
    print(x + v)

# A function that tries to modify a variable defined
# outside its scope
def h():
    '''v = v + 5 cannot modify global variable
    print(5)'''

#the fix
def j(value):
    return value + 5

def k(value):
    return value*3

#nested functions - beyond scope of class, not on exam

def hi():
    print("Hello ")
    def goodbye(n):
        print("Goodbye "*n)
    return goodbye
# Even/odd function
def even_or_odd(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

####Main Code####
v = 1
x = 2
e() # prints 5
f() # prints 1
g() # print 3
j(v) #calls a function but does nothing with return value
print(j(v)) #prints return value of 6
print(v) #v doesn't change
v = j(v) #this updates v to 6 because the value of j(v) is assigned to v
v = j(v) + k(v) #this updates v to 11 + 18 = 29
print(v)
w = 5
w = j(k(w)) #first k(w) = 15 so j(15) = 20
print(w)
hi()(5) #calls hi with 5 as parameter to the inner function
print(even_or_odd(7))