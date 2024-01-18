
# t (time) in s
t = [0, 2, 4, 6, 8, 10, 12, 14]


def sum_array(arr):
    summ = 0
    for elt in arr:
        summ += elt
    return summ


def average(arr):
    return sum_array(arr)/len(arr)


print(f"La moyenne est : {average(t)}")


def square(arr):
    result = 0
    for elt in arr:
        result = (elt * elt) + result
    return result



def variance(arr):
    print(square(arr))
    print(average(arr))
    return square(arr)/len(arr)-(average(arr)*average(arr))

print(variance(t))