import tkinter as tk

class SimpleCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('+', 4, 1), ('=', 4, 2), ('C', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, padx=20, pady=10, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, value):
        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, value)

def main():
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
