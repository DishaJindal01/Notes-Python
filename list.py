# # 1. creating  a list and accessing element
# l = [11, 22, 33, 43, 21, "name", "joe"]
# print(l)
# print(l[6])

# # 2. slicing the elements
# print(l[2:7])

# # 3.using '+' operator for connecting two lists and '*' to replicate the elements in list
# m = ["one", "two", 3]
# n = l + m
# print(n)
# print(n[::-1])         # using negative to access elements from backwards

# print(m * 2)           # using * to replicate elements in list

# # 4.using 'in' and 'is' operator on list
# print('1' not in m)
# print("one" in m)
# print("four" in m)

# a = "hello python"
# b = "hello python"
# print(a is not b)
# print(a is b)

# a1 = [1, 2, 3]
# b1 = [1, 2, 3]
# print(a1 is b1)           # we can do changes in the elements of list whereas you can't change strings
# print(a1 is not b1)

# # 5.using "del" operator on list
# del a1[1]
# print(a1)
# del a1[-2]
# print(a1)

# # 6.list comprehensions: it is used to create a new list from the existing list
# com = [20, 30, 40, 50]
# com = [x + 5 for x in com]
# print(com)
# for x in range(0, 4):            # using range
#     com[x] = com[x] + 1
#     print(com)

# # find odd numbers using list comprehensions
# odd =[1,2,3,4,5,6]
# print("contestant list:",odd)
# odd2 =[x for x in odd if x % 2 == 1]
# print(odd2)




# # 7.USING METHODS IN LIST

# # 1. split method ".split()"
# sen = "using split method in list"
# sen.split()
# print(sen)

# # 2.using ".append()" method in list
# mtd = list([10, 20, 30, "forty", 50])
# print(mtd)
# mtd.append("sixty")
# print(mtd)

# # 3.using ".clear()" method in list
# clr =[1,2,3,4,10]
# print(clr)
# clr.clear()
# print(clr)

# # 4.using ".count()" method in list
# c = [1, 6, 6, "six", 8, 5, 1, 6]
# one = c.count(11)                  # shows the no. of times element x appears in list
# two = c.count(1)
# three = c.count("six")
# four = c.count(6)
# print(one)
# print(two)
# print(three)
# print(four)

# # 5. using ".copy()" method on list
# cop =["riya", 21, "sita", 11, "geeta", 1]
# p = cop
# print(p)

# cop2 = [20, 30]
# q = cop2
# print(q)
# cop2[0]= 10
# print(q)

# # 6. using ".extend()" method on list
# states = ["punjab", "haryana", "bihar"]
# countries = ["india", "japan", "usa"]
# states.extend(countries)
# print(states)

# # 7.using ".insert()" method in list
# first = ["india", "japan", "usa"]
# first.insert(1,'20')
# print(first)

# # 8.using "remove()".
# snd = [1, 2, 3, 4, 5, "count", 7, 8]
# print(snd)
# snd.remove(3)          # removing "3" from list of elements
# print(snd)

# # 9.using ".pop()"method in list And USING "del" function on list.
# snd.pop(3)             # pop or deleting element from index 3
# print(snd)
# del snd[1]             # deleting element from index 7
# print(snd)

# # 10.using "sort()" method in list.
# st = [99, 4, 73, 20, 9, 2, 0]
# st.sort()
# print(st)
# name = ["ziyana", "riya", "priya"]
# name.sort()
# print(name)

# # 11.using ".reverse()" method in list.
# rev = [10, 20, 40, 90, 100]
# rev.reverse()
# print(rev)

# # 12. using ".index()" method
# ind =[10, 20, 30, 100]
# print(ind.index(20))             # to know the index of a particular element in list.





# # 8.appling lenght function
# forth =[4, 56, 74, 11]
# print(len(forth))
# ------------------------------------------------
# # funtions in list
# # len()
# # del()          works same as pop (take index value)
# # s = list(sorted(a,key = len))
# # methods of list

# # 1.      .append()         adds element at the end of the list
# # 2.      .insert()        give an index value
# # 3.      .clear()
# # 4.      .copy()
# # 5.      .count()
# # 6.      .extend()
# # 7.      .index()
# # 8.      .reverse()
# # 9.     .remove()
# # 10.     .pop()    , funtion del s[]        work on index value
# # 11.     .sort()
# # 12.     .split()   coverts string to list
# # 13.     .join()






# #create a empty list
# kk=[]
# print(kk)

# l= list()
# print(l)

# # list("canonot contain more than one argumnet"), use list([]) to avoid error
# l = list([1,2,3])
# print(l,type(l))





# # 1. creating  a list and accessing element
# l = [11, 22, 33, 43, 21, "phebe", "joe"]
# print(l)
# print(l[6])

# # 2. slicing the elements
# print(l[2:7])

# # 3.using '+' operator for connecting two lists and '*' to replicate the elements in list
# m = ["one", "two", 3]
# n = l + m
# print(n)
# print(n[::-1])         # using negative to access elements from backwards

# print(m * 2)           # using * to replicate elements in list

# # 4.using 'in' and 'is' operator on list
# print('1' not in m)
# print("one" in m)
# print("four" in m)

# a = "hello python"
# b = "hello python"
# print(a is not b)
# print(a is b)

# a1 = [1, 2, 3]
# b1 = [1, 2, 3]
# print(a1 is b1)           # we can do changes in the elements of list whereas you can't change strings
# print(a1 is not b1)

# # 5.using "del" operator on list
# del a1[1]
# print(a1)
# del a1[-2]
# print(a1)

# # 6.list comprehensions: it is used to create a new list from the existing list
# com = [20, 30, 40, 50]
# com = [x + 5 for x in com]
# print(com)
# for x in range(0, 4):            # using range
#     com[x] = com[x] + 1
#     print(com)

# # find odd numbers using list comprehensions
# odd =[1,2,3,4,5,6]
# print("contestant list:",odd)
# odd2 =[x for x in odd if x % 2 == 1]
# print(odd2)




# # 7.USING METHODS IN LIST

# # 1. split method ".split()"
# sp = "using split method in list"
# k = sp.split()
# print(k)

# # 2.using ".append()" method in list
# mtd = list([10, 20, 30, "forty", 50])
# print(mtd)
# mtd.append("sixty")
# print(mtd)

# # 3.using ".clear()" method in list
# clr =[1,2,3,4,10]
# print(clr)
# clr.clear()
# print(clr)

# # 4.using ".count()" method in list
# c = [1, 6, 6, "six", 8, 5, 1, 6]
# one = c.count(11)                  # shows the no. of times element x appears in list
# two = c.count(1)
# three = c.count("six")
# four = c.count(6)
# print(one)
# print(two)
# print(three)
# print(four)

# # 5. using ".copy()" method on list
# cop =["riya", 21, "sita", 11, "geeta", 1]
# p = cop
# print(p)

# cop2 = [20, 30]
# q = cop2
# print(q)
# cop2[0]= 10
# print(q)


# coy = [1,2,3,55]
# empty =coy.copy()
# print("copied list",empty)

# # 6. using ".extend()" method on list
# states = ["punjab", "haryana", "bihar"]
# countries = ["india", "japan", "usa"]
# states.extend(countries)
# print(states)

# # 7.using ".insert()" method in list
# first = ["india", "japan", "usa"]
# first.insert(1,'20')
# print(first)

# # 8.using "remove()".
# snd = [1, 2, 3, 4, 5, "count", 7, 8]
# print(snd)
# snd.remove(3)          # removing "3" from list of elements
# print(snd)

# # 9.using ".pop()"method in list And USING "del" function on list.(putting index value)
# snd.pop(3)             # pop or deleting element from index 3
# print(snd)
# del snd[1]             # deleting element from index 7
# print(snd)

# # 10.using "sort()" method in list.
# st = [99, 4, 73, 20, 9, 2, 0]
# st.sort()
# print(st)
# name = ["ziyana", "riya", "priya"]
# name.sort()
# print(name)

# # 11.using ".reverse()" method in list.
# rev = [10, 20, 40, 90, 100]
# rev.reverse()
# print(rev)

# # 12. using ".index()" method
# ind =[10, 20, 30, 100]
# print(ind.index(20))             # to know the index of a particular element in list.



# # 13. using .join() method.
# myLIST= ["John", "Peter", "Vicky"]

# xq = "$".join(myLIST)
# print(xq)
# print(type(xq))

# # output:-   John$Peter$Vicky
# #              <class 'str'>



# # 8.using len() lenth function
# ar =[10, 22, 30, 100]
# print(len(ar))


# # progarms from code with harry
# # write names of seven frits in a list take elements from user
# f1 = input("enter fruit 1")
# f2 = input("enter fruit 2")
# f3 = input("enter fruit 3")
# f4 = input("enter fruit 4")
# f5 = input("enter fruit 5")
# f6 = input("enter fruit 6")
# f7 = input("enter fruit 7")
# MY_fruit_list=[f1,f2,f3,f4,f5,f6,f7]
# print(MY_fruit_list)


# # write a program to sum a list with four numbers.
# list=[1,2,3,4]
# x= list[0]+list[1]+list[2]+list[3]
# print(x)

# # sort a list according to the length of the list


# a = ["karan", "a" ]
# sss = list(sorted(a,key = len))
# print(sss)

