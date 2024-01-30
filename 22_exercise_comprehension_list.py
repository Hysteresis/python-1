# Générer une liste de nombre jusque 9 en compréhension list
numbers = [number for number in range(0, 10)]
print(numbers)

# Générer des nombres jusque 9 en boucle for
for i in range(10):
    print(i)

# Générer des nombres jusque 1 million en boucle for. On ne conserve que les nombres impairs
for i in range(1000000):
    if i % 2 != 0 :
        print(i)

# Générer des nombres jusque 1 million en compréhension list. On ne conserve que les nombres impairs
numbers = [number for number in range(1000000) if number % 2 != 0]
print(numbers)
