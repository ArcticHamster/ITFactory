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

