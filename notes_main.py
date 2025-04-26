#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
import json 
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel,
 QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QPushButton, QButtonGroup, QTextEdit,
  QLineEdit, QListWidget, QInputDialog)

def show_note():
    name = List1.selectedItems()[0].text()
    big_window.setText(notes[name]['текст'])
    List2.clear()
    List2.addItems(notes[name]['теги'])
def add_note():
    note_name, ok = QInputDialog.getText(main_win, 
    'Добавить заметку','Название заметки')
    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги' : []}
        List1.addItem(note_name)
def del_note():
    if List1.selectedItems():
        key = List1.selectedItems()[0].text()
        del notes[key]

        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)
        List1.clear()
        List2.clear()
        big_window.clear() 
        List1.addItems(notes)
        print(notes)
    else:
        eror = QMessageBox()
        eror.setText('Заметка для удаления не выбрана!')
        eror.exec_()
def save_note():
    if List1.selectedItems():
        key = List1.selectedItems()[0].text()
        notes[key]['текст'] = big_window.toPlainText()
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        eror1 = QMessageBox()
        eror1.setText('Заметка для сохранения не выбрана!')
        eror1.exec_()
def add_tag():
    if List1.selectedItems():
        key = List1.selectedItems()[0].text()
        tag = new_teg.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            List2.addItem(tag)
            new_teg.clear()
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        eror2 = QMessageBox()
        eror2.setText('Тег для сохранения не выбран!')
        eror2.exec_()
def del_teg():
    if List2.selectedItems():
        key = List1.selectedItems()[0].text()
        tag = List2.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        List2.clear()
        List2.addItems(notes[key]['теги'])
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        eror3 = QMessageBox()
        eror3.setText('Тег для удаления не выбран!')
        eror3.exec_()
def search_teg():
    tag = new_teg.text()
    if button5.text() == 'Искать заметки по тегу' and tag:
        notes_filtreted = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtreted[note] = notes[note]
        button5.setText('Сбросить поиск')
        List1.clear()
        List2.clear()
        List1.addItems(notes_filtreted)
    elif button5.text() == 'Сбросить поиск':
        List1.clear()
        List2.clear()
        new_teg.clear()
        List1.addItems(notes)
        button5.setText('Искать заметки по тегу')
    else:
        eror3 = QMessageBox()
        eror3.setText('Тег для поиска не выбран!')
        eror3.exec_()

'''notes = { 
    'Добро пожаловать':
    {
        'текст' : 'В этом приложении можно сосдавать заметки с теггом',
        'теги'  : ['Умные заметки','Инструкция']
    }
}
with open('notes_data.json', 'w', encoding = 'utf-8') as file:
    json.dump(notes, file)'''

app = QApplication([])
main_win = QWidget()
main_win.resize(750, 500)
main_win.move(750, 200)
big_window = QTextEdit()
lable1 = QLabel('Список заметок')
lable2 = QLabel('Список тегов')
List1 = QListWidget()
List2 = QListWidget()
new_teg = QLineEdit()
new_teg.setPlaceholderText('Введите тег')
button = QPushButton('Сосдать заметку')
button1 = QPushButton('Удалить заметку')
button2 = QPushButton('Сохранить заметку')
button3 = QPushButton('Добавить к заметке ')
button4 = QPushButton('Открепить от заметки')
button5 = QPushButton('Искать заметки по тегу')
#Направляющие линии:
#Две вертикали
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
#Главная горизонталь
layoutH = QHBoxLayout()
#Горизонтали
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH5 = QHBoxLayout()
layoutH6 = QHBoxLayout()
layoutH7 = QHBoxLayout()
layoutH8 = QHBoxLayout()
layoutH9 = QHBoxLayout()
#Размещение направляющих линий:
v_line1.addWidget(big_window)

layoutH1.addWidget(lable1)
layoutH2.addWidget(List1, alignment = Qt.AlignCenter)
layoutH3.addWidget(button, alignment = Qt.AlignCenter)
layoutH3.addWidget(button1, alignment = Qt.AlignCenter)
layoutH4.addWidget(button2, alignment = Qt.AlignCenter)
layoutH5.addWidget(lable2)
layoutH6.addWidget(List2, alignment = Qt.AlignCenter)
layoutH7.addWidget(new_teg, alignment = Qt.AlignCenter)
layoutH8.addWidget(button3, alignment = Qt.AlignCenter)
layoutH8.addWidget(button4, alignment = Qt.AlignCenter)
layoutH9.addWidget(button5, alignment = Qt.AlignCenter)
v_line2.addLayout(layoutH1)
v_line2.addLayout(layoutH2)
v_line2.addLayout(layoutH3)
v_line2.addLayout(layoutH4)
v_line2.addLayout(layoutH5)
v_line2.addLayout(layoutH6)
v_line2.addLayout(layoutH7)
v_line2.addLayout(layoutH8)
v_line2.addLayout(layoutH9)
layoutH.addLayout(v_line1)
layoutH.addLayout(v_line2)
main_win.setLayout(layoutH)

with open('notes_data.json', 'r', encoding = 'utf-8') as file:
    notes = json.load(file)
print(notes)
List1.addItems(notes)
List1.itemClicked.connect(show_note)
button.clicked.connect(add_note)
button1.clicked.connect(del_note)
button2.clicked.connect(save_note)
button3.clicked.connect(add_tag)
button4.clicked.connect(del_teg)
button5.clicked.connect(search_teg)
main_win.show()
app.exec_()