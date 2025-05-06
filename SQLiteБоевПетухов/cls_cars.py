import sqlite3


class Cars:
    def __init__(self):
        self.con = sqlite3.connect("Автосалон.db")
        self.cur = self.con.cursor()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Автомобили (
               Id_автомобиля    INTEGER PRIMARY KEY AUTOINCREMENT
                                        UNIQUE
                                        NOT NULL,
               Модель           TEXT    UNIQUE,
               Стоимость        NUMERIC,
               Id_производителя NUMERIC REFERENCES Производители (Id_производителя) ON DELETE SET NULL
                                                                                    ON UPDATE NO ACTION
);''')
        self.con.commit()

    def __del__(self):
        # отключение от БД
        self.con.close()

    def view(self):
        # просмотр всех записей в таблице БД
        self.cur.execute("SELECT * FROM Автомобили")
        # список всех записей из таблицы
        rows = self.cur.fetchall()
        return rows

    def insert(self, model, price, manufacturer_id):
        # добавить запись
        self.cur.execute("INSERT INTO Автомобили (Модель, Стоимость, Id_производителя) "
                         "VALUES (?, ?, ?)",
                         (model, price, manufacturer_id))
        self.con.commit()

    def update(self, model, price, manufacturer_id):
        # изменение записи
        self.cur.execute("INSERT INTO Автомобили (Модель, Стоимость) "
                         "VALUES (?, ?)",
                         (model, price))
        self.con.commit()

    def delete(self, id):
        # удаление записи
        self.cur.execute("DELETE FROM Автомобили "
                         "WHERE Id_автомобиля=?", (id,))
        self.con.commit()

    def search(self, name):
        self.cur.execute("SELECT FROM Автомобили "
                         "WHERE Модель=?", (name,))

        rows = self.cur.fetchall()
        return rows
