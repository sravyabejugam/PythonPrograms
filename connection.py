import sqlite3

def connect(dbname):

    connection = sqlite3.connect(dbname)

    connection.execute("CREATE TABLE IF NOT EXISTS LAPTOPS(NAME TEXT ,PRICE INT ,RATING TEXT ,FEATURES TEXT)")

    print("Table created successfully")

    connection.close()

def insert_into_table(dbname, values):

    connection = sqlite3.connect(dbname)
    insert_sql = "INSERT INTO LAPTOPS (NAME ,PRICE ,RATING ,FEATURES) VALUES(?, ?, ?, ?)"

    connection.execute(insert_sql , values)

    connection.commit()
    connection.close()

def get_info(dbname):

    connection = sqlite3.connect(dbname)

    cur = connection.cursor()

    cur.execute("SELECT * FROM LAPTOPS")

    data = cur.fetchall()

    for record in data:
        print(record)

    connection.close()
