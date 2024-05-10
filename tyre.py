#Imports for functionality
import sqlite3
import locale

# Sets locale for formattinglocale
locale.setlocale(locale.LC_ALL, '')  # Setting locale based on system defaults

# Connects to SQLite database
conn = sqlite3.connect('country_data.db')
cursor = conn.cursor()

# Creates tables if they don't exist
create_tables_queries = [
    '''CREATE TABLE IF NOT EXISTS country (
            country_id INTEGER PRIMARY KEY,
            name TEXT,
            population INTEGER,
            gdp REAL,
            area INTEGER,
            government_type TEXT
        )''',
    '''CREATE TABLE IF NOT EXISTS cities (
            country_id INTEGER,
            name TEXT,
            population INTEGER
        )''',
    '''CREATE TABLE IF NOT EXISTS geography (
            country_id INTEGER,
            feature TEXT,
            description TEXT
        )''',
    '''CREATE TABLE IF NOT EXISTS histories (
            country_id INTEGER,
            event_date TEXT,
            event_description TEXT
        )''',
    '''CREATE TABLE IF NOT EXISTS languages (
            country_id INTEGER,
            language TEXT
        )'''
]

for query in create_tables_queries:
    cursor.execute(query)

# Inserts data into tables
country_data = [
    ("Esse", 102825424, 90432365893590, 3622983, "Democratic Republic"),
    ("Esusass", 112965273, 109562348754298, 5246239, "Democratic Republic"),
    ("Federation of the Interior", 2808126, 1203659340, 1849001, "Highly Integrated Federal State"),
    ("Saletonia", 256245242, 113772662966244, 6032549, "Democratic Theocracy"),
    ("Tyrania", 1027895753, 979832659274562, 20476236, "Federal Republic"),
    ("Ussur", 29242963, 124255825452, 29481011, "Democratic Republic"),
    ("Zene", 98209272, 103785378937667, 3849001, "Democratic Republic")
]

cursor.executemany("INSERT INTO country (name, population, gdp, area, government_type) VALUES (?, ?, ?, ?, ?)", country_data)

language_data = [
    (1, 'Exterian'),
    (2, 'Tyranian'),
    (3, 'Tyranian'),
    (4, 'Tyranian'),
    (5, 'Tyranian'),
    (6, 'Tyranian'),
    (7, 'Zenean')
]

cursor.executemany("INSERT INTO languages (country_id, language) VALUES (?, ?)", language_data)

city_data = [
    (1, 'Baak', 20644978),
    (2, 'Littleton', 23322458),
    (3, 'Darysys', 1012003),
    (4, 'Faubridge', 45245345),
    (5, 'Tyrania', 302565423),
    (6, 'Godwill', 10578329),
    (7, 'Candis City', 14567344)
]

cursor.executemany("INSERT INTO cities (country_id, name, population) VALUES (?, ?, ?)", city_data)

geography_data = [
    (1, 'Great Lakes National Park', 'A beautiful land covered in thousands of lakes both great and small. Wildlife not found anywhere else in the world are found here.'),
    (2, 'Middlelands Preserve', 'A sacred and beautiful land covered in oak trees thousands of years old. It is thought to have been the site of where the Adam and Eve were placed.'),
    (3, 'Federations of The Nations World Park', 'A large archipelago where people from all nations come to participate in vacationing and cultural infusion.'),
    (4, 'Northwest Ridge Preserve', 'The land with the most dense natural resources per square mile in the world, home to untouched lands, and thousands of species of animals.'),
    (5, 'National Park of the Most Magnificent Tyre', 'A mountainous and beautiful area of Tyrania, said to have housed many of the prophets on sabbaticals pre and post-flood.'),
    (6, 'Lindoria National Preserve', 'A set of untouched tropical islands home to the most number of species in the world, and the volcanic soil is some of the richest on Tyre.'),
    (7, 'Lord of the East National Park and Preserve', 'A sacred land where the Lord Ishaw had received communion with Elohim before his death, as written in the Holy Books.')
]

cursor.executemany("INSERT INTO geography (country_id, feature, description) VALUES (?, ?, ?)", geography_data)

history_data = [
    (1, '4527-02-12', 'The city of Baak is thrust into a 100-year civil war which killed 4.3 million souls.'),
    (2, '0001-01-01', 'Adam and Eve are expelled from the Garden, marking the beginning of the 7000 years.'),
    (3, '3901-07-01', 'The city of Darysys hosts the first Sea Games, marking a turning point in foreign relations between all nations.'),
    (4, '5000-04-04', 'Saletonia becomes a Democratic Theocracy after 552 years as a Democratic Republic.'),
    (5, '3991-06-13', 'The second Kingdom of Tyrania is formed after The Flood, heralding a new era in world history.'),
    (6, '4322-02-28', 'Ussur wins independence from the Kingdom of Tyrania after a bloody revolutionary war that killed two million souls.'),
    (7, '4022-5-23', 'The Lord Ishaw is born in the nation of Zene, fulfilling laws of the eternities.')
]

cursor.executemany("INSERT INTO histories (country_id, event_date, event_description) VALUES (?, ?, ?)", history_data)

# Commits changes
conn.commit()

# Retrieves average GDP and total population using two aggregate functions
cursor.execute("SELECT AVG(gdp), SUM(population) FROM country")
avg_gdp, total_population = cursor.fetchone()

# Formats numerical values with commas
formatted_avg_gdp = locale.format_string("%.2f", avg_gdp, grouping=True)
formatted_total_population = locale.format_string("%d", total_population, grouping=True)

print("Average GDP:", formatted_avg_gdp)
print("Total Population:", formatted_total_population)

# Closes connection
conn.close()