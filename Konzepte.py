# Wichtige Dinge in Python
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(list_)

# for Schleife
for element in list_:
    print(element)

# lambda - eine einzeilige Funktion für einmaligen Gebrauch
square_func = lambda z: z ** 2
is_odd = lambda z: z%2 == 1
multiply = lambda x,y: x*y

# list - eine Liste mit der Funktion list automatisch erzeugen
aList = list(range(10))
print(aList)
# Zugriff auf das letzte Element der Liste
print(aList[-1])
# Zugriff auf einen Teil der Liste
print(aList[2:5])
# Liste umdrehen - reverse
print(aList[::-1])
      
y = 3

# list comprehension ist eine prägnante und flexible Methode zur Erstellung
# von Listen aus anderen Listen mit flexiblen Ausdrücken und Bedingungen.
# Sie wird durch eine eckige Klammer konstruiert, mit einem Ausdruck oder einer
# Funktion, die auf jedes Element in einer Liste nur dann angewendet wird, wenn
# das Element eine bestimmte Bedingung erfüllt. Sie kann auch verschachtelt
# werden, um verschachtelte Listen zu handhaben, und ist weitaus flexibler als
# die Verwendung von map und filter.
# Syntax of list comprehension
# [ expression(x) for x in aList if optional_condition(x) ]

# Beispiel mit map - Funktion
print('Beispiel mit map - Funktion')
print(list(map(square_func, aList)))
# print(list(map(multiply, aList, y)))

# Beispiel mit list comprehension
print('Beispiel mit list comprehension')
print([x ** 2 for x in aList])
print([x * y for x in aList])

# Beispiel mit filter - Funktion
print('Beispiel mit filter - Funktion')
print(list(filter(is_odd, aList)))

# Beispiel mit list comprehension
print('Beispiel mit list comprehension')
print([x for x in aList if x%2 == 1])

