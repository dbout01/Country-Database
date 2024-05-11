## Overview

**Project Title**: Country Database

**Project Description**: This is a database of fictional countries I created with detailed information,
such as GDP, cities and geographical features. This information can be pulled using the .py file provided.

**Project Goals**:
* Become more confident in my skills with relational databases
* Try new kinds of datasets.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Install Python: Ensure that Python is installed on your system. You can download it from the official Python website: python.org.
2. Install SQLite: If you don't already have SQLite installed, you can download the SQLite tools from the official website: sqlite.org.
3. Table Creation: Define SQL queries to create tables if they don't already exist. This involves creating tables for storing country data, city data, geography data, historical events, and language data.
4. Data Insertion: Prepare and execute SQL statements to insert data into the tables. Data includes information about countries, cities, geographical features, historical events, and languages.
5. Clone the Repository: Clone the repository containing the code if you haven't already done so.
6. Imports: Import necessary modules and libraries. In this case, you'll need sqlite3 for working with SQLite databases and locale for formatting numerical values.
7. Database Connection: Connect to the SQLite database using sqlite3.connect().
8. Data Retrieval: Perform SQL queries to retrieve information from the database. This may involve querying aggregate functions like AVG and SUM to calculate average GDP and total population.
9. Data Formatting: Format the retrieved numerical values using the locale module to include commas for readability.
10. Navigate to the Directory: Using the command line interface, navigate to the directory where the code files are located.
11. Run the Script: Execute the Python script by running the following command: python tyre.py
12. View Output: Once the script is executed, it will connect to the SQLite database, create tables (if they don't exist), insert data into the tables, calculate the average GDP and total population, and print the results. You can view the output directly in the terminal/console.
13. Verify Database: Optionally, you can verify the SQLite database (tyre.db) to ensure that the tables and data have been correctly created and inserted.
14. Close Connection: After the script execution is completed, the connection to the SQLite database will be closed automatically.

Instructions for using the software:

1. Open the tyre.py file
2. Open a Terminal or Command Prompt: Navigate to the directory where the Python file is located.
3. Run the Python File: Use the python command followed by 'tyre.py'
4. Execute: Press Enter to execute the command.
5. (Here you will see all of the tables in the data become outputted as well as results for the  SQLite COUNT() function that adds all country populations and the SQLite AVG() function that calculates the average GDP of the entire world
## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* VSCode (latest version)
* DB Browser SQLite3 (https://sqlitebrowser.org/dl/)
* SQLite extension on VSCode
* SQLite Tools (https://www.sqlitetutorial.net/download-install-sqlite/)

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [YouTube](https://youtu.be/AKynuCZttBs?si=gDmvsa4fEnuRUAdX)
* [YouTube](https://youtu.be/halX_6VxwHk?si=wABiawudBPsfDqzW)
* [YouTube](https://youtu.be/YmW7LCnWrxY?si=SXPsa_wGTW47uj4M)
* [YouTube](https://youtu.be/6QH7pQEfoSo?si=fMYbRgFh9CQOvYxS)
* [YouTube](https://youtu.be/l5NQ58TJejk?si=YU64mhbtlCxNfKFa)
* [YouTube](https://youtu.be/b0Dplx4M5zg?si=rRvkzEjx1fccfVRZ)
* [YouTube](https://youtu.be/lkodYE6Xb7M?si=5nR93Qu9sSchxOng)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* Seperate SELECT statement
* GROUPBY
* Ironing-out all bugs
* Adding fuctionality that lets the user add statistics to a table/multiple tables
* A user-friendly UI, rather than just output
