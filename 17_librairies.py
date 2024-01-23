import sys
import os

ROOT = os.getcwd()
sys.path.append(ROOT)

# import module_1
from pandas import DataFrame, date_range
import pandas


# module_1.function_1()





data = DataFrame({'A':[*range(100)]})

import numpy as np


A = np.arange(0, 100)

B = np.arange(200, 300)

A * B

path = "C://Users//adoup//OneDrive//Documents//PROJECT//APPRENDRE_PYTHON//content//PHARMA PILOT//EDUCATION//DATA//BusinessPartners.csv"

f = open(path)

for n_line, line in enumerate(f.readlines()):
    if n_line == 0:
        print(line.split(','))
    else:
        print(line.split(','))

# Extraction de données
data = pd.read_csv(path)
data.head()

from faker import Faker

my_generator = Faker()

addresses = [my_generator.address() for n in range(100)]
data = pd.DataFrame({'Addresses':addresses})

# Transform

data['Addresses'] = data['Addresses'].apply(lambda row:row.replace('\n', ' '))
data['Addresses'] = data['Addresses'].str.replace('\n', ' ')

# Chargement

data.to_csv('DATA/BusinessPartnersClean.csv', index=False)

# ETL
# Extraction de données
data = pd.read_csv(path)
data.head(3)

def retrieve_first_name(email):
    """_summary_

    Args:
        email (_type_): _description_

    Returns:
        _type_: _description_
    """
    return email.split('.')[0]

retrieve_first_name('maria.brown@all4bikes.com')

columns = ['PARTNERID', 'EMAILADDRESS']

data = data[columns]
data['FIRSTNAME'] = data['EMAILADDRESS'].apply(retrieve_first_name)

data = data.rename({0: 100}, axis=0)
data.head()

# Chargement

data.to_csv('DATA/BusinessPartnersClean.csv', index=False)
