from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox, QListView)
from memo___app import app
from memo___edit_layout import layout_form
from memo___card_layout import layout_card

list_question = QListView()
w_edit = QWidget()
w_edit.setLayout(layout_form)
btn_add = QPushButton("Нове запитання")
btn_del = QPushButton("Видалити запитання")
btn_start = QPushButton("Почати тренування")

main_col1 = QVBoxLayout()
main_col1.addWidget(list_question)
main_col1.addWidget(btn_add)

main_col2 = QVBoxLayout()
main_col2.addWidget(w_edit)
main_col2.addWidget(btn_del)

main_line1 = QHBoxLayout()
main_line1.addLayout(main_col1)
main_line1.addLayout(main_col2)

main_line2 = QHBoxLayout()
main_line2.addStretch(1)
main_line2.addWidget(btn_start, stretch=2)
main_line2.addStretch(1)

layout_main = QVBoxLayout()
layout_main.addLayout(main_line1)
layout_main.addLayout(main_line2)