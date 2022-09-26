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

7.) Create workhorse function to

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


8.) Populate tables:


import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database = db_name
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

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

#queries

#create tables:

create_vehicle_information_table = """
CREATE TABLE Vehicle_Information(
Make_Model VARCHAR(50) NOT NULL,
PRICE VARCHAR(50) NOT NULL,
Mileage VARCHAR(50) NOT NULL,
Color VARCHAR(20) NOT NULL);"""


create_staff_table = """
CREATE TABLE Directory(
Name VARCHAR(70) NOT NULL,
Position VARCHAR(70) NOT NULL,
Benefits VARCHAR(5) NOT NULL)"""

#populate tables

vehicle_info = """
INSERT INTO Vehicle_Information VALUES
("McLaren 720S", "$230,000", "50", "Graphite"),
("Aston Martin Vanquish", "$450,000", "112", "Silver"),
("Bugatti Chiron", "$2,450,000", "3", "Black")"""

employee_info = """
INSERT INTO Directory Values
("Dorothy Moore", "Area Manager", "Yes"),
("Mark Maxwell", "Department Manager", "Yes"),
("Brendan Dean", "Sales Representative", "Yes"),
("Christina Berry", "Sales Representative", "Yes")"""

#Callout section
connection = create_server_connection("localhost", "root", "student", "Exotic_Dealership")
execute_query(connection, employee_info)


9.) Read the information from the Database in Pycharm.
update content for main.py

