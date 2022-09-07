import json
import sqlite3
import psycopg2
import os.path

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "petstore.db")

postgres = psycopg2.connect(database="petdata", user="postgres",
                            password="admin", host="localhost", port="5432")


# cur = postgres.cursor()
# cur.execute("select * from pet.petstore")
# rows = cur.fetchall()
# print(rows)


class Dbconnection:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if not self.connection:
            self.connection = psycopg2.connect(database="petdata", user="postgres",
                            password="admin", host="localhost", port="5432")

        else:
            return self.connection

    def get_all_by_status(self, status):
        query = f"select * from PET WHERE status == '{status}'"
        self.get_connection()
        # self.connection.row_factory = sqlite3.Row
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        # return json.dumps([dict(i) for i in result])
        return [{'name': i[0], 'id': i[1], 'catagory': i[2], 'status': i[3]} for i in result]

    def get_all(self):
        query = f"select * from pet.petstore"
        self.get_connection()
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return [{'name': i[0], 'id': i[1], 'catagory': i[2], 'status': i[3]} for i in result]

    def get_all_by_id(self, id):
        query = f"select * from pet.petstore WHERE id == {id}"
        self.get_connection()
        cursor = self.connection.cursor()
        cursor.execute(query)
        i = cursor.fetchone()
        cursor.close()
        return {
            'name': i[0],
            'id': i[1],
            'catagory': i[2],
            'status': i[3]
        }

    def add_pet_data(self, name, id, catagory, status):
        query = f"INSERT INTO PET(PetName, id, catagory, status) VALUES ('{name}', {id}, '{catagory}', '{status}')"
        self.get_connection()
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        self.connection.close()
        return True

    def delete_pet_data(self, id):
        query = f"DELETE FROM PET WHERE ID == {id}"
        self.get_connection()
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        self.connection.close()
        return True

    def update_pet_data(self, name, id, catagory, status):
        query = f"UPDATE PET SET PetName = {name}, id = {id}, catagory = {catagory}, status = {status}"
        self.get_connection()
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        self.connection.close()
        return True
