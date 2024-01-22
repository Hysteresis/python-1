# Les boucles itératives

# ---------------  la boucle for ---------------
# for number in range(1, 10):
#     print(number)
#
# for number in range(10):
#     print(number)

# for letter in ['a', 'b', 'c']:
#     print(letter)
#
# for i, letter in enumerate(['a', 'b', 'c']):
#     print(i, letter)

# for number in range(10):
#     if number == 5:
#         break
#     else:
#         print(number)

for number in range(0, 10, 2):
    if number >=5:
        break
    else:
        print(number)


#--------------- Boucle while ---------------
i = 0
while i < 10:
    print(i)
    i += 1

my_boolean = True
while my_boolean:
    print('blabla')
    my_boolean = False

my_boolean = True
while my_boolean:
    print('blabla')
    break


my_boolean = True
while my_boolean:
    print('blabla')
    if (my_boolean):
        break
    else:
        continue


