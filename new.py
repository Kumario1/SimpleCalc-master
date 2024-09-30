import tkinter

import tkinter as tk

def button_click(number):
    current_text = entry.get()
    new_text = current_text + str(number)
    entry.delete(0, tk.END)  
    entry.insert(0, new_text)  


root = tk.Tk()
root.title("Simple Calculator")

s = 12
entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


button0 = tk.Button(root, text="0", command=lambda: button_click(0), width=10, height=2)
button1 = tk.Button(root, text="1", command=lambda: button_click(1), width=5, height=2)
button2 = tk.Button(root, text="2", command=lambda: button_click(2), width=5, height=2)
button3 = tk.Button(root, text="3", command=lambda: button_click(3), width=5, height=2)
button4 = tk.Button(root, text="4", command=lambda: button_click(4), width=5, height=2)
button5 = tk.Button(root, text="5", command=lambda: button_click(5), width=5, height=2)
button6 = tk.Button(root, text="6", command=lambda: button_click(6), width=5, height=2)
button7 = tk.Button(root, text="7", command=lambda: button_click(7), width=5, height=2)
button8 = tk.Button(root, text="8", command=lambda: button_click(8), width=5, height=2)
button9 = tk.Button(root, text="9", command=lambda: button_click(9), width=5, height=2)
button10 = tk.Button(root, text="+", command=lambda: button_click("+"), width=4, height=2)
button11 = tk.Button(root, text="-", command=lambda: button_click("-"), width=4, height=2)
button12 = tk.Button(root, text="*", command=lambda: button_click("*"), width=4, height=2)
button13 = tk.Button(root, text="/", command=lambda: button_click("/"), width=4, height=2)


button0.grid(row=4, column=1)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button10.grid(row=5, column=0)
button11.grid(row=5, column=1)
button12.grid(row=5, column=2)
button13.grid(row=5, column=3)


root.mainloop()