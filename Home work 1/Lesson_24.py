# # fruits = ["apple", "banana", "cherry"]
# # # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# # for index, fruit in enumerate(fruits): # (0, 'apple')
# #     print(f"{index}: {fruit}")
# #
# # numbers = [10, 20, 15, 30, 25, 35]
# #
# # for index, value in enumerate(numbers[:-1]):  # Проходим по списку, кроме последнего элемента
# #     if value > numbers[index + 1]:  # 10 > 20
# #         print(f"{value} больше, чем {numbers[index + 1]}")
# #
# # for index, value in enumerate(numbers[:-1], start=1):  # Проходим по списку, кроме последнего элемента
# #     if value > numbers[index]:  # 10 > 20
# #         print(f"{value} больше, чем {numbers[index]}")
#
# '''
# Кортеж уникальных
# Напишите программу, которая обрабатывает кортеж чисел. Программа должна вернуть
# кортеж, в котором будут только уникальные элементы.
# Не используйте неизученные коллекции.
#
# Данные:
# numbers = (1, 2, 3, 2, 1, 4, 5, 3, 6)
#
# Пример вывода:
# Уникальные элементы: (1, 2, 3, 4, 5, 6)
# '''
# # num_ = (1, 2, 3, 2, 1, 4, 5, 3, 6)
# #
# # unique_num = ()
# # for num in num_:
# #     if num not in unique_num:
# #         unique_num += (num,)
# #
# # print(f"Уникальные элементы: {unique_num}")
# #
#
# '''
# Кортеж выше среднего
# Напишите программу, которая обрабатывает кортеж чисел. Программа должна вернуть кортеж, состоящий из элементов, которые больше среднего значения всех элементов исходного кортежа.
# Данные:
# numbers = (10, 15, 20, 25, 30)
# Пример вывода:
# Элементы больше среднего: (25, 30)
# '''
#
# numbers = (10, 15, 20, 25, 30)
#
# # Находим среднее значение
# average = sum(numbers) / len(numbers)
#
# # Формируем новый кортеж с элементами больше среднего
# above_average = ()
# for num in numbers:
#     if num > average:
#         above_average += (num,)
#
# print(f"Элементы больше среднего: {above_average}")
#
#
# '''
# Генерация отчёта о студентах
# Напишите программу, которая обрабатывает список кортежей, где каждый кортеж содержит имя студента, количество набранных баллов и максимальное количество баллов. Программа должна вывести таблицу с именем, баллом и статусом ("Зачёт" или "Незачёт", если оценка меньше 50). Вывести в соответствии с примером.
# Данные:
# students = [
#     ("Алексей", 80, 100),
#     ("Мария", 50, 100),
#     ("Дмитрий", 70, 100),
#     ("Екатерина", 40, 100)
# ]
#
# Пример вывода:
# Имя             Процент      Статус
# -----------------------------------
# Алексей           80.00       Зачёт
# Мария             50.00       Зачёт
# Дмитрий           70.00       Зачёт
# Екатерина         40.00     Незачёт
# '''
Daniil
Boiko, [15.04.2025 23: 00]
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QColorDialog, QDialog, QDialogButtonBox, QHBoxLayout
)
from PyQt5.QtGui import QFont, QPalette, QColor, QLinearGradient, QBrush
from PyQt5.QtCore import Qt, QTimer, QDateTime


class BeautifulApp(QWidget):
    def init(self):
        super().init()
        self.setWindowTitle("Красивое PyQt5-приложение")
        self.setGeometry(200, 200, 400, 350)
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        # Шрифты
        title_font = QFont("Arial", 18, QFont.Bold)
        text_font = QFont("Arial", 12)

        # Виджеты
        self.label_title = QLabel("Добро пожаловать!", self)
        self.label_title.setFont(title_font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Введите ваше имя")
        self.input.setFont(text_font)

        self.button_hello = QPushButton("Сказать привет", self)
        self.button_hello.setFont(text_font)
        self.button_hello.clicked.connect(self.say_hello)

        self.button_change_bg = QPushButton("Изменить фон", self)
        self.button_change_bg.setFont(text_font)
        self.button_change_bg.clicked.connect(self.change_background)

        self.button_info = QPushButton("Информация о приложении", self)
        self.button_info.setFont(text_font)
        self.button_info.clicked.connect(self.show_info)

        self.output = QLabel("", self)
        self.output.setFont(text_font)
        self.output.setAlignment(Qt.AlignCenter)

        # Текущее время
        self.time_label = QLabel("", self)
        self.time_label.setFont(text_font)
        self.time_label.setAlignment(Qt.AlignCenter)

        # Обновление времени каждую секунду
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.input)
        layout.addWidget(self.button_hello)
        layout.addWidget(self.button_change_bg)
        layout.addWidget(self.button_info)
        layout.addWidget(self.output)
        layout.addWidget(self.time_label)
        self.setLayout(layout)

    def say_hello(self):
        name = self.input.text().strip()
        if name:
            self.output.setText(f"🌸 Привет, {name}! 🌸")
        else:
            self.output.setText("Пожалуйста, введите имя 🌿")

    def change_background(self):
        color = QColorDialog.getColor()
        if color.isValid():
            palette = QPalette()
            palette.setColor(QPalette.Window, color)
            self.setPalette(palette)

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.time_label.setText(f"Текущее время: {current_time}")

    def show_info(self):
        info_dialog = QDialog(self)
        info_dialog.setWindowTitle("Информация")

        info_label = QLabel("Это простое PyQt5-приложение, демонстрирующее\n"
                            "работу с графическим интерфейсом, цветами,\n"
                            "временем и взаимодействием с пользователем.", info_dialog)
        info_label.setFont(QFont("Arial", 12))

        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.rejected.connect(info_dialog.reject)

        layout = QVBoxLayout()
        layout.addWidget(info_label)
        layout.addWidget(buttons)
        info_dialog.setLayout(layout)

        info_dialog.exec_()

    def apply_styles(self):
        # Градиент фона
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#ffecd2"))
        gradient.setColorAt(1.0, QColor("#fcb69f"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)


Daniil
Boiko, [15.04.2025 23: 00]
# Стили для кнопки и поля ввода
self.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #f8cdda;
                border-radius: 10px;
                background-color: #fffaf0;
            }
            QPushButton {
                background-color: #f6d365;
                border: none;
                padding: 10px;
                border-radius: 15px;
                color: #4b3832;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #fda085;
            }
            QLabel {
                color: #4b3832;
            }
        """)
Daniil
Boiko, [15.04.2025 23: 00]
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QColorDialog, QDialog, QDialogButtonBox, QHBoxLayout
)
from PyQt5.QtGui import QFont, QPalette, QColor, QLinearGradient, QBrush
from PyQt5.QtCore import Qt, QTimer, QDateTime


class BeautifulApp(QWidget):
    def init(self):
        super().init()
        self.setWindowTitle("Красивое PyQt5-приложение")
        self.setGeometry(200, 200, 400, 350)
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        # Шрифты
        title_font = QFont("Arial", 18, QFont.Bold)
        text_font = QFont("Arial", 12)

        # Виджеты
        self.label_title = QLabel("Добро пожаловать!", self)
        self.label_title.setFont(title_font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Введите ваше имя")
        self.input.setFont(text_font)

        self.button_hello = QPushButton("Сказать привет", self)
        self.button_hello.setFont(text_font)
        self.button_hello.clicked.connect(self.say_hello)

        self.button_change_bg = QPushButton("Изменить фон", self)
        self.button_change_bg.setFont(text_font)
        self.button_change_bg.clicked.connect(self.change_background)

        self.button_info = QPushButton("Информация о приложении", self)
        self.button_info.setFont(text_font)
        self.button_info.clicked.connect(self.show_info)

        self.output = QLabel("", self)
        self.output.setFont(text_font)
        self.output.setAlignment(Qt.AlignCenter)

        # Текущее время
        self.time_label = QLabel("", self)
        self.time_label.setFont(text_font)
        self.time_label.setAlignment(Qt.AlignCenter)

        # Обновление времени каждую секунду
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.input)
        layout.addWidget(self.button_hello)
        layout.addWidget(self.button_change_bg)
        layout.addWidget(self.button_info)
        layout.addWidget(self.output)
        layout.addWidget(self.time_label)
        self.setLayout(layout)

    def say_hello(self):
        name = self.input.text().strip()
        if name:
            self.output.setText(f"🌸 Привет, {name}! 🌸")
        else:
            self.output.setText("Пожалуйста, введите имя 🌿")

    def change_background(self):
        color = QColorDialog.getColor()
        if color.isValid():
            palette = QPalette()
            palette.setColor(QPalette.Window, color)
            self.setPalette(palette)

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.time_label.setText(f"Текущее время: {current_time}")

    def show_info(self):
        info_dialog = QDialog(self)
        info_dialog.setWindowTitle("Информация")

        info_label = QLabel("Это простое PyQt5-приложение, демонстрирующее\n"
                            "работу с графическим интерфейсом, цветами,\n"
                            "временем и взаимодействием с пользователем.", info_dialog)
        info_label.setFont(QFont("Arial", 12))

        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.rejected.connect(info_dialog.reject)

        layout = QVBoxLayout()
        layout.addWidget(info_label)
        layout.addWidget(buttons)
        info_dialog.setLayout(layout)

        info_dialog.exec_()

    def apply_styles(self):
        # Градиент фона
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#ffecd2"))
        gradient.setColorAt(1.0, QColor("#fcb69f"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)


Daniil
Boiko, [15.04.2025 23: 00]
# Стили для кнопки и поля ввода
self.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #f8cdda;
                border-radius: 10px;
                background-color: #fffaf0;
            }
            QPushButton {
                background-color: #f6d365;
                border: none;
                padding: 10px;
                border-radius: 15px;
                color: #4b3832;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #fda085;
            }
            QLabel {
                color: #4b3832;
            }
        """)

