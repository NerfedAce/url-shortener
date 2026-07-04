import psycopg2


#enter these field with the same data that you used for running postgres container
host = ""
user = ""
password = ""
database = ""
port = 0




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
