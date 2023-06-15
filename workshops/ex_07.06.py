"""
SQL 
Write a SQL statement to create a table called continents, with the following columns:
continent_id
continent_name
continent_code – 2 letters code, use this link
Using the link above, write all SQL statements needed to add all the seven continents (INSERT).
Write a SQL statement to create a table called countries, with the following columns:
country_code – 2 letters code (e.g. RO, US, IT, etc)
country_name
continent_id – foreign key
population – number
TEMA PENTRU MIERCURI
Write a few SQL statements to add some countries. Here is a list of countries with their codes. Feel free to invent or approximate their populations, and use your geography knowledge for their continent. Add at least 10 countries, as diverse as possible (INSERT). Examples:
– Romania, EU, 19mil
– USA, NA, 330mil
– France, EU, 70mil
– Hungary, EU,  9mil
– Canada, NA, 40mil
– China, AS, 1450mil
– Belgium, EU, 12mil
–  Egypt, AF, 110mil
– Australia, OC, 25mil
Write a SQL statement to select all countries, ordered by name. Write another statement to count them all.
Write a SQL statement to select only countries with a population greater than 20 millions. 
Write a SQL statement to select only countries that start with a certain letter (choose one that exists for you, e.g. C in the example above).
Write a SQL statement that groups all countries by continents, and counts them.
Write a SQL statement that groups all countries by continent, and computes the total population per continent (SUM).

"""

import sqlite3

# conexiunea la db (daca db nu exista, va fi creata)
connection = sqlite3.connect('FILES/dbtest.db')

# cursor = structura de control folosita la interogare db. Intermediaza legatura intre db si sql query
cursor = connection.cursor()

# comanda de creare tabel in db
# cursor.execute("""
# CREATE TABLE Continents (
# continent_id INT PRIMARY KEY AUTOINCREMENT,
# continemt_name TEXT NOT NULL,
# continent_code CHAR(2) NOT NULL);
# """)

# continente = [('Africa', 'AF'), ('North America', 'NA'), ('South America', 'SA'), ('Antarctica', 'AN'), ('Australia', 'OC'), ('Asia', 'AS')]
#
# sql_query = 'INSERT INTO Continents (continemt_name, continent_code) VALUES (?,?)'
# cursor.executemany(sql_query, continente)

# cursor.execute("""
# CREATE TABLE Countries (
# Country_code CHAR(2) NOT NULL,
# Country_name TEXT NOT NULL FOREIGN KEY REFERENCES Continents(continent_id),
# Continent_ID CHAR(2) NOT NULL,
# Population INT);
# """)

# # executare comanda


# country_code = ['RO', 'US', 'FR', 'HU', 'CA', 'CN', 'BE', 'EG', 'AU']
# country_name = ['Romania', 'USA', 'France', 'Hungary', 'Canada', 'China', 'Belgium', 'Egypt', 'Australia']
# continent_id = ['EU', 'NA', 'EU', 'EU', 'NA', 'AS', 'EU', 'AF', 'OC']
# population = [19000000, 330000000, 70000000, 9000000, 40000000, 1450000000, 12000000, 110000000,25000000]
#
# for i in range(8):
#     cursor.execute(f'INSERT INTO Countries VALUES ("{country_code[i]}", "{country_name[i]}", "{continent_id[i]}", {population[i]});')

# cursor.execute('DELETE FROM Countries WHERE Country_code = "RO";')
# cursor.execute('SELECT * FROM Countries')

# data = cursor.fetchall()
# for i in data:
#     print(i)
# salvare modificari
connection.commit()

# inchidere conexiune
connection.close()

