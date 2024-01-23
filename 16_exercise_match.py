# Créer une fonction qui vérifie la lettre entréé par l'utilisateur est une voyelle

letter_entry = input("Saisir une lettre : ")

match str(letter_entry):
    case 'a':
        print('Cette lettre  {letter_entry} est une voyelle')
    case 'e':
        print('Cette lettre  {letter_entry} est une voyelle')
    case 'i':
        print('Cette lettre  {letter_entry} est une voyelle')
    case 'o':
        print('Cette lettre  {letter_entry} est une voyelle')
    case 'u':
        print('Cette lettre  {letter_entry} est une voyelle')
    case 'y':
        print('Cette lettre  {letter_entry} est une voyelle')
    case _:
        print(f"Cette lettre {letter_entry} n'est pas une voyelle")
