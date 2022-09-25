#Генератор пароля с выбором вводимых символов
from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title('Генератор пароля')
window.geometry('450x450')
window.resizable(False, False)
window['bg'] = '#00BFFF'
window.iconbitmap('logo.ico')

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Georgia', 20)
font_entry = ('Arial', 12)
label_font = ('Arial', 12)
base_padding = {'padx': 10, 'pady': 10}
header_padding = {'padx': 10, 'pady': 12}

# обработчик нажатия на клавишу 'Генерировать пароль'
def clicked():

    # получаем длину пароля, и ответы на вопросы
    l  = l_entry.get()
    l1 = int(l)
    rus = str.lower(rus_entry.get())
    spec = str.lower(spec_entry.get())
    pas = "abcdefghijklmnopqrstuvwxyz"
    pas = pas + str.upper(pas)

    if rus == 'да' and spec == 'да':
        pas2 = 'абвгдежзийклмнопрстуфхцчшщъыьэю'
        pas = pas + pas2 + str.upper(pas2) + '!;%:?*(){}+-'
    else:
        if spec == 'да':
            pas = pas + '!;%:?*(){}+-'

    password = ''
    i = 0
    while i < l1:
        h = random.choice(pas)
        password = password + h
        i += 1
    msg = Message(window, bg='#ADD8E6', fg='#32CD32', font='Arial 15', justify=CENTER, width=450, padx=20, text=(password))
    msg.pack()


# заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
main_label = Label(window, text='Генератор пароля', bg='#00BFFF',  font=font_header, justify=CENTER, **header_padding)
main_label.pack()

# метка для поля ввода имени
l_label = Label(window, text='Длина пароля', bg='#00BFFF', font=label_font , **base_padding)
l_label.pack()

# поле ввода длины пароля
l_entry = Entry(window, bg='#ADD8E6', fg='#444', font=font_entry)
l_entry.pack()

# метка для поля ввода ответа rus
rus_label = Label(window, text='Нужны ли в пароле русские буквы?', bg='#00BFFF', font=label_font , **base_padding)
rus_label.pack()

# поле ввода ввода ответа rus
rus_entry = Entry(window, bg='#ADD8E6', fg='#444', font=font_entry)
rus_entry.pack()

# метка для поля ввода ответа spec
spec_label = Label(window, text='Нужны ли в пароле спецсимволы?', bg='#00BFFF', font=label_font , **base_padding)
spec_label.pack()

spec_entry = Entry(window, bg='#ADD8E6', fg='#444', font=font_entry)
spec_entry.pack()

# кнопка отправки формы
send_btn = Button(window, text='Генерировать пароль', fg='#00BFFF', font='Tahoma 10', bg='#4682B4', command=clicked)
send_btn.pack(**base_padding)

# Запуск окна
window.mainloop()
