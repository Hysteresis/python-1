# Les blocs conditionnels
if 1 == 2:
    print("1 est egal a 2")
elif 1 == 1:
    print("1 est egal a 1")
else:
    print("1 n'est pas egal a 1")

# les conditions :
# 1 == 1
# 1 <= 1
# 1 >= 1
# 1 != 2
# 1 in [1, 2, 3, 4]
# 1 not in [1, 2, 3, 4]
# True or False

# avec import numpy
if ~(1 == 1):
    print("test")
else:
    print("not ok")

# (1 == 1) or (1 == 2)
# (1 == 1) | (1 == 2)
#
# (1 == 1) and (1 == 2)
# (1 == 1) & (1 == 2)

# (1 == 1) and ~(1 == 2)
# (1 == 1) & (1 == 2)

match 'A':
    case 'B':
        print('Cette lettre est un B')
    case 'A':
        print('Cette lettre est un A')


# Créer une fonction qui vérifie la lettre entréé par l'utilisateur est une voyelle

letter_entry = input("Saisir une lettre : ")

match str(letter_entry):
    case 'a':
        print('Cette lettre est un a')
    case 'e':
        print('Cette lettre est un e')
    case 'i':
        print('Cette lettre est un i')
    case 'o':
        print('Cette lettre est un o')
    case 'u':
        print('Cette lettre est un u')
    case 'y':
        print('Cette lettre est un y')
    case _:
        print(f"Cette lettre {letter_entry} n'est pas une voyelle")
