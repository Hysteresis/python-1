import pandas as pd


first_date_range = pd.date_range('01/01/1992', '01/01/1999', freq='Y').astype(str).to_list()
second_date_range = pd.date_range('01/01/1988', '01/01/1995', freq='Y').astype(str).to_list()

set_first_date_range = set(first_date_range)
set_second_date_range = set(second_date_range)

# Les dates communes.
print("\ndate communes")
common_dates = set_first_date_range & set_second_date_range
print(common_dates)

print("date communes avec Pandas")
same_dates = set_first_date_range.intersection(set_second_date_range)
print(same_dates)

# Les dates non communes à ces deux listes.
print("\ndate non communes")

non_common_dates = set_second_date_range - set_first_date_range | set_first_date_range - set_second_date_range
print(non_common_dates)

print("date non communes avec Pandas")
nn_same_dates = set_first_date_range.symmetric_difference(set_second_date_range)
print(non_common_dates)
