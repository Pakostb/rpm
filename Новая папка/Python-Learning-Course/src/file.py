import tkinter as tk


root = tk.Tk()
root.title("Калькулятор TOP!!!")
root.geometry("600x500")




top_frame = tk.Frame(root, height=100, bg="midnightblue", padx=10, pady=10)
top_frame.pack(fill='x', side='top')


right_frame = tk.Frame(root, bg="midnightblue", padx=10, pady=10)
right_frame.pack(fill='y', side='right')


left_frame = tk.Frame(root, bg="midnightblue", padx=10, pady=10)
left_frame.pack(fill='both', expand=True, side='left')


input_label = tk.Label(top_frame, text='', font=("Arial", 20), bg="midnightblue", fg="white", anchor="e")
input_label.pack(fill="x", padx=10, pady=10)

a = ''


def calc(x):
    global a

    if x == '=':
        expr = a.replace('%', '/')
        res = "Ошибка"

        if expr != "":
            res = str(eval(expr))

        a = res
        input_label.configure(text=a)
        return


    if a == "Ошибка":
        a = ""


    a += f'{x}'
    input_label.configure(text=a)


states = [ "+", "-", "*", "%", ".", "=" ]

col = 0
row = 0


for btn in range(10):
    if col == 3:
        row += 1
        col = 0

    tk.Button(
        left_frame,
        text=btn,
        width=12,
        height=4,
        font=("Arial", 11, "bold"),
        command=lambda var=btn: calc(var)
    ).grid(row=row, column=col, padx=2, pady=2)
    col += 1

for state in states:
    tk.Button(
        right_frame,
        text=state,
        width=12,
        height=3,
        font=("Arial", 11, "bold"),
        bg="orange",
        command=lambda x=state: calc(x)
    ).pack(padx=2, pady=2, fill="x")

# Запуск
root.mainloop()