def my_function(arg1, arg2):
    return arg1 + arg2


def magicmix(person):
    """MA fonction magicmix calcule les ongrédients nécessaires

    :param person:
        person(integer): nombre de personnes

    :return:
        str: La recette
    """
    sugar = 6 * person
    salt = 1 * person
    return f"{sugar} g, {salt} g"


# bonne pratique mettre le nom de l'argument entre parenthèses
print(magicmix(person=50))


# bonne pratique mettre on peut mettre un parametre par défaut
def magicmix(person, unit='g'):
    """MA fonction magicmix calcule les ongrédients nécessaires

    :param person:
        person(integer): nombre de personnes

    :return:
        str: La recette
    """
    sugar = 6 * person
    salt = 1 * person
    return f"{sugar} {unit}, {salt} {unit}"


# bonne pratique mettre le nom de l'argument entre parenthèses
print(magicmix(person=20))


def my_function(b):
    print("b > 0")
    pass


# t (time) in s
t = [0, 2, 4, 6, 8, 10, 12, 14]
N = [2, 5, 16, 20, 40, 100, 200, 300]


def average(arr):
    """Caclul de la moyenne d'un tableau
    :param arr:
        arr(array): tableau de temps en secondes
    :return:
        float : la moyenne
    """
    summ = 0
    for elt in arr:
        summ = elt + summ
    return summ / len(t)


print("\nPour t et N :")
print("--------")
print(f"- La moyenne est : {average(t)}")


def square(arr):
    """"Calcul de la somme des carrés d'un tableau

    :param arr:
        arr(array): tableau
    :return:
        int : la somme des carrés
    """
    result = 0
    for elt in arr:
        result = (elt**2) + result
    return result


def variance(arr):
    """"Calcul de la variance

    :param arr:
        arr(array): tableau
    :return:
        float : la variance somme des carrés - moyenne au carré
    """
    return square(arr)/len(arr) - (average(arr)**2)


print(f"- La variance est : {variance(t)}")
