# Listes (list) :
# Collection d'éléments ordonnée et mutable.
# Des crochets [].
# Différents types (nombres, chaînes de caractères, objets, etc.).

ma_liste = [1, 2, 3, "quatre", 5.0]
print(ma_liste)

# Vous pouvez ajouter, supprimer et modifier des éléments dans une liste.
# ajouter
ma_liste.append("ceci est une valeur ajoutée qui va etre efface avec .pop()")
print(ma_liste)

# supprimer
ma_liste.pop()
print(ma_liste)

# modifier
ma_liste[0] = "element 0 bien modifié"
print(ma_liste)

#  ------------------------------
# Tuples (tuple) :
# Un tuple est similaire à une liste, mais il est immuable
# Parenthèses ().
# Les éléments d'un tuple peuvent également être de différents types.
mon_tuple = (1, 2, "trois", 4.0)
print(mon_tuple[2])

# immuable
# mon_tuple[2] = "deux" # renvoie une erreur :TypeError: 'tuple' object does not support item assignment
print(mon_tuple)



#  ------------------------------
# Chaînes de caractères (str) :
# Séquence de caractères.
# Guillemets simples (') ou doubles (").
# Les caractères individuels d'une chaîne peuvent être accédés à l'aide d'index.
ma_chaine = "Bonjour, Python !"
print(ma_chaine)
print(ma_chaine[0])
print(ma_chaine[10])

# ma_chaine[10] = "i" # erreur on ne peut pas remplacer le caractere : TypeError: 'str' object does not support item assignment
# print(ma_chaine)


#  ------------------------------
# Plages (range) :
# Sséquence d'entiers immuable.
ma_sequence = range(5)
print(ma_sequence)

for elt in range(5):
    print(elt)

for elt in range(2, 5):
    print(elt)

for elt in range(0, 20, 4):
    print(elt)
