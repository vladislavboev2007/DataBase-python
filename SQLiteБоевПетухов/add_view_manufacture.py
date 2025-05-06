from cls_cars import Cars


# создать объект базы данных
database_cat = Cars()


# логика
# добавление записи
def add_command(name, country):
    database_cat.insert(name, country)


# просмотр всех записей
def view_command():
    for row in database_cat.view():
        print(row)


# основная программа в консоли
# добавление записи
add_command(input("Введите название производителя: "), input("Введите страну: "))

# просмотр всех записей
view_command()
