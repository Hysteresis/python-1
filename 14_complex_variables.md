Create a list of numbers from one to tree hundred and seventy two

```
list_numbers = [number for number in range(1, 373)]

print(list_numbers)
```

Create a list of string, containing the months January to December. Each month have to be duplicate 31 times.
Expected result : ['January', 'January', 'January', 'January'.. 'December', 'December', 'December', 'December']
```
list_numbers = [number for number in range(1, 373)]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
new_list_months = [month for month in months for i in range(0, 31)]

print(new_list_months)
```

Compute the length of the list.
The expected result is 372
```
print(len(new_list_months))
```

Create a list of integer, containing 372 times the number 2020

```
list_years = [2020 for i in range(1, 373)]
print(list_years)

print(len(list_years))
```

Create a list of tuple. Each tuple have to contains the day of the year and the number tree hundred and seventy two.
The expected result is : [(1, 372), (2, 372)... (372, 372)]
```
tuple_lists = [(i, 372) for i in range(1, 373)]

print(tuple_lists)
```

Use a comprehension list, to divide each first element of the tuple by the second one.
Each result have to be rounded by 3 digits.
The excepted result is : [0.003, ...]
```
elapsed_time = [round(t[0]/t[1], 3) for t in tuple_lists]

print(elapsed_time)
```

Create a dictionary, containing the following keys ['day', 'month', 'year', 'elapsed_time'].
The values of that dictionnary will be the lists previously created.
The expected result is : {'day': [1, 2...], 'month': ['January', 'January'...'December'], 'year': [2020, 2020..], 'elapsed_time': [0.003, ...100]}
```
dict_elapsed_time = {
    "day": list_numbers,
    'month': new_list_months,
    'year': list_years,
    'elapsed_time': elapsed_time
}

print(dict_elapsed_time)
```

Create two sets.
One with all the days of the week (ex : Monday till Sunday). The other one with Monday till Wednesday.
```
set_all_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
set_mid_days = {'Monday', 'Tuesday', 'Wednesday'}
```

Substract the first list by the second one.
Expected result : {'Friday', 'Saturday', 'Sunday', 'Thursday'}
```
print(set_all_days - set_mid_days)
```
Explain the difference between a list and a tuple.
```
List: Mutable ordered collection; allows modifications.
Tuple: Immutable ordered collection; fixed after creation.
```
Explain the difference between a list and a dictionary.
```
List: Ordered collection by index; suitable for sequences.
Dictionary: Unordered key-value pairs; efficient for lookups.
```
Explain the difference between a list and a set.
```
List: Ordered collection with duplicates; suitable for sequences.
Set: Unordered collection without duplicates; ensures uniqueness.
```
