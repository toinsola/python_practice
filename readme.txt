1.) Install extensions needed for mysql and pycharm:
    file>settings>Project Name>Python Interpreter>Install extensions from search bar
        extensions:
        - mysql
        -mysql-connector
        -mysql-connector-python
        - pandas - pandas is a software library written for the Python programming language
            for data manipulation and analysis. In particular, it offers data structures and operations for
            manipulating numerical tables and time series.


2.) Configure mysql with Pycharm:
-Open DB browser, select plus sign, and authenticate your credentials and then test connection.



3.) Configure GIT Repository
VCS>Enable Version Control Integration

4.) Create project content in main.py
    content for main.py:

import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
        )
        print("MySQL Database connection was successful.")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


#Callout section
create_server_connection("localhost", "root", "student")

5.) Create Database from main.py

import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
        )
        print("MySQL Database connection was successful.")
    except Error as err:
        print(f"Error: '{err}'")

    return connection




def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully.")
    except Error as err:
        print(f"Error: '{err}'")

#Callout section
connection = create_server_connection("localhost", "root", "student")
database_query = "CREATE DATABASE Exotic_Dealership"
create_database(connection, database_query)


6.) Authenticate DB in Connection. Updated Main.py

import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name): <<<< added "db_name"
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database = db_name     <------------ added this whole line
        )
        print("MySQL Database connection was successful.")
    except Error as err:
        print(f"Error: '{err}'")

    return connection




def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully.")
    except Error as err:
        print(f"Error: '{err}'")

#Callout section
connection = create_server_connection("localhost", "root", "student", "Exotic_Dealership") <<<< added DB name
database_query = "CREATE DATABASE Exotic_Dealership"
create_database(connection, database_query)

7.)

