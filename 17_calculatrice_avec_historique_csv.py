import pandas as pd

path = "17_historique_calculs.csv"

def entry_values():
    """
    Fonction pour saisir deux membres.

    :return: Une liste contenant les deux membres saisis.
    """
    try:
        a = int(input("Saisir le 1er membre : "))
        b = int(input("Saisir le 2nd membre : "))
        values = [a, b]
        return values
    except ValueError:
        print("Erreur : Veuillez saisir des nombres entiers.")
        return None

def addition(arr):
    """
    Fonction pour effectuer l'addition de deux nombres, afficher le résultat, et enregistrer l'opération dans
    un historique CSV.

    :param arr: Une liste contenant deux membres à additionner.
    :return: Aucune valeur de retour directe.
    """
    if arr is not None:
        result = int(arr[0]) + int(arr[1])
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
    response = input("Consulter historique : o/N : ")
    if str(response) == "o":
        historique = pd.read_csv(path)
        print("Historique des opérations :\n", historique)
    elif str(response) == "N":
        print("Vous ne souhaitez pas consulter l'historique")
    else:
        print("Il faut saisir la lettre 'o' ou 'N ")


values = entry_values()
addition(values)
consult_historique()
