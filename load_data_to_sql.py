import csv, os
import mysql.connector
from mysql.connector import Error, errorcode


# This function describes how I read data and load to AWW RDS

password = os.environ.get('password')
user_name =os.environ.get('user')
host = os.environ.get('host')
db = os.environ.get('database')

try: 
    connection = mysql.connector.connect( host = host,
                                       database = db,
                                       user = user_name,
                                       password = password)
    
    
    #reading Csv file initiating cursor
    rows= []
    with open('cleaned_sheet.csv', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row.values())
        
        #Insert Query
        insert_qry = " INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor = connection.cursor()
        cursor.executemany(insert_qry, rows)
        connection.commit()
        print(cursor.rowcount, "record inserted into table")

        #Select statement to validate our output
        select_sql = "SELECT * FROM users"
        cursor = connection.cursor()
        cursor.execute(select_sql)
        records = cursor.fetchall()
        print("Total number of rows is:", cursor.rowcount)
        
        print("\npringing each user")
        for row in records:
            print("name = ", row[0]),
            print("email = ", row[1])
        cursor.close()
        
except mysql.connector.Error as error:
    print("Failed to inset into user tables {}".format(error))  
    

finally: 
    if (connection.is_connected()):
        connection.close()
        print("Connection is closed")
    

