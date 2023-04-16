from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import randint, shuffle
 


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
list_question = list()

#Вопрос 1
question_list = []
p1 = Question('Какой национальности не существует?', 'Энцы', 'Смурфа', 'Чулымцы', 'Алеуты')
#Вопрос2
q2 = Question('Как выглядет житель Якутса', 'Синим', 'Фиолетовым', 'Черным', 'Светлым')
question_list.append(q2)
#Вопрос3
q3 = Question('Что будет делать свами админ если вы с читами', 'БАН', 'КИК', 'Отпустет', 'БАН:IP')
question_list.append(q3)
#Вопрос4
q4 = Question('Кто такой Ю́рий Бори́сович Левита́н', 'диктор', 'Инженер', 'Юрист', 'Фокусник')
question_list.append(q4)
#Вопрос5
q5 = Question('Кто такой крыса', 'Тот кто нападает со спины', 'Чел крыса', 'Мутант', 'Что-то')
question_list.append(q5)
#Вопрос6
q6 = Question('Кто призедент Росий', 'Путин', 'АБАБА', 'Люкашенка', 'Сампайю')
question_list.append(q6)
#Вопрос5
q7 = Question('Кто правит миром', 'Россия', 'США', 'Евросоюз', 'Нато')
question_list.append(q7)
#Вопрос8
q8 = Question('Кто такой Кирил', 'Рандом чел', 'Друг', 'Недруг', 'Однакласник')
question_list.append(q8)
#Вопрос9
q9 = Question('Какой город является столицей нашего государства? ', 'Москва', 'Санкт-Петербург', 'Севастополь', 'Киев')
question_list.append(q9)
#Вопрос10
q10 = Question('Сколько будет 9*9', '81', '18', '64', '12')
question_list.append(q10)
#Вопрос11
q11 = Question('Какой язык объединяет народы России?', 'Руский', 'Англиский', 'Китайски', 'Украинский')
question_list.append(q11)
#Вопрос12
q12 = Question('Сколько будет 2+2=', '4', '98', '18', '6')
question_list.append(q12)
#Вопрос13
q13 = Question('Как называется основной закон Российской Федерации?', 'Конституция', 'Закон', 'Правила', 'Обман')
question_list.append(q13)
#Вопрос14
q14 = Question('На каком материке находится Россия?', 'Евразия', 'Африка', 'Австралия', 'Южная Америка')
question_list.append(q14)
#Вопрос15
q15 = Question('Совокупное название граждан России', 'Россияне', 'Африканцы', 'Американцы', 'Автралиций')
question_list.append(q15)
#Вопрос16
q16 = Question('Сколько будет 48:2', '24', '12', '6', '2')
question_list.append(q16)
#Вопрос17
q17 = Question('Как продать видиокарту', 'Через интернет', 'На рынке', 'Береш и продаешь', 'Через знакомово')
question_list.append(q17)
#Вопрос18
q18 = Question('Кто такой Ленин', 'Революционер', 'Царь', 'Император', 'Гриб')
question_list.append(q18)
#Вопрос19
q19 = Question('Сколко будет 52-12', '40', '12', '8', '19')
question_list.append(q19)
#Вопрос20
q20 = Question('Когда появился первый персонал компьютер', '1977', '1934', '1945', '1965')
question_list.append(q20)
def next_question():
    window.total += 1
    print("Статистика\n-Всего вопросов:", window.total, '\nПравилных ответов', window.score)
    cur_question = randint (0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Какой национальности не существует?')
 
RadioGroupBox = QGroupBox("Вырианты ответов") 
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфа')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    #''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
#''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    #''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    #при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question()

def show_correct(res):
    #''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    #''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print("Стастика\n-Всего вопрсов:", window.total, '\n-Правильный ответ:', window.score)
        print("Рейтинг:", (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print("Рейтинг:", (window.score/window.total*100), '%')
def click_OK():
    #Определяет надо показывать другой вопрос либо проверить ответ на этот
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.resize(400,300)
q = Question('Какой национальности не существует?', 'Энцы', 'Смурфа', 'Чулымцы', 'Алеуты')
ask(q)
btn_OK.clicked.connect(click_OK) 

window.score = 1
window.total = 1
ask(p1)
window.show()
app.exec()

