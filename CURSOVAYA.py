from tkinter import *
#from tkinter import ttk
import tkinter.font as tkFont
import time
import random
import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.radio = tk.StringVar()
        self.radio2 = tk.StringVar()
        self.radio3 = tk.StringVar()
        self.radio4 = tk.StringVar()
        self.radio.set("green")
        self.radio.trace("w", self.mark_radio)
        self.radio2.set("gold")
        self.radio2.trace("w", self.mark_radio)
        self.radio3.set("5")
        self.radio3.trace("w", self.mark_radio)
        self.radio4.set("1")
        self.radio4.trace("w", self.mark_radio)
        menu = tk.Menu(self)

        submenu = tk.Menu(menu, tearoff=0)
        submenu.add_separator()
        submenu.add_radiobutton(label="Зеленый", value="green",
                                variable=self.radio)
        submenu.add_radiobutton(label="Синий", value="blue",
                                variable=self.radio)
        submenu.add_radiobutton(label="Серый", value="gray",
                                variable=self.radio)

        submenu2 = tk.Menu(menu, tearoff=0)
        submenu2.add_separator()
        submenu2.add_radiobutton(label="Золотой", value="gold",
                                 variable=self.radio2)
        submenu2.add_radiobutton(label="Фиолетовый", value="violet",
                                 variable=self.radio2)
        submenu2.add_radiobutton(label="Белый", value="white",
                                 variable=self.radio2)

        submenu3 = tk.Menu(menu, tearoff=0)
        submenu3.add_separator()
        submenu3.add_radiobutton(label="Скорость 1", value="5",
                                variable=self.radio3)
        submenu3.add_radiobutton(label="Скорость 2", value="3",
                                variable=self.radio3)
        submenu3.add_radiobutton(label="Скорость 3", value="1",
                                variable=self.radio3)

        submenu4 = tk.Menu(menu, tearoff=0)
        submenu4.add_separator()
        submenu4.add_radiobutton(label="Круг", value="1",
                                 variable=self.radio4)
        submenu4.add_radiobutton(label="Квадрат", value="2",
                                 variable=self.radio4)

        menu.add_cascade(label="Цвет фона", menu=submenu)
        menu.add_cascade(label="Цвет змейки", menu=submenu2)
        menu.add_cascade(label="Скорость змейки", menu=submenu3)
        menu.add_cascade(label="Форма элементов змейки", menu=submenu4)
        menu.add_command(label="Запуск игры", command=self.destroy)
        self.config(menu=menu)

    def mark_radio(self, *args):
        global colorbgr, colorsnake, speedsnake, formsnake
        colorbgr = self.radio.get() #Цвет фона
        colorsnake = self.radio2.get() # Цвет змейки
        speedsnake = self.radio3.get() #Скорость змейки
        formsnake = self.radio4.get()  # Форма элементов змейки


if __name__ == "__main__":
    app = App()
    app.geometry("630x200")
    app.mainloop()


# Рисование одного элемента змейки
def draw_element(x, y):
    if formsnake == "1":
        canvas.create_oval((x + 1) * 25, (y + 1) * 25, (x + 2) * 25, (y + 2) * 25, fill=colorsnake)
    else:
        canvas.create_rectangle((x + 1) * 25, (y + 1) * 25, (x + 2) * 25, (y + 2) * 25, fill=colorsnake)

# Рисование змейки
def draw_snake():
    global table_x, table_y
    i = 0
    while i < len(table_x):
        draw_element(table_x[i], table_y[i])
        i += 1


# Изменения направления змейки
def left(event):
    global vx, vy
    vx = -1
    vy = 0


def right(event):
    global vx, vy
    vx = 1
    vy = 0


def up(event):
    global vx, vy
    vx = 0
    vy = -1


def down(event):
    global vx, vy
    vx = 0
    vy = 1


# Рисование поля
def draw_field():
    canvas.create_rectangle(0, 0, (30 + 2) * 25, (20 + 2) * 25, fill='brown')
    canvas.create_rectangle(25, 25, (30 + 1) * 25, (20 + 1) * 25, fill=colorbgr)


# Рисование яблока
def draw_bonus():
    global xb, yb
    canvas.create_oval((xb + 1) * 25, (yb + 1) * 25, (xb + 2) * 25, (yb + 2) * 25, fill='red')

# Рисование препятствий
def draw_wall():
    global xw, yw
    canvas.create_rectangle(xw*25, yw*25, (xw+1)*25, (yw+1)*25, fill='black')
    canvas.create_rectangle(xw*25, (yw+1)*25, (xw+1)*25, (yw+2)*25, fill='black')



# Рисование счетчика съеденных яблок
def draw_counter():
    canvas.create_text(50, 50, fill='yellow', font='Arial 15', text=counter)

# Рисование всего
def draw_all():
    draw_field()
    draw_wall()
    draw_snake()
    draw_bonus()
    draw_counter()
    canvas.update()


# Назначение главного окна
root = Tk()
# Настройка окна
root.title('Компьютерная игра "Змейка"')
root.geometry('800x600')
root.resizable(width=False, height=False)
root['bg'] = 'white'
root.iconbitmap('logo.ico')


# Создание окна для рисования
canvas = Canvas(root, bg='brown', width=800, height=550)
canvas.pack()

# Координаты элементов змейки
table_x = [11, 12, 13, 14]
table_y = [3, 3, 3, 3]
counter = 0

# Координаты яблока
xb = 5
yb = 5

# Направление змейки
vx = -1
vy = 0

# Координаты препятствия
xw = 20
yw = 14

# События bind
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)

win = True
# Запуск игры
while win:
    # Переход от одного края поля к другому
    if (table_x[0] == 0) and (vx == -1):
        table_x[0] = 29
    if (table_x[0] == 29) and (vx == 1):
        table_x[0] = 0
    if (table_y[0] == 0) and (vy == -1):
        table_y[0] = 19
    if (table_y[0] == 19) and (vy == 1):
        table_y[0] = 0

    table_x = [table_x[0] + vx] + table_x # Изменяем координаты змейки по оси x
    table_y = [table_y[0] + vy] + table_y # Изменяем координаты змейки по оси y

    if (table_x[0] != xb) or (table_y[0] != yb):
        table_x.pop(-1) # Удаляем последний элемент списка (змейки)
        table_y.pop(-1) # Удаляем последний элемент списка (змейки)
    else:
        counter += 1
        xb = random.randint(0, 29)
        yb = random.randint(0, 19)
        if xb == xw and yb == yw: # Проверка совпадения кооринат яблока и препятствия
            xb = random.randint(0, 29)
            yb = random.randint(0, 19)



    # Проигрыш змейки
    if (table_x[0] == (xw-1)) and (table_y[0] == (yw-1)) or (table_x[0] == (xw-1)) and (table_y[0] == yw):
        win = False # Столкновение с препятствием
    i = 1
    while i < len(table_x):  # Перебор элементов змейки, начиная со второго
        if (table_x[0] == table_x[i]) and (table_y[0] == table_y[i]):
            win = False
        i += 1


    draw_all() # Рисование всех объектов
    time.sleep(int(speedsnake)*0.1) # Скорость змейки
    canvas.delete('all') # Очищаем холст (canvas)
canvas.create_text(400, 275, text='    Вы проиграли ((\n Съеденных яблок '+ str(counter), fill='Snow', font='Arial 20')

# Запуск окна
root.mainloop()
