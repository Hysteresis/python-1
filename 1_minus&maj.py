my_variable = "String Object"

my_variable.isupper()
print(my_variable)


def myfunction():
    """Cette fonction ne sert à rien
    input:
        None
    output:
        None
    la doc est comprise entre les triples quotes
    """
    pass


print(myfunction.__doc__)


month = "January"

# minuscule
print(month.lower())

# majuscule
print(month.upper())

# Capital
print(month.capitalize())
