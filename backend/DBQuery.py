import psycopg2
import os

#enter these field with the same data that you used for running postgres container
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
port = os.getenv("DB_PORT")




def search(short):
    conn = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
    curr = conn.cursor()
    curr.execute(
        "SELECT * FROM urls WHERE short_url = %s;",
        (short,)
    )
    data = curr.fetchall()
    print(data)
    conn.close()
    if data :
        return data
    else:
        return None

def insert(short , long , region):
    conn = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
    curr = conn.cursor()
    curr.execute(
        "SELECT * FROM urls WHERE short_url = %s;",
        (short,)
    )
    data = curr.fetchall()
    if data :
        conn.close()
        return None

    curr.execute("INSERT INTO urls VALUES (%s, %s, %s , %s);", (short, long, 0 ,  region))
    conn.commit()
    conn.close()
    return short
