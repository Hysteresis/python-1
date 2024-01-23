# Créer une fonction qui vérifie la lettre entréé par l'utilisateur est une voyelle

letter_entry = ''


def vowel_verifcator(letter_entry):
    match str(letter_entry):
        case 'a':
            print(f'Cette lettre {letter_entry} est une voyelle')
        case 'e':
            print(f'Cette lettre {letter_entry} est une voyelle')
        case 'i':
            print(f'Cette lettre {letter_entry} est une voyelle')
        case 'o':
            print(f'Cette lettre {letter_entry} est une voyelle')
        case 'u':
            print(f'Cette lettre {letter_entry} est une voyelle')
        case 'y':
            print(f'Cette lettre {letter_entry} est une voyelle')
        case _:
            print(f"Cette lettre {letter_entry} n'est pas une voyelle")


vowel_verifcator(letter_entry = input("Saisir une lettre : "))
