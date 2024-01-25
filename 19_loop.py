# Loop
# By using a while loop, create a list of numbers from 1 to 31 included.
i = 0
numbers = []
while i < 31:
    i += 1
    numbers.append(i)
print(numbers)


# By using a for loop, create a list of tuple, containing a number and a month.
# All months can have 31 days.

# Expected result : [(1, 'January'), (2, 'January'), (31, 'Décembre')]

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

result = []
i = 0
for month in months:
    for day in range(1, 32):
        result.append((day, month))

print(result)




print()