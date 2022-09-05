''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 

# віджети, які треба буде розмістити:
btn_Menu = QPushButton("Меню") 
btn_Sleep = QPushButton("Відпочити")
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_OK = QPushButton("Відповідь")
lb_Question = QLabel("")


# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу переGмикачів
RadioGroupBox = QGroupBox("Варіант відповідей") 
RadioGroup = QButtonGroup()

rbtn1 = QRadioButton ("")
rbtn2 = QRadioButton ("")
rbtn3 = QRadioButton ("")
rbtn4 = QRadioButton ("")

RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
# Опиши панень з результатами
AnsGroup = QGroupBox("Результати тесту")
lb_Result = QLabel("")#True False
lb_Correct = QLabel("")#100% True

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch= 2)
AnsGroup.setLayout(layout_res)
AnsGroup.hide()
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(QLabel("хвилин"))
layout_line1.addWidget(box_Minutes)

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroup)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2)
layout_line4.addStretch(1)

layout_card =QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) #пробіли між данними
# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    
    RadioGroupBox.hide()
    AnsGroup.show()
    btn_OK.setText("Наступне запитання")
def show_question():
    ''' показати панель запитань '''
    
    RadioGroupBox.show()
    AnsGroup.hide()
    btn_OK.setText("Відповісти")

    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
