import tkinter as tk


def button_clicked():
    result.config(text=f'{round(float(user_input.get())*1.6, 2)}')


window = tk.Tk()
window.title('Miles to Kilometers')
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)

user_input = tk.Entry(width=10)
user_input.grid(column=1, row=1)

label1 = tk.Label(text='km', font=('Arial', 12, 'normal'))
label1.grid(column=2, row=1)
label1.config(padx=20, pady=20)

label2 = tk.Label(text='is equal to', font=('Arial', 12, 'normal'))
label2.grid(column=0, row=2)

label3 = tk.Label(text='miles', font=('Arial', 12, 'normal'))
label3.grid(column=2, row=2)

result = tk.Label(text='0')
result.grid(column=1, row=2)
result.config(padx=20, pady=20)

button = tk.Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()