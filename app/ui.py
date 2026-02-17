from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QLabel, QTextEdit, QLineEdit,
    QTabWidget
)

from logic import (
    square_generator,
    note_list_generator,
    common_coins
)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generators App")
        self.resize(700, 500)

        layout = QVBoxLayout()

        tabs = QTabWidget()

        tabs.addTab(self.tab1(), "Площади")
        tabs.addTab(self.tab2(), "Ноты")
        tabs.addTab(self.tab3(), "Монеты")

        layout.addWidget(tabs)
        self.setLayout(layout)

    

    def tab1(self):

        widget = QWidget()
        layout = QVBoxLayout()

        self.area_output = QTextEdit()
        self.area_output.setReadOnly(True)

        btn = QPushButton("Показать первые 100")

        btn.clicked.connect(self.show_areas)

        layout.addWidget(btn)
        layout.addWidget(self.area_output)

        widget.setLayout(layout)
        return widget

    def show_areas(self):

        self.area_output.clear()

        gen = square_generator()

        for i in range(100):
            self.area_output.append(str(next(gen)))

    

    def tab2(self):

        widget = QWidget()
        layout = QVBoxLayout()

        self.notes_output = QTextEdit()
        self.notes_output.setReadOnly(True)

        btn = QPushButton("Сгенерировать 10x10")

        btn.clicked.connect(self.show_notes)

        layout.addWidget(btn)
        layout.addWidget(self.notes_output)

        widget.setLayout(layout)
        return widget

    def show_notes(self):

        self.notes_output.clear()

        matrix = note_list_generator(10, 10)

        for row in matrix:
            self.notes_output.append(" ".join(row))

    

    def tab3(self):

        widget = QWidget()
        layout = QVBoxLayout()

        self.input1 = QLineEdit()
        self.input2 = QLineEdit()

        self.input1.setPlaceholderText("Список Саши")
        self.input2.setPlaceholderText("Список Гали")

        btn = QPushButton("Найти общие чётные")

        self.coins_output = QLabel()

        btn.clicked.connect(self.show_coins)

        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(btn)
        layout.addWidget(self.coins_output)

        widget.setLayout(layout)
        return widget

    def show_coins(self):

        try:
            f = list(map(int, self.input1.text().split()))
            g = list(map(int, self.input2.text().split()))

            result = common_coins(f, g)

            self.coins_output.setText(
                "Результат: " + str(result)
            )

        except ValueError:
            self.coins_output.setText("Ошибка: введите числа!")
