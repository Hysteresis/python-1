from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import sqlite3

# Extraire de l'information
data = urlopen('https://fr.wikipedia.org/wiki/Surnom_des_%C3%A9quipes_nationales_de_rugby_%C3%A0_XV')
data = data.read()

# Transformation d'information
soup = BeautifulSoup(data)
team_table = soup.find('table', {'class': 'wikitable'})

tds = soup.find_all('span', {'class': 'nowrap'})

flag_urls = []
flag_titles = []
countries = []

for td in tds:
    flag_url = td.find('a', {'class': 'mw-file-description'})['href']
    # flag_title = td.find('a', {'class':'mw-file-description'})['title']
    country = (td.text)

    flag_urls.append(flag_url)
    # flag_titles.append(flag_title)
    countries.append(country)

data = {'flag_urls': flag_urls, 'countries': countries}
data = pd.DataFrame(data)
data['creation_date'] = datetime.now()

# Loading

con = sqlite3.connect("boite_du_fromager/DATA/rugby_team.sqlite")

# Write the new DataFrame to a new SQLite table
data.to_sql("ODS", con, if_exists="replace")

con.close()

con = sqlite3.connect("boite_du_fromager/DATA/rugby_team.sqlite")

# Load the data into a DataFrame
data = pd.read_sql_query("SELECT * from ODS", con)
print(data)
# Select only data for 2002
#surveys2002 = surveys_df[surveys_df.year == 2002]

con.close()
# data

# Créer un ETL qui extrait les informations de fromages : https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/
#
#
# Contraintes techniques :
# - ETL devra être implémenté en classe
# - Les informations stockées devront l'être dans SQL dans une table ODS
# - Les colonnes devront être : Le fromage, la famille, la pâte et la date de création.
#
# Votre travail sera validé par 10 tests unitaires implémentés par pytest. Le rapport de résultat devra être livré sur github.
#