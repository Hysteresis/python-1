# Create a list of tuple which contains numbers from 1 to 31 and the string 'January'.
# Expected result : [(1, 'January'), (2, 'January').. (31, 'January')]

january_numbers = tuple((i, 'January') for i in range(1, 32))
print(january_numbers)

# Create a list of tuple which contains numbers from 1 to 31 and the string 'February'.
# Expected result : [(1, 'February'), (2, 'February').. (31, 'February')]

year = 2024
february_numbers = tuple((i, 'February') for i in range(1, 32))
print(february_numbers)

# Concatenate the two previous list into one.
# Expected result : [(1, 'January'), (2, 'January').. (31, 'February')]

january_february_lists = january_numbers + february_numbers
print(january_february_lists)

# Check if the value (1, 'March') is in the concatenate list.
# If yes, then print "The 1 March exist". Otherwise, print "The 1 March does not exist"

if (1, 'March') in january_february_lists:
    print("The 1 March exist")
else:
    print("The 1 March does not exist")

# In the concatenated list, print every tuple which are equal or below 28 and contains the string 'February'.
february_28 = [elt for elt in january_february_lists if elt[0] <= 28 and elt[1] == 'February']
print(february_28)

# In the concatenated list, delete every date which are above 28.
february_delete = [elt for elt in january_february_lists if elt[0] <= 28 and elt[1] == 'February']
print(february_delete)
