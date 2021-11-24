import tkinter as tk
# Компилляция проекта: pyinstaller.exe --onefile --noconsole --icon=ico.ico main.py

# Настройки главного окна
mainwindow = tk.Tk()
mainwindow.title('PyCalc')
mainwindow.geometry('500x550')
mainwindow.resizable(False, False)
mainwindow.configure(bg="orange")
photo = tk.PhotoImage(file='ico.png')
mainwindow.iconphoto(False, photo)

# Функции:
# Вычисление
def calc(operation):
    # Заглушка pass
    # pass
    global result

    if operation == 'C':
        result = '0'

    elif operation == 'Del':
        result = result[0:-1]
        if result == '':
            result = '0'

    elif operation == 'x^2':
        result = str((eval(result)) ** 2)

    elif operation == '=':
        result = str(eval(result))

    else:
        if result == '0':
            result = ''
        result += operation
    label_result.configure(text=result)


# ShowBox
result = '0'
label_result = tk.Label(text=result, font=('Roboto', 30, 'bold'), bg='orange', fg='black')
label_result.place(x=11, y=50)

# Кнопки
buttons = ['C', 'Del', '*', '=', '1', '2', '3', '/', '4', '5', '6', '+', '7', '8', '9', '-', '+/-', '0', '%', 'x^2']
# Отсупы
bx = 18
by = 140

for bplace in buttons:
    get_lbl = lambda cx=bplace: calc(cx)
    tk.Button(text=bplace,
              bg='orange',
              command=get_lbl,
              font=('Roboto', 20)).place(x=bx, y=by, width=115, height=79)
    bx += 117
    if bx > 400:
        bx = 18
        by += 81

# if __name__ == '__main__':
#    print("Hello, i am PyCalc!")
# lambda test
# square = lambda a, b: a*b
# print(square(5,5))

mainwindow.mainloop()
