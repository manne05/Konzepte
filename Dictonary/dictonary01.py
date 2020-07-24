dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print("Dict 1:",dict1)
print("Dict 2:",dict2)
dict3 = {**dict1, **dict2}

print("merge two dictionaries")
print("Dict 3:",dict3)

# Returns: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
