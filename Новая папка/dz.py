import tkinter as tk

window = tk.Tk()
window.title("Калькулятор")
window.geometry("280x380")


text_input = tk.Label(window, text="", font=("Arial", 18), width=18, height=2, bg="white", relief="sunken")
text_input.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

expression = ""

def button_click(value):
    global expression
    if value == "=":
        try:
            result = eval(expression)
            text_input.config(text=str(result))
            expression = str(result)
        except:
            text_input.config(text="Ошибка")
            expression = ""
    else:
        expression = expression + str(value)
        text_input.config(text=expression)


numbers = [7, 8, 9, 4, 5, 6, 1, 2, 3, 0]
row = 1
col = 0

for num in numbers:
    btn = tk.Button(window, text=str(num), width=5, height=2, font=("Arial", 12),
                    command=lambda n=num: button_click(n))
    btn.grid(row=row, column=col, padx=2, pady=2)
    col = col + 1
    if col > 2:
        col = 0
        row = row + 1


operations = ["*", "%", "+", "-", "="]
op_row = 1

for op in operations:
    btn = tk.Button(window, text=op, width=5, height=2, font=("Arial", 12),
                    command=lambda o=op: button_click(o))
    btn.grid(row=op_row, column=3, padx=2, pady=2)
    op_row = op_row + 1

window.mainloop()