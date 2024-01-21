# x = Surface de la maison
# a = 507.576
# b = 18.5
# c = -0.2
# y = Prix de la maison
#
# L'équation est : ax2 + bx + c = y
#
#TODO Votre mission, calculer y pour toutes les maisons allant de 200m² jusque 500m2.
# Seulement les pas de dix doit être pris en compte.

# print([507.576 * surface**2 + 18.5 * surface -0.2 for surface in range(200, 501, 10)])
# print({surface: 507.576 * surface**2 + 18.5 * surface -0.2 for surface in range(200, 501, 10)})

new_prices = {surface: round(507.576 * surface**2 + 18.5 * surface - 0.2, 2) for surface in range(200, 501, 10)}
print(new_prices)


