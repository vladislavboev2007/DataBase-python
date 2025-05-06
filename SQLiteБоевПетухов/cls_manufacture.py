import sqlite3


class Cars:
    def __init__(self):
        self.con = sqlite3.connect("Автосалон.db")
        self.cur = self.con.cursor()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Производители (
               Id_производителя INTEGER PRIMARY KEY AUTOINCREMENT
                                        UNIQUE
                                        NOT NULL,
               Наименование     TEXT,
               Страна           TEXT    NOT NULL
);''')
        self.con.commit()

    def __del__(self):
        # отключение от БД
        self.con.close()

    def view(self):
        # просмотр всех записей в таблице БД
        self.cur.execute("SELECT * FROM Производители")
        # список всех записей из таблицы
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, country):
        # добавить запись
        self.cur.execute("INSERT INTO Производители (Наименование, Страна) "
                         "VALUES (?, ?)",
                         (name, country))
        self.con.commit()

    def update(self, model, price, manufacturer_id):
        # изменение записи
        self.cur.execute("INSERT INTO Производители (Наименование, Страна) "
                         "VALUES (?, ?)",
                         (name, country))
        self.con.commit()

    def delete(self, id):
        # удаление записи
        self.cur.execute("DELETE FROM Производители "
                         "WHERE Id_производителя=?", (id,))
        self.con.commit()

    def search(self, name):
        self.cur.execute("SELECT FROM Производители "
                         "WHERE Наименование=?", (name,))

        rows = self.cur.fetchall()
        return rows
