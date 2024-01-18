# Les types de données
type(1)
print(type(1))

# Les nombres flottants
type(1.01)
my_round = round(1.025441, 3)
print(f"my_round est arrondi avec 3 chiffres après la virgule {my_round} ")

print(type(1.01))

# Les booléens
type(True)
type(False)

print(type(True))
print(type(False))

# Les séquences
# # Les listes
my_list = ['one', 'two', 'three']
print(my_list)

# # les Tuples
one_tuple = ('one', 'two', 'three')
print(one_tuple)

# # Les sets
one_set = {'one', 'two', 'three'}
print(one_set)

# # les item
# Dictionary
my_dict = {"key": "value"}
print(my_dict)
print("\n\n\n\n\n")


# par rapport à 11h30
date = "18 janvier 2024"

print("**************************")
print(f"* Date : {date} *")
print("**************************")

# Nombre de minutes écoulées depuis minuit jusque 11h30
minute = 11 * 60 + 30
print(f"\n- {minute} minutes écoulées depuis minuit jusque 11h30 ")

# Pourcentage de minutes restantes dans la journée
remaining_minutes = round((24*60 - 12*60 - 30)/(24*60)*100, 1)

print(f"- Pourcentage de minutes restantes dans la journée : {remaining_minutes}")

# Est que le nombre de minute écoulée est pair ou impair
is_even = minute % 2

# Verfier avec la condition if...else si is_even est pair ou impaire
if is_even == 0:
    print(f"\n- le nombre de minute écoulée est pair : {minute}")
else:
    print(f"\nle nombre de minute écoulée est impaire : {minute}")

