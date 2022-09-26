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

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
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

#fetching values from tables, from DB

display_vehicle_information = """
SELECT * FROM Vehicle_Information;
"""

display_directory_information = """
SELECT * FROM Directory;


"""

#updating information

vehicle_updates = """
UPDATE Vehicle_Information
SET mileage = "100"
WHERE make_model = "McLaren 720S";"""


#Callout section
connection = create_server_connection("localhost", "root", "student", "Exotic_Dealership")
execute_query(connection, vehicle_updates)
#execute_query(connection, employee_info)
information = read_query(connection, display_vehicle_information)

for values in information:
    print(values)