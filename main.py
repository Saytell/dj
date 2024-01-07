import sys
from PyQt5 import QtWidgets
import sqlite3
from sqlite3 import Error

from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ui.untitled import Ui_Frame
from ui.yes import Ui_yes
from ui.no import Ui_no
from ui.client import Ui_client_form
from ui.order import Ui_order_form
from ui.tours import Ui_tours_form

connection = None
try:
    connection = sqlite3.connect('host.db')
    cur = connection.cursor()
    print("Подключение к базе данных SQLite прошло успешно")
except Error as e:
    print(f"Произошла ошибка '{e}'")

app = QtWidgets.QApplication(sys.argv)
frame = QtWidgets.QFrame()
ui = Ui_Frame()
ui.setupUi(frame)
frame.show()

def check_query(connection, name, password):
    result = True
    cursor = connection.cursor()
    record_name = name
    record_password = password
    name_check = cursor.execute("SELECT Login,Password  FROM Clients WHERE Login = ? AND Password = ?", (record_name, record_password, )).fetchone()
    if name_check is None:
        result = False
    return result

def get_hotels_data():
    query = "SELECT * FROM Tours, Hotels"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data

def filters(self, star_rate, country, hotel_id, price, start_date, end_date):
    cursor = connection.cursor()
    # Подготовка запроса к базе данных с использованием параметров фильтрации
    query = "SELECT * FROM Hotels WHERE StarRate=? AND Country=? AND id_hotel=? AND Price BETWEEN ? AND ? AND DateStart BETWEEN ? AND ?"
    cursor.execute(query, (star_rate, country, hotel_id, price, start_date, end_date))
    data = cursor.fetchall()
    connection.close()
    return data


def populate_table(data):
    # Определяем размеры таблицы и заполняем модель данными
    model.setRowCount(len(data))
    model.setColumnCount(len(data[0]))
    for row_num, row_data in enumerate(data):
        for col_num, cell_data in enumerate(row_data):
            item = QStandardItem(str(cell_data))
            model.setItem(row_num, col_num, item)

def open_client_form():
    global client_form
    client_form = QtWidgets.QFrame()
    ui = Ui_client_form()
    ui.setupUi(client_form)
    client_form.show()
    ui.tours.clicked.connect(open_tours_form)

def open_order_form():
    global order_form
    order_form = QtWidgets.QFrame()
    ui = Ui_order_form()
    ui.setupUi(order_form)
    order_form.show()

    ui.date_begining.setText(start_date)
    ui.date_end.setText(end_date)
    ui.name_hotel.setText(hotel_id)
    ui.sum_tour.setText(price)
    ui.name_tour.setText(name_tour)

def open_tours_form():
    global tours_form, model, star_rate, country, hotel_id, price, start_date, end_date,name_tour
    tours_form = QtWidgets.QFrame()
    ui = Ui_tours_form()
    ui.setupUi(tours_form)
    tours_form.show()

    # Создаем модель данных для таблицы
    model = QStandardItemModel()
    ui.tableView.setModel(model)

    # Получаем данные из таблицы Hotels
    hotels_data = get_hotels_data()

    # Заполняем модель данными
    populate_table(hotels_data)

    star_rate = ''
    name_tour = ''
    country = ''
    hotel_id = ''
    price = ''
    start_date = ''
    end_date = ''

    def selected(selected_index):
        global star_rate, country, hotel_id, price, start_date, end_date, name_tour
        row = selected_index.row()
        star_rate = model.index(row, 3).data()
        country = model.index(row, 11).data()
        hotel_id = model.index(row, 1).data()
        price = model.index(row, 5).data()
        start_date = model.index(row, 7).data()
        end_date = model.index(row, 8).data()
        name_tour = model.index(row,2).data()
        print(star_rate, country, hotel_id, price, start_date, end_date,name_tour)

    ui.tableView.doubleClicked.connect(lambda index: selected(index))
    ui.tableView.doubleClicked.connect(open_order_form)

    def update_table():
        star_rate = ui.comboBox.currentText()
        country = ui.country.text()
        hotel_id = ui.hotel.text()
        price = ui.price.text()
        start_date = ui.dateEdit.date().toString("yyyy-MM-dd")
        end_date = ui.dateEdit_2.date().toString("yyyy-MM-dd")

        filtered_data = get_hotels_data(star_rate, country, hotel_id, price, start_date, end_date)
        populate_table(filtered_data)

    ui.filter.clicked.connect(update_table)


def no_dialog():
    global no
    no = QtWidgets.QFrame()
    no_ui = Ui_no()
    no_ui.setupUi(no)
    no.show()

def yes_dialog():
    global yes
    yes = QtWidgets.QFrame()
    yes_ui = Ui_yes()
    yes_ui.setupUi(yes)
    yes.show()

def auth():
    global name_login
    name_login = ui.login.text()
    password = ui.password.text()
    try:
        if check_query(connection, name_login, password):
            open_client_form()
            frame.close()
        else:
            no_dialog()
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def open_tours_from_clients():
    open_tours_form()

ui.autorization.clicked.connect(auth)

sys.exit(app.exec_())