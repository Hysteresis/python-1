# Create a function which will generate a calendar.

# The parameter have to be a Year, the out a Dictionnary with the following keys.

# The expected result is :
# {'day': [1, 2...], 'month': ['January', 'January'...'December'], 'year': [2020, 2020..], 'elapsed_time': [0.003, ...100]}

def generate_calendar(year):
    list_numbers = [number for number in range(1, 373)]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    new_list_months = [month for month in months for i in range(0, 31)]
    list_years = [year for i in range(1, 373)]
    tuple_lists = [(i, 372) for i in range(1, 373)]
    elapsed_time = [round(t[0] / t[1], 3) for t in tuple_lists]
    new_calenendar = {
        "day": list_numbers,
        'month': new_list_months,
        'year': list_years,
        'elapsed_time': elapsed_time

    }
    return new_calenendar


print(generate_calendar(2021))


# Why are we using functions ?
# We use functions when, for example, there is repeated code, which makes the code clearer and easier to maintain.
