from cls_cars import Cars


# создать объект базы данных
database_cat = Cars()


# логика
# добавление записи
def add_command(model, price, manufacturer_id):
    database_cat.insert(model, price, manufacturer_id)

def del_command(id):
    database_cat.delete(model, price, manufacturer_id)



# просмотр всех записей
def view_command():
    for row in database_cat.view():
        print(row)


# основная программа в консоли
# добавление записи
add_command(input("Введите название модели: "), input("Введите стоимость: "), input("Введите вторичный ключ производителя"))

# просмотр всех записей
view_command()
