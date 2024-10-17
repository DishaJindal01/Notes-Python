# methods
# .join()
# tuple(sorted(tuple_name))                              to sort a tuple
# tuple(sorted(tuple_name,reverse = True))               to reverse a tuple

# empty tuple
t= tuple()
print(t,"\n",type(t))

# tuple("canonot contain more than one argumnet"), use tuple(()) to avoid error
lm= tuple((1,2,3))
print(lm,type(lm))




t = 10,20,20,30
print(type(t))
print(len(t))
print(t)

k= 10
print(type(k),"\n",k)

l= 10,                   # to put a single element in tuple we use coma" , "
print(type(l),"\n",l)


# t[2]=3            immutable
# print(t)

# since its immutable we use type casting to do changes in tuple   list to tuple to list
k= list(t)
k[2]=800
change = tuple(k)
print(change)

# using .join() method
myTuple = ("John", "Peter", "Vicky")

x = "$".join(myTuple)

print(x)

# output:-   John$Peter$Vicky


# REVERSING A TUPLE
a = ( 2, 3, 1)
s = tuple(sorted(a,reverse=True))
print(s)

# SORTIG A TUPLE
a = ( 2, 3, 1)
s = tuple(sorted(a))
print(s)