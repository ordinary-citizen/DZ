#Форма регистрации с проверкой вводимых полей
#и проверкой пароля на совпадение

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('VK')
window.geometry('450x450')
window.resizable(False, False)
window['bg'] = '#00BFFF'
window.iconbitmap('logo.ico')

#frame = Frame(window, bg='red')
#.frame.place(relx=0.1, rely=0.0, relheight=0.8, relwidth=0.8)
# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Georgia', 20)
font_entry = ('Arial', 12)
label_font = ('Arial', 12)
base_padding = {'padx': 10, 'pady': 5}
header_padding = {'padx': 10, 'pady': 12}



# обработчик нажатия на клавишу 'Зарегистрироваться'
def clicked():

    # получаем имя пользователя, email и пароль
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    passwordconfirm = passwordconfirm_entry.get()

    if password == passwordconfirm:
        if username and email and password:
            messagebox.showinfo('Поздравляем!', username + '  , Вы успешно зарегистрировались.')
        if not username and email:
            messagebox.showerror('Ошибка', 'Введите логин !')
        if not email and username:
            messagebox.showerror('Ошибка', 'Введите email !')
    else:
        messagebox.showerror('Ошибка', 'Пароли не совпадают !')

# заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
main_label = Label(window, text='Регистрация', bg='#00BFFF',  font=font_header, justify=CENTER, **header_padding)
main_label.pack()

# метка для поля ввода имени
username_label = Label(window, text='логин' + ' '*27, bg='#00BFFF', font=label_font , **base_padding)
username_label.pack()

# поле ввода имени
username_entry = Entry(window, bg='#ADD8E6', fg='#444', font=font_entry)
username_entry.pack()

# метка для поля ввода email
email_label = Label(window, text='email' + ' '*28, bg='#00BFFF', font=label_font , **base_padding)
email_label.pack()

# поле ввода email
email_entry = Entry(window, bg='#ADD8E6', fg='#444', font=font_entry)
email_entry.pack()

# метка для поля ввода пароля
password_label = Label(window, text='пароль' + ' '*25, bg='#00BFFF', font=label_font , **base_padding)
password_label.pack()

password_entry = Entry(window, bg='#ADD8E6', fg='#444', font=font_entry)
password_entry.pack()

passwordconfirm_label = Label(window, text='подтвердите пароль' + ' '*5, bg='#00BFFF', font=label_font , **base_padding)
passwordconfirm_label.pack()

passwordconfirm_entry = Entry(window, bg='#ADD8E6', fg='#444', font=font_entry)
passwordconfirm_entry.pack()

# кнопка отправки формы
send_btn = Button(window, text=' Зарегистрироваться', fg='#00BFFF', font='Tahoma 10', bg='#4682B4', command=clicked)
send_btn.pack(**base_padding)


# запускаем главный цикл окна
window.mainloop()
