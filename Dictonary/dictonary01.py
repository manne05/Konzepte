# Mit sets arbeiten - ein set speichert Variablen gleichen Datentyps
# Deklaration mit geschweiften Klammern {}
# Beispiel 1:
numSet = {1, 2, 3, 4, 5}
print('numSet = ', numSet)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print("Dict 1:",dict1)
print("Dict 2:",dict2)
dict3 = {**dict1, **dict2}

print("merge two dictionaries")
print("Dict 3:",dict3)

# Returns: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Testen, ob ein bestimmter Schlüssel im Dictionary ist.
print('a' in dict3)
print('f' in dict3)
