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

class Extract:
    def __init__(self, url):
        self.url = url

    def read_website(self, url):
        cheese_list = []
        data = urlopen(url)
        soup = BeautifulSoup(data, features="html.parser")
        tds_list = soup.find_all('td')

        for i in range(0, len(tds_list), 3):
            if tds_list[i] != "":
                cheese = tds_list[i].text
                family = tds_list[i+1].text
                paste = tds_list[i+2].text
                cheese_list.append({'Fromage': cheese, 'Famille': family, 'Pâte': paste})


        # Create a DataFrame outside the loop
        data = pd.DataFrame(cheese_list)

        # Assuming you want to add a creation date column
        data['creation_date'] = datetime.now()

        # Connect to SQLite and write the DataFrame to the ODS table
        con = sqlite3.connect("DATA/boitedufromager.sqlite")
        data.to_sql("ODS", con, if_exists="replace", index=False)
        con.close()
        # # Loading

        con = sqlite3.connect("DATA/rugby_team.sqlite")

        # Write the new DataFrame to a new SQLite table
        data.to_sql("ODS", con, if_exists="replace")

        con.close()

        con = sqlite3.connect("DATA/rugby_team.sqlite")
        data.to_sql("ODS", con, if_exists="replace")
        con.close()

        con = sqlite3.connect("DATA/rugby_team.sqlite")

        # Load the data into a DataFrame
        data = pd.read_sql_query("SELECT * from ODS", con)
        print(data)

        con.close()
        # print(data)

        return tds_list


url = "https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/"
extract = Extract(url)
print(extract.read_website(url))

# # Extraire de l'information
# data = urlopen('https://fr.wikipedia.org/wiki/Surnom_des_%C3%A9quipes_nationales_de_rugby_%C3%A0_XV')
# data = data.read()
# soup = BeautifulSoup(data)
# team_table = soup.find('table', {'class': 'wikitable'})
#
# tds = soup.find_all('span', {'class': 'nowrap'})
#
# flag_urls = []
# flag_titles = []
# countries = []
#
# for td in tds:
#     flag_url = td.find('a', {'class': 'mw-file-description'})['href']
#     # flag_title = td.find('a', {'class':'mw-file-description'})['title']
#     country = (td.text)
#
#     flag_urls.append(flag_url)
#     # flag_titles.append(flag_title)
#     countries.append(country)
#
# data = {'flag_urls': flag_urls, 'countries': countries}
# data = pd.DataFrame(data)
# data['creation_date'] = datetime.now()
#
# TODO # Transformation d'information
# # Loading
#
# con = sqlite3.connect("DATA/rugby_team.sqlite")
#
# # Write the new DataFrame to a new SQLite table
# data.to_sql("ODS", con, if_exists="replace")
#
# con.close()
#
# con = sqlite3.connect("DATA/rugby_team.sqlite")
#
# # Load the data into a DataFrame
# data = pd.read_sql_query("SELECT * from ODS", con)
# print(data)
# # Select only data for 2002
# #surveys2002 = surveys_df[surveys_df.year == 2002]
#
# con.close()
# # data
#
