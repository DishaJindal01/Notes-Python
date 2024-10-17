
# methods of set
# .len()
# .remove()
# .pop()
# .clear()
# .union()  - # prints all the element of both the sets(only unique values)
# .intersection()   -# print only common elements
# .add(value to be added)
# .symmetric_difference(vari2)
# .difference(vari2)

#important
# set("canonot contain more than one argumnet"), use .add() to add elements in set


# s.add(["sharan","dipi",23,True]) cannot add list since they are unhashable type
# s.add({"sharan","dipi",23,True})  cannot add  set since they are unhashable type
# s.add({"name":"suman"})           cannot add dictionary  since they are unhashable type


# k= set(123)
# print(k,type(k))
# output:-  TypeError: 'int' object is not iterable



k= set("123456")
print(k,type(k))
# output:-  {'5', '3', '6', '4', '2', '1'} <class 'set'>



# making an empty set

s = set()
print(type(s))
print(s)
s.add(5)
s.add(("sharan","dipi",23,True))
# s.add(["sharan","dipi",23,True])  cannot add list since they are unhashable type
# s.add({"sharan","dipi",23,True})  cannot add  set since they are unhashable type
# s.add({"name":"suman"})           cannot add dictionary  since they are unhashable type
s.add(6)
s.add(24), s.add(1), s.add(100)
s.add(5)                                 # stores unique values
print(s)

# methods
set1 = {1, 2, 3, 4, 1, 22,("sharan", 54)}
print(len(set1))                     # doesnot consider repeatitive values
print(set1)

# using .remove()

set1.remove(("sharan",54))
print(set1)

# using .pop()

set1.pop()                           #removes any random elements since set doenot have any index
print(set1)

k={"sham", 2, 65, 5}
print(k)
k.clear()
print(k)


# using .intersection(),.union method()
ui = {1, 3, 4, 5, 6, 11}
j = {3, 4, 5, 100, 422, 11}
k1 = ui.union(j)                          # prints all the element of both the sets(only unique values)
k2 = ui.intersection(j)                   # print only common elements

print(k1)
print(k2)


# Question from code with  harry .

# 2. write a program to input eight numbers from user and displayonly unique nuumbers.
unique = eval(input("enter  1 number\n"))
unique2 = eval(input("enter 2 number\n"))
unique3 = eval(input("enter 3 number\n"))
unique4 = eval(input("enter 4 number\n"))
unique5 = eval(input("enter 5 number\n"))
unique6 = eval(input("enter 6 number\n"))
unique7 = eval(input("enter 7 number\n"))
unique8 = eval(input("enter 8 number\n"))


k = unique,unique2,unique3,unique4,unique5,unique6,unique7,unique8
s = set(k)
print(s)
# or

# k = {unique,unique2,unique3,unique4,unique5,unique6,unique7,unique8}
# print(k)


# 3. can we have a set with 18 as integer and with 18 as string.

s = eval(input("enter a number in string"))
n = eval(input("enter a number"))

sn = s, n
comb = set(sn)
print(comb)

# 4. what will be te length of following string om:
# om = set()
# om.add("20")
# om.add(20)
# om.add(20.0)
om = set()
om.add("20")
om.add(20)
om.add(20.0)
print(len(om),"\n",om)