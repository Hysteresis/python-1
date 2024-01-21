import pandas as pd

my_dict = {'one': 'un', 'two': 'deux'}
my_dict.items()

# clé et valeur .items()
for key, value in my_dict.items():
 print(f"Key: {key}, Value: {value}")

# juste les cles .keys()
for key in my_dict.keys():
 print(f"Key: {key}")

# juste les valeurs .values()
for value in my_dict.values():
 print(f"Valeur: {value}")

# comprehension dictionnaire
print({key: value for key, value in my_dict.items()})

# fonction zip
list1 = ('Oeuf', 'Lait', 'Sucre')
list2 = ('Sucre', 'Farine', 'Huile')
dict(zip(list1,list2))
print({(key, value) for key, value in zip(list1,list2)})

# unpacke un var directement sur le contenu du dico
one, two = [1, 2]
print(one)
print(two)

# a partir le la liste des entreprises
# créer une liste qui contient uniquement le premier mot
# créer une liste qui contient la longueur du premier mot
# créer une liste qui contient des tuples et sa position dans la liste originale

company_names = [
 'All For Bikes',
 'Amaze Bikes Inc',
 'Arena Sports Inc',
 'Atlanta Corp Inc',
 'Bike World Inc',
 'Alpha AG',
 'BuchungsKreis 1010',
 'Trek Cycle AG',
 'Tona Bikes AG',
 'Meine Bicycle',
 'Avante Grande Bikes',
 'Bike On',
 'Carefree Cycles',
 'G&M Bicycle',
 'Keep Cycling',
 'iCare Australia',
 'CC SportWorld',
 'DigiPay',
 'TechCycle Canberra',
 'eBike 100',
 'Cycle World',
 'High Tech Sports Inc',
 'Tires On Fire',
 'MX Bike',
 'FitnessWorld',
 'Homerun Millwork Inc.',
 'Antonio Bandolera',
 'Khan Cycles',
 'Palm Beach Bike World',
 'A to Z Fitness',
 'Hudson SportsTec',
 'Ebike 36',
 'Wichita Sport',
 'Move by Bike',
 'TechCycle',
 'YourCycleShop',
 'Unolab Manufacturing',
 'E bike 201',
 'The Cycle Factor',
 'Eiffel Bikes'
]

data = (list1, list2)
print(pd.DataFrame(data))

# créer une liste qui contient uniquement le premier mot
first_word_company_names = [name.split()[0] for name in company_names]
print(first_word_company_names)

# créer une liste qui contient la longueur du premier mot
length_first_word = [len(word) for word in first_word_company_names]
print(length_first_word)

dict_length_first_word = {word: len(word)for word in first_word_company_names}
print(dict_length_first_word)

# créer un set
# set_first_word_company_names = set(first_word_company_names )

# recreer en list
# new_first_word_company_names = list(set_first_word_company_names)

# créer une liste qui contient des tuples et sa position dans la liste originale
position_original = []

for word in first_word_company_names:
    for i in range(len(first_word_company_names)):
        if word == first_word_company_names[i]:
            count_word = first_word_company_names.count(word)
            position_word = i
            if count_word == 1:
                position_original.append(tuple({position_word}))
            elif count_word > 1:
                list_temp = []
                for j in range(count_word):
                    # index = index(first_word_company_names)
                    list_temp.append({position_word})
                position_original.append(tuple(list_temp))


print(f"position_original : {position_original}")
