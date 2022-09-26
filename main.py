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

