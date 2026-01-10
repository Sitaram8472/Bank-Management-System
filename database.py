import mysql.connector as sql

#  first time run this query alwalys beasuse database is connected with sql is compulsory otherwise you will gey error query is python database.py


mydb = sql.connect(
    host="localhost",
    user="bankuser",
    passwd="bank123",
    database="bank"
)

cursor = mydb.cursor(buffered=True)


def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            username VARCHAR(20) NOT NULL,
            user_password VARCHAR(20) NOT NULL,
            name VARCHAR(20) NOT NULL,
            age INT NOT NULL,
            city VARCHAR(20) NOT NULL,
            balance INT NOT NULL,
            account_number INT NOT NULL,
            status BOOLEAN NOT NULL
        )
    ''')
    mydb.commit()

if __name__ == "__main__":
    print("CONNECTED SUCCESSFULLY")
    createcustomertable()
