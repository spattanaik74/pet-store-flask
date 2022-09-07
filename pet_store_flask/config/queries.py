import sqlite3
DB_PATH = sqlite3.connect('petstore.db')


def get_data(string):
    query = f"SELECT * FROM PET WHERE STATUS == '{string}'"
    conn = DB_PATH
    cursor = conn.cursor()
    cursor.execute(query)
    return conn


def get_all_data():
    query = f"SELECT * FROM PET"
    conn = DB_PATH
    cursor = conn.cursor()
    cursor.execute(query)
    return conn


def add_pet(name, id, catagory, status):
    queury = f"INSERT INTO PET(PetName, id, catagory, status) VALUES('{name}', {id}, '{catagory}', '{status}')"
    conn = DB_PATH
    cursor = conn.cursor()
    cursor.execute(queury)
    conn.commit()
    cursor.close()


if __name__ == '__main__':
    get_all_data()