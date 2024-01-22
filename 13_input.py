# nb_person = input("Combien de personnes viennent manger ce soir :")
#
# nb_person = int(nb_person)

# N = [2, 5, 16, 20, 40, 100, 200, 300]

# t (time) in s
t = []

def entry_time():
    """
    :return: number of values in list
    """
    number_items = input("Combien de valeurs voulez-vous saisir : ")
    for i in range(int(number_items)):
        input_entry = input(f"Valeur {i} :  ")
        t.append(float(input_entry))


entry_time()

def average(arr):
    """Caclul de la moyenne d'un tableau
    :param arr:
        arr(array): tableau de temps en secondes
    :return:
        float : la moyenne
    """
    print(f"Voici le tableau : {arr}")
    summ = 0
    for elt in arr:
        summ = elt + summ
    return summ / len(t)


def add_entry(add_list):
    """
    :param add_list:
    list
    :return:
    list : some element added to the list
    """
    choice = input("Voulez-vous ajouter des valeurs au tableau ? o / N ")
    while choice == 'o':
        add_number = input("Ajouter une valeur : ")
        add_list.append(float(add_number))
        print(t)
        choice = input("Voulez-vous ajouter des valeurs au tableau ? o / N ")
    print("\n--------")
    print(f"-> La moyenne du tableau est : {average(t)}")

add_entry(t)














#
# def square(arr):
#     """"Calcul de la somme des carrés d'un tableau
#
#     :param arr:
#         arr(array): tableau
#     :return:
#         int : la somme des carrés
#     """
#     result = 0
#     for elt in arr:
#         result = (elt**2) + result
#     return result
#
#
# def variance(arr):
#     """"Calcul de la variance
#
#     :param arr:
#         arr(array): tableau
#     :return:
#         float : la variance somme des carrés - moyenne au carré
#     """
#     return square(arr)/len(arr) - (average(arr)**2)
#
#
# print(f"- La variance est : {variance(t)}")
#
#
