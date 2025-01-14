from tkinter import *

with open("movies.txt", "r") as file:
    str1 = file.readline()
    str2 = file.readline()
    str3 = file.readline()
films = [str1, str2, str3]
# открывает текстовый док, считываем построчно

def changeBut(event):
    event.widget["background"] = "red"
# виджет, кнопочка меняется на красную

def for_knopki():
    root = Tk()
    for i in range(10):
        for j in range(10):
            but = Button(root,
                         background="#ccc",
                         foreground="#555",
                         padx="20",
                         pady="8",
                         # state= 'active',
                         font="16",
                         width="1",
                         )
            but.configure()
            but["text"] = str(j + 1)
            but.bind("<Button-1>", changeBut)
            # but.bind("<Button-1>", lambda event, but=but: changeBut(event, but))
            but.grid(row=i, column=j)
        lab = Label(root, text="ряд " + str(i + 1))
        lab.grid(row=i, column=(j + 1))

def kino():
    names = []
    for i in range(3):
        name = "Кинозал №" + str(i + 1)
        names.append(name)
    root = Tk()
    root.geometry("100x138")
    root.title("Бронирование мест")
    for i in range(3):
        but = Button(root, text=names[i],  # текст кнопки
                     background="#ccc",  # фоновый цвет кнопки
                     foreground="#555",  # цвет текста
                     padx="40",  # отступ от границ до содержимого по горизонтали
                     pady="8",  # отступ от границ до содержимого по вертикали
                     font="16",  # высота шрифта
                     width="12",  # ширина кнопки-
                     command=for_knopki
                     )
        but.pack()

nameq = []

for s in films:
    name = s
    nameq.append(name)
root = Tk()
root.geometry("400x189")
root.title("Сеансы на фильмы")
for q in range(3):
    but = Button(root, text=films[q],  # текст кнопки
                background="#ccc",  # фоновый цвет кнопки
                foreground="#555",  # цвет текста
                padx="400",  # отступ от границ до содержимого по горизонтали
                pady="8",  # отступ от границ до содержимого по вертикали
                font="16",  # высота шрифта
                width="12",  # ширина кнопки
                command=kino
                )
    but.pack()

board = list(range(1, 10))
root.mainloop()
