import sqlite3


class Database(object):
    def __init__(self):
        self.connection = sqlite3.connect("Database.db")
        self.cursor = self.connection.cursor()
        self.table_name = "Example"
        self.cursor.execute(f"Create table if not exists {self.table_name} \
            (column_1 int,column_2 text,column_3 real)")

    def insert_data(self):
        column_1 = int(input("Enter integer "))
        column_2 = input("Enter String ")
        column_3 = float(input("Enter Floating value "))
        self.cursor.execute(f"insert into {self.table_name} \
            (column_1,column_2,column_3) VALUES(?,?,?)", (column_1, column_2, column_3))
        self.connection.commit()
        print("Data Saved")

    def read_data(self):
        self.cursor.execute(f"select * from {self.table_name}")
        for db in self.cursor.fetchall():
            print(db)


if __name__ == "__main__":
    database = Database()
    database.insert_data()
    database.read_data()
    database.cursor.close()
    database.connection.close()
