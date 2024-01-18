import math
# t (time) in s
t = [0, 2, 4, 6, 8, 10, 12, 14]
N = [2, 5, 16, 20, 40, 100, 200, 300]


def sum_array(arr):
    summ = 0
    for elt in arr:
        summ += elt
    return summ


def average(arr):
    return sum_array(arr)/len(arr)

print("\nPour t :")
print("--------")
print(f"- La moyenne est : {average(t)}")


def square(arr):
    result = 0
    for elt in arr:
        result = (elt * elt) + result
    return result


def variance(arr):
    return square(arr)/len(arr)-(average(arr)*average(arr))


print(f"- La variance est : {variance(t)}")


def natural_logarithm(arr):
    ln = []
    for elt in arr:
        ln.append(round(math.log(elt), 8))
    return ln

print("\nPour ln(N) :")
print("-------------")
print(f"\n- La moyenne des ln est : {round(average(natural_logarithm(N)), 2)}")

print(square(natural_logarithm(N))/8 - round(average(natural_logarithm(N)), 2)*round(average(natural_logarithm(N)), 2))


# print(f" {variance(nat_logarithm )} ")
14,48