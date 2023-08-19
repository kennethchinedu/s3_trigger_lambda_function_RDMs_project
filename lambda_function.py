import json, boto3, csv, os
import mysql.connector
from mysql.connector import Error, errorcode

s3_client = boto3.client('s3')

#Defining enviromental variable
password = os.environ.get('password')
user_name =os.environ.get('user')
host = os.environ.get('host')
db = os.environ.get('database')

#Lamda function
def lambda_handler(event, context):
    #Reading s3 file on upload
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = event['Records'][0]['s3']['object']['key']
    main_file = s3_client.get_object(Bucket=bucket, Key=csv_file)
    lines = main_file['Body'].read().decode('utf-8').split()
    
    #reading and displaying the dictionary values of our file
    results = []
    for row in csv.DictReader(lines):
        results.append(row.values())
    print(results)
    
    #Creating database connection
    connection = mysql.connector.connect( host = host,
                                       database = db,
                                       user = user_name,
                                       password = password)
    
    insert_qry = " INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor = connection.cursor()
    cursor.executemany(insert_qry, results)
    connection.commit()
    print(cursor.rowcount, "record inserted into user's table")
    
    

    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
