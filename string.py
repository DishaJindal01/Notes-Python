# funtion

# len()
# max()
# min()
# type()

# methods in string

# 1  .find(value)                                            return index value or -1(if doesnot  )
# 2  .split()                                                      converts strings to list
# 3  .count()

# methods  to covert a string to another string
# 1  .capitalize()                                                    firsts letter capital
# 2  .replace("old word","new word")
# 2  .replace("old word","",1)                                       replace only first occurance
# 2  .replace(char1, '*').replace(char2, char1).replace('*', char2)    swaping two strings
# 3  .upper()                                                             upper case
# 4  .lower()                                                                   lower case
# 5. .casefold()                                          The casefold() method returns a string where all the characters are lower case.

# methods for testing strings(return bool value)
# 1.       .isalnum()
# 2.       .isalpha()
# 3.       .isspace()
# 4.       .isdigit()
# 5.       .isupper()
# 6.       .islower()
# 7.       .endswith("end word of string")          return bool
# 8.       .startswith()

#methods for formatting strings

# 1.  .center(width)
# 2.  .rjust(width)
# 3.  .ljust(width)
# 4.  .join()

# methods of strit leading and trailing white space characters
# 1.     .lsprit()
# 2.     .rsprit()
# 3.     .strip()





# creating an empty string
s = str()
print(s)
print(type(s))
print(id(s))
s = "hello,python"
print(s)
print(id(s))
# BUILT-IN OPERATORS IN STRINGS
print(len(s))              # using lenght fuction
print(max(s))              # to know the largest alphabetic character
print(min(s))              # to know the smallest alphabetic character
# note:-consider space and symbol as min() space < , <  #

print(s[6])                # indexing
print(s[-4])               # negative indexing
print(s[0:7])              # slicing
print(s[0:len(s):4])       # step size slicing
#print(s[-1:-4])            # negative (backwards) slicing
print(s[::-1])             # reverse printing using slicing



# traversing string with loops:
# 1.for loop:
l = "indians\n"
for ch in l:
    print(ch, end="")
# 2.using while loop:
m = "america\n"
i = 0
while i < len(m):
    print(m[i], end="")
    i += 1

# concatenation '+' '*'
a = "this is python"
b = "programming\n"
print(a + b)
print(a,b)
# using '*'
print(b * 4)

# "in" and "not in" operator
print("is" in a)
print("p" not in b)
# using isspace() bool
c = ""
print(type(c))
print(c.isspace())


# string functions

q = "these are string functions in  in python"

    #1. lenght of string
print(len(q))


    #2 using endswith function
print(q.endswith("java"))
print(q.endswith("python"))

    #3 using find function
print(q.find("shreya"))
print(q.find("are"))

     #4 replace
print(q.replace("python","c++"))
print(q)

      #5 count
print(q.count("o"))
print(q.count("in"))
print(q.count("ri"))

      #6 capitalizing firsts letter
print(q.capitalize())

# escape sequence characters
# \n,  \f,  \r,   \',  \\,  \t

print("hi\ndisha")
print("hello\tpython")
print("what\rhow are you,")
print("great,i need two programs \n\fadditional \n\fsunstraction")
print("addition\\substraction")
print("ok\'z")



# using replace function
letter= '''Dear |Name|,
you are selected!
date: |date|\n'''
print(letter)


name= input("enter your name")
date = input("enter the selection date")

letter = letter.replace("|Name|",name)
letter= letter.replace("|date|", date)
print(letter)


#          using fomating string methods

aq ="hello python"
print(aq)

k0 = aq.center(23)
k1= aq.rjust(100)
k2= aq.ljust(4)
k3= "$".join(aq)                         #  op-  h$e$l$l$o$ $p$y$t$h$o$n

print(k0)
print(k1)
print(k2)
print(k3)


#     USING .swapcase() method

sc ="hello python, its DISHA"
jj= sc.swapcase()
print("swapcase:  ",jj)
print("ORIGNAL:  ",sc)




# methods for testing strings(return bool value)



# 1.       .isalnum()

sp= "hello123there"
sp1=sp.isalnum()
print(sp1)
# note:- couldnot have symbol($%,) or space






# 2.       .isalpha()
al1 ="hellpythonitsdisha"
al=al1.isalpha()
print(al)

#note:- srtring must not have ##anyspace or symbol or number(just all alphabets)





# 3.       .isspace()
ws =" "
ws1 = ws.isspace()
print(ws1)

sw = "\f\t\n\r"
sw1 = sw.isspace()
print(sw1)
# note:- no symbol,number,alphabet(just space)






# 4.       .isdigit()

dig= "1234346789"
dig1=dig.isdigit()
print(dig1)
# note:- cannot have any space symbols,alphabets






# 5.       .isupper()
# 6.       .islower()

al2 ="1this is#upper method "
al3 ="HEL%7LO"
ff1=al2.isupper()
ff2=al2.islower()

ff3=al3.islower()                       #every element should be n lower case
ff4=al3.isupper()                       #every element should be n upper case

print(ff1)
print(ff2)
print(ff3)
print(ff4)

# Note:symbols and numbers doesnot effect the output


#2 using endswith function          also return bool value
print(q.endswith("java"))
print(q.endswith("python"))




# methods of strit leading and trailing white space characters
# 1.     .lsprit()
# 2.     .rsprit()
# 3.     .strip()


txt = "     banana     "
txt1 = ",,,,,,rtyggr,,''#3...banana .    "
right_strip = "               banana               "
left_strip =  "               banana               "


xt = txt.strip()                             # remove spaces from biggning and end of the string
xt1 = txt1.strip(",.rt#3g y'")             # declare all the symbols you want to remove
rsp = right_strip.rstrip()                #remove extra space from right
lsp = left_strip.lstrip()                 #remove extra space from left

print("of all fruits", xt, "is my favorite")
print("of all fruits", xt1, "is my least fav" )
print("of all fruits", rsp, "is my favorite")
print("of all fruits", lsp, "is my favorite")



# using .casefold() method
# program weather harry is present in post or not

post =input("enter a post")
case_sensitive = post.casefold()

if "harry" in case_sensitive:
    print("harry is in the post")
else:
    print("harry is not in the post")



