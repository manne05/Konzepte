# Ändern einer Liste während der Iteration? 
# - eine denkbar schlechte Idee, da dann auf Elemente zugegriffen wird,
#   die nicht mehr vorhanden sind.
def odd(x): return bool(x % 2)
numbers = [n for n in range(10)]
for i in range(len(numbers)):
    if odd(numbers[i]):
#       del numbers[i] -- das gibt einen list index out of range Fehler 
        print(numbers[i])

# so funktionierts dann
numbers[:] = [n for n in numbers if not odd(n)]
print(numbers)
