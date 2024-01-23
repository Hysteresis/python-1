import pandas as pd

path = "17_historique_calculs.csv"

def entry_values():
    """
    Saisir deux membres.

    :return: Une liste contenant les deux membres saisis.
    """
    try:
        a = float(input("Saisir le 1er membre : "))
        b = float(input("Saisir le 2nd membre : "))
        values = [a, b]
        return values
    except ValueError:
        print("Erreur : Veuillez saisir des nombres entiers.")
        return None

def addition(arr):
    """
    Effectuer l'addition de deux nombres

    :param arr: Une liste contenant deux membres à additionner.
    :return: Aucune valeur
    """
    if arr is not None:
        result = float(arr[0]) + float(arr[1])
        print(f"{arr[0]} + {arr[1]} = {result}")

        try:
            data = pd.read_csv(path)
        except (FileNotFoundError, pd.errors.EmptyDataError):
            data = pd.DataFrame(columns=['OPERANDE1', 'OPERANDE2', 'RESULTAT'])

        new_operation = pd.DataFrame([[arr[0], arr[1], result]], columns=['OPERANDE1', 'OPERANDE2', 'RESULTAT'])
        data = pd.concat([data, new_operation], ignore_index=True)
        data.to_csv(path, index=False)
    else:
        print("Une erreur est survenue lors de la saisie des membres.")


def consult_historique():
    """
    Choisir de consulter l'historique
    :return: aucune valeur de retour
    """
    # response = input("Consulter historique : o/N : ")
    retry = True
    while retry:
        response = input("Consulter historique : o/N : ")
        if str(response) == "o":
            historique = pd.read_csv(path)
            print("Historique des opérations :\n", historique)
            retry = False
        elif str(response) == "N":
            print("Vous ne souhaitez pas consulter l'historique")
            retry = False
        else:
            print("Il faut saisir la lettre 'o' ou 'N ")
            retry = True


response = True

while response:
    values = entry_values()
    addition(values)
    consult_historique()
    retry = input("Encore une addition ? o / N  : ")
    if retry == 'o':
        response = True
    elif str(response) == "N":
        print("Calculatrice à l'arrêt")
        retry = False
        break
    else:
        print("Vous ne souhaitez pas continuer")
        response = False

