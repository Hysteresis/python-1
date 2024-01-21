import pandas as pd

company_names = ['All For Bikes',
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


new_company_names = []
i = 0


for company_name in company_names:
    company_name = company_name.split()
    new_company_names.append(company_name[0])
    i += 1

# print(new_company_names)


list_a = ['Oeuf', 'Lait', 'Sucre']
A = set(list_a)

list_b = ['Sucre', 'Farine', 'Huile']
B = set(list_b)

# l'ensemble des 2
# {'Huile', 'Farine', 'Lait', 'Oeuf', 'Sucre'}
outer = A | B
print(outer)

# intersection des 2
# {'Sucre'}
inner = A & B
print(inner)

# exclu Sucre
# {'Lait', 'Oeuf'}
left = A - B
print(left)

# exclu sucre A - B et Ajoute sucre A & B
# {'Lait', 'Oeuf', 'Sucre'}
# 1ère methode
left_inner = (A - B) | (A & B)
print(left_inner)

# 2nde methode
left_inner = A or B
print(left_inner)

