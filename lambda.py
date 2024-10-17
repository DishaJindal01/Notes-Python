# also called  anonymous function

# called anonymous because they are declared in standard manner using def

# used where the functions obj re required


# adding 3 numbers
x= lambda a,b,c : a + b + c
print(x(10,20,30))

# # cube
c = lambda a: a ** 3
a = int(input("enter: "))
print(c(3))

# lambda expressions

def fun(a):
    return lambda n : a * n
call_fun = fun(2)
print(call_fun(3))
print(call_fun)
