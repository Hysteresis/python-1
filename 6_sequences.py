# Les séquences
my_string = "Hello world !"

len(my_string)

# .split()
my_list = my_string.split('o')
# print(my_list)

#  .append() ajouter un dernier élément au tableau

#  .pop() supprime le dernier element de la liste

# .reverse() changer l'ordre des éléments de la liste
# ajouter 2 liste
# print(my_list + my_list)

# Tuple
# pourquoi tuple : protège les éléments de ma liste : immuable, on ne peut pas modifier les éléments de la lsite
# tuple(my_list)

my_tuple = ('1', '2', 5)
# print(my_tuple.pop()) # AttributeError: 'tuple' object has no attribute 'pop'

# Afficher de index 1 => dernier
my_list[1:]

my_list[::2]
my_new_list= []

# TODO syntax  my_new_list = [*range(100)]
my_new_list = [*range(100)]
# print(my_new_list)

# TODO comprehension list : [number**2 for number in range(100)]
# print([number**2 for number in range(100)])


# y = ax + b
# x = Surface de la maison
# a = 7.5
# b = 1.5
# y = Prix de la maison

# Votre mission, calculer y pour toutes les maisons allant de 20m² jusque 50m2

# print([7.5 * surface + 1.5 for surface in range(20, 51)])


prices = {}

#
# def calculate_price(range1, range2):
#     for surface in range(range1, range2 + 1):
#         price = 7.5 * surface + 1.5
#         prices.update({surface: price})
#     return prices

# def calculate_price(range1, range2):
#     prices = {surface: 7.5 * surface * 1.5 for surface in range(range1, range2)}
#
#     return prices
#
#
# print(calculate_price(20, 50))


# print([surface * 2 for surface in range(0, 20)])

# TODO Créer une liste des carrés des nombres de 0 à 9.
# squares = [i * i for i in range(0, 10)]
# print(squares)

# TODO Filtrer les nombres pairs d'une liste.
# numbers = [i for i in range(0, 10)]
# filter_pair = [pair for pair in numbers if pair % 2 == 0]
#
# print(filter_pair)

# Utilisez une compréhension de liste pour créer une nouvelle liste
# contenant la longueur de chaque mot dans la liste `words`.
words = ["python", "programming", "is", "fun"]
length_words = [len(word) for word in words]
print(length_words)


# Utilisez une compréhension de liste pour créer une nouvelle liste
# contenant les nombres pairs de la liste `numbers`, mais multipliés par 2.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_numbers = [number * 2 for number in numbers if number % 2 == 0]
print(double_numbers)

# words = ["apple", "banana", "orange", "grape", "avocado"]
# Utilisez une compréhension de liste pour créer une nouvelle liste
# contenant les mots de la liste `words` qui ont une longueur supérieure à 3 caractères
# et qui commencent par la lettre "a".

# new_lists = [word for word in words if len(word) > 3 and word[0] == "a"]
# print(new_lists)


phrases = ["Hello World", "Python is AWESOME", "Programming is fun", "Hello again"]
# Utilisez une compréhension de liste pour créer une nouvelle liste
# contenant les mots uniques (distincts) de toutes les phrases, en lettres minuscules.
# unique_words = list(set(word.lower() for phrase in phrases for word in phrase.split()))
unique_words = set(["a", "a", "a"])
# print(unique_words)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Utilisez une compréhension de liste pour créer une nouvelle liste
# contenant les carrés des nombres impairs de la liste `numbers`.
list_numbers = [number**2 for number in numbers if number % 2 != 0]

words = ["apple", "banana", "orange", "grape", "kiwi", "pear"]
# Utilisez une compréhension de liste pour créer une nouvelle liste
# contenant les mots de la liste `words` qui ont une longueur paire
# et qui commencent par une voyelle.
new_words = [word for word in words if len(word) % 2 == 0 and word[0] in "aeiouy"]
# print(new_words)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Utilisez une compréhension de liste pour créer une nouvelle liste
# contenant les carrés des nombres pairs et les cubes des nombres impairs de la liste `numbers`.

number_lists = [number**2 if number % 2 == 0 else number**3 for number in numbers]
print(number_lists)

words = ["python", "programming", "is", "fun"]
# Utilisez une compréhension de liste pour créer une nouvelle liste
# contenant les mots inversés de la liste `words`.

# new_words = [''.join(reversed(word)) for word in (words)]
# print(new_words)

phrases = ["Python est génial", "Les compréhensions de liste sont puissantes", "Programmer est amusant"]
# Utilisez une compréhension de liste pour créer une nouvelle liste
# contenant la longueur de chaque mot dans chaque phrase, mais uniquement si la longueur est supérieure à 2.

new_phrases = [len(word) for phrase in phrases for word in phrase.split() if len(word) > 2]
# print(new_phrases)

phrases = ["Python est un langage puissant", "Les list comprehensions sont utiles", "Programmer est une compétence précieuse"]
# Utilisez une compréhension de liste pour créer une nouvelle liste
# contenant la première lettre de chaque mot dans chaque phrase, à condition que le mot ait une longueur supérieure à 2.
new_phrases = [word[0] for phrase in phrases for word in phrase.split() if len(word) > 2]
