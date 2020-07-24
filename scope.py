# Zugriff auf die globale Variable x in der Funktion foo1() muss mit 
# global x erfolgen.

x = 5
def foo1():
    global x
    x += 1
    print(x)

print("global x")
foo1()

# Zugriff auf die lokale Variable x der Funktion foo2() in der lokalen Funktion
# bar() muss mit nonlocal x erfolgen. 
def foo2():
    x = 5
    def bar():
        nonlocal x
        x += 1
        print(x)
    bar()

print("nonlocal x")
foo2()


