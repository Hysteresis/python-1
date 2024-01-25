from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import sqlite3

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
url = "https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/"



class Extract:
    def __init__(self, url):
        self.url = url

    def read_website(self, url):
        cheese_list = []
        data = urlopen(url)
        soup = BeautifulSoup(data, features="html.parser")
        tds_list = soup.find_all('td')

        for i in range(0, len(tds_list), 3):
            cheese = tds_list[i].text.strip()  # Utilisez .strip() pour supprimer les espaces inutiles
            if cheese:
                family = tds_list[i + 1].text.strip()
                paste = tds_list[i + 2].text.strip()
                cheese_list.append({'Fromage': cheese, 'Famille': family, 'Pate': paste})

        print(cheese_list[1]['Fromage'])

        # Create a DataFrame outside the loop
        data = pd.DataFrame(cheese_list)

        # Assuming you want to add a creation date column
        data['creation_date'] = datetime.now()

        # Connect to SQLite and write the DataFrame to the ODS table
        con = sqlite3.connect("DATA/boitedufromager.sqlite")
        data.to_sql("ODS", con, if_exists="replace", index=False)
        con.close()
        # # Loading

        con = sqlite3.connect("DATA/boitedufromager.sqlite")

        # Write the new DataFrame to a new SQLite table
        data.to_sql("ODS", con, if_exists="replace")

        con.close()

        con = sqlite3.connect("DATA/boitedufromager.sqlite")
        data.to_sql("ODS", con, if_exists="replace")
        con.close()

        con = sqlite3.connect("DATA/boitedufromager.sqlite")

        # Load the data into a DataFrame
        data = pd.read_sql_query("SELECT * from ODS", con)
        print(data)

        con.close()
        # print(data)

        return tds_list


extract = Extract(url)
print(extract.read_website(url))
