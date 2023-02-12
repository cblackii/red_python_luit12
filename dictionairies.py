import random
var = {}

print(var)
print(type(var))

var2 = {"fruit": "apple", "juice":"cranbery", "food":"spaghetti"}

print(var2) #Key then Value Associated

for k, v in var2.items():
    print(k, v)
    
    var2["drank"] = "petron"
    print(var2)
    
    var2["fruit"] = "grape" 
    print(var2)
    
    var2["fruit"] = ["apple", "grape"]
    print(var2)
    print(var2["fruit"][0])
    
    print(list(var2.keys()))
    print(list(var2.values()))
    
    print(dir(var2))
    
    dict_of_dict = [[random.randint(0,10) for i in range(5)] for j in range(5)]