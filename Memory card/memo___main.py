from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer

from memo___app import app
from memo___card_layout import*
from memo___data import *
from memo___main_layout import *
from memo___edit_layout import *



card_width, card_height = 600, 500 # розміри вікна "карточка"
main_width, main_height = 1000, 450 #розміри головного вікна
time_unit = 1000  # тривалість одиниці часу 


question_listmodel = QuestionListModel() #список запитань
radio_list = [rbtn1, rbtn2, rbtn3, rbtn4]
frm_card = 0 #звязок запитання з формою тесту
win_card = QWidget()
win_main = QWidget()
timer = QTimer()
frm_edit = QuestionEdit(0, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)


def testlist():

    frm = Question('Яблоко','apple',  'application','building','caterpillar')
    question_listmodel.form_list.append(frm)
    frm = Question('Будинок','house',  'husband','horny','horse')
    question_listmodel.form_list.append(frm)
    frm = Question('Гра','game',  'play','gaming','cosplay')
    question_listmodel.form_list.append(frm)
#################
def set_card ():
    win_card.resize(card_width, card_height)
    win_card.move(300, 300)
    win_card.setWindowTitle('Memory Card')
    win_card.setLayout(layout_card)

def sleep_card():
    #картка ховаться на вказаний час
    win_card.hide()
    timer.setInterval(time_unit*box_Minutes.value())
    timer.start()

def show_card():
    win_card.show()
    timer.stop()

def show_random():
    global frm_card
    frm_card = random_AnswerCheck(question_listmodel, lb_Question, radio_list, lb_Correct, lb_Result)

    frm_card.show()
    show_question()


def click_OK(self):
    # пока что проверяем вопрос, если мы в режиме вопроса, иначе ничего
    if btn_OK.text() != 'Наступне запитання':
       frm_card.check()
       show_result()
    else:
        show_random()

def back_to_menu():
    win_card.hide()
    win_main.showNormal()

#################################
def set_main():
    win_main.resize(main_width, main_height)
    win_main.move(100, 100)
    win_main.setWindowTitle("Список запитань")
    win_main.setLayout(layout_main)

def edit_question(index):
    if index.isValid():
        i = index.row()
        frm = question_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()

def add_form():
    question_listmodel.insertRows()
    last = question_listmodel.rowCount(0)-1

    index = question_listmodel.index(last)
    edit_question(index)
    txt_Question.setFocus(Qt.TabFocusReason)

def del_form():
    question_listmodel.removeRows(list_question.currentIndex().row())
    edit_question(list_question.currentIndex())

def start_test():
    show_random()
    win_card.show()
    win_main.showMinimized()

#############################################
def connects():
    list_question.setModel(question_listmodel)#звязуємо список на екрані зі списком наших запитань
    list_question.clicked.connect(edit_question)
    btn_add.clicked.connect(add_form)
    btn_del.clicked.connect(del_form)
    btn_start.clicked.connect(start_test)
    btn_OK.clicked.connect(click_OK)
    btn_Menu.clicked.connect(back_to_menu)
    btn_Sleep.clicked.connect(sleep_card)
    timer.timeout.connect(show_card)

####################### ЗАПУСК ПРОГРАМИ ########################

testlist()
set_card()
set_main()
connects()
win_main.show()
app.exec_()