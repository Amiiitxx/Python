my_dict={"name":"alico","age":25}
my_dict1={"name1":"jhone","age1":25}
#dict1=my_dict.update(my_dict1)
print(my_dict)
print(type(my_dict))
print(my_dict["name"])
my_dict["city"]="america"
print(my_dict)
my_dict["age"]=26
print(my_dict)
del my_dict["name"]
print(my_dict)
print(my_dict.get("city"))
print(my_dict.get("agessss","not found"))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
  

my_dict.update(my_dict1)
print(my_dict)
list1=list(my_dict.values())
list1.append("state")
print(list1)
for x,y in my_dict.items():
   print(x,y)
       
