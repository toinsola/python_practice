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

5.)

