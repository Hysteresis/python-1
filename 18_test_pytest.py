import variable
import pytest


# def test_number_1_():
#     """check if my_list is a list
#
#     :return:
#     """
#     assert (isinstance(variable.my_list, list))
#

# def test_number_2_my_list_length():
#     """check if the length of my_list is > 2
#
#     :return:
#     """
#     assert (len(variable.my_list) > 2)
#

# @pytest.mark.parametrize
from variable import *



# Vérifiez si la taille de la liste my_list est égale à 3.
def test_1_size_list():
    """"
    """
    assert (len(variable.my_list) == 3)


# Vérifiez si l'élément "one" appartient à l'ensemble my_set.
def test_2_one_is_in_my_set():
    assert ("one" in variable.my_set)


# Vérifiez si l'ordre des éléments dans la liste my_list est correct.
@pytest.mark.parametrize("lists", ["one", "two", "three"])
def test_3_list_ordered(lists):
    assert (variable.my_list == lists)


# Ajoutez un nouvel élément, par exemple "four", à la liste my_list, puis vérifiez si cet élément est présent
# dans la liste.
@pytest.mark.parametrize("lists", ["one", "two", "three", "four"])
def test_4_list_argument_false(lists):
    assert (variable.my_list != lists)
# Supprimez l'élément "two" de l'ensemble my_set et vérifiez qu'il n'est plus présent.
# Vérifiez si l'élément "four" est présent dans la liste my_list.
# Utilisez une fixture pour partager l('ensemble my_set entre plusieurs tests. Réalisez deux tests : '
#  'l')un vérifiant l'appartenance de l'élément "three" à l('ensemble partagé, et '
#   'l')autre vérifiant la taille de l'ensemble partagé.

