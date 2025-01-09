import csv
import mysql.connector

# Connect to server
mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password="2002",
    database="flipkartProducts"
)

# Get a cursor
mycursor = mydb.cursor()

# Create the table only once
create_table_query = '''
CREATE TABLE IF NOT EXISTS products2 (
    image VARCHAR(255),
    name VARCHAR(255),
    rating FLOAT,
    price VARCHAR(255),
    discount VARCHAR(255)
);
'''
mycursor.execute(create_table_query)

# Open the CSV file
with open('C:/Users/hrutu/Desktop/Flipkart Scraping/output/products2.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)  # Skip the header row if it exists

    # Prepare the insert query
    insert_query = '''
    INSERT INTO products2 (image, name, rating, price, discount) 
    VALUES (%s, %s, %s, %s, %s);
    '''
    for row in csv_reader:
        mycursor.execute(insert_query, row)
       

# Commit changes
mydb.commit()

# Close connection
mydb.close()
