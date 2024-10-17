# dictionary is unordered
# cannot have duplicate key that is one name cannot be assigned to two keys
# if new keys name match the existing key the value of new key will overide the value of exiting key
# values of two keys can be same unlike keys themselves

# methods
# .keys()
# .items()
# .values()
# .get()
# .update()

# making a dictionary
d = {"name":"zoya", "rollno":"28","nested":{"palak":"ludhiana"},"number":23,"list":[1,2,3],"tuple":(1,22,3),"set":{88,"sharan"}}
print(d["name"])
print(d["rollno"])
print(d["list"])
print(d["tuple"])
print(d["tuple"])
print(d["number"])
print(d["set"])
                   # nested dictionary
print(d["nested"])
print(d["nested"]["palak"])


# its mutable
d["number"]=66
print(d["number"])
d["list"]=[35,1,76]
print(d["list"])


# methods in dictionary
d = {"name":"zoya",
     "rollno":"28",
     "nested":{"palak":"ludhiana"},
     "number":23,
     "list":[1,2,3],
     "tuple":(1,22,3),
     "set":{88,"sharan"},
      1:2}

# print all the keys in a form of list
print(d.keys())
print(type(d.keys()))                           # datatype dict_keys

print(list(d.keys()))                           # typecasting from dict_keys to list

# print all the values in a form of list
print(d.values())
print(type(d.values()))                            # datatype dict_values

# print all the items in a form of tuple
print(d.items())
print(type(d.items()))                            # datatype dict_items



# we can print dictionary using 2 ways
# 1. print(dictionary_name["key_name"])
# 2.print(dictionary_name.get("keyname"))
print(d.get(1))
print(d.get("nested"))

# note:- .get() method will not through error if the given key is not in the declared dictionary it will return None
# whereas print(dictionary_name["key_name"]) will through error if the given name is not in declared dictionary.
# hence we use .get()method usually.for example:-

# print(d.get("section"))
# print(d["section"])

# using.update() method

new = {"language": 20, "zodiac":"scorpio"}
update_dic = {"year" : "2020","month":"november"}
new.update(update_dic)
print(new)
new.update({"era": "cen10"})
print(new)



# Question from code with  harry .


# 1. create  a dictionary with hindi words which have values of english translation,provide user with an option to look it up.

first_dict = {"kahan" : "where",
                1 :      "two",
              "kab" : "when",
              "kese" : "how",
              "kya" : "what",
              22: "bhai",
              "list":[12,33, 44]}

print("options are: ",list(first_dict.keys()))
I = first_dict.get(eval(input('enter your word use ""\n')))
print(I)
#or u can use
# print(first_dict[eval(input("enter your world use''"))])


# 5,6. make an empty dictionary allow your four friends to ente there fav language as values.use there unique names as keys.

w={}
print(type(w))

w ={"karan":input("enter your fav language karan"),
    "ram":input("enter your fav language ram"),
    "mehak":input("enter your fav language mehak"),
    "diya":input("enter your fav language diya"),         #when two friends have same fav language
    "ram": input("enter your fav language ram")}  # this rams input value will override the value of exiting ram

print(w)

# or


# w={}
# a = input("enter your fav language")
# b = input("enter your fav language")
# c = input("enter your fav language")
# d = input("enter your fav language")
# w["karn"]=a
# w["ram"]=b
# w["disha"]=c
# w["karn"]=d
# print(w)
# print(len(w))











'''
how to find lenght of dictionary?
how to use the update method in dictionary?
how to change the code in dictionary?
how to set a default value to a key?
how you can have multiple values to a single key?
try pop, del, clear, pop item
how to find weather a key exit in dictionary or not?
'''
d = {}
print(type(d))
d ={'a':10, 'b':20}
print(d)
print(d.keys())
print(d.values())
print(d.items())

print(len(d))            # FIRST ANSWER

d1 = {'c':[25,35], 'd':11}    # sixth answer
print(d1)

#copy one dictionary to other using update
d.update(d1)                      # second ans
print(d)

