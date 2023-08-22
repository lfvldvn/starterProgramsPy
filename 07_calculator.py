import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_display()
        self.create_buttons()

        # Captura de teclas do teclado
        self.root.bind("<KeyPress>", self.key_pressed)
        self.root.bind("<KeyRelease>", self.key_released)

        # Foco na entrada de texto
        self.entry_display.focus_set()

    def create_display(self):
        entry_display = ttk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 20), justify="right")
        entry_display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=100, ipady=10)
        self.entry_display = entry_display

    def create_buttons(self):
        style = ttk.Style()
        style.configure("Calculator.TButton", font=("Helvetica", 16), padding=(0, 0), background="lightgray", foreground="black")  

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            (",", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3)
        ]

        for (text, row, column) in buttons:
            button = ttk.Button(self.root, text=text, command=lambda t=text: self.update_display(t), style="Calculator.TButton")
            button.grid(row=row, column=column, padx=5, pady=5, ipadx=0, ipady=0)

        clear_button = ttk.Button(self.root, text="C", command=self.clear_display, style="Calculator.TButton")
        clear_button.grid(row=1, column=4, padx=5, pady=5, ipadx=0, ipady=0)

        calculate_button = ttk.Button(self.root, text="Calcular", command=self.calculate, style="Calculator.TButton")
        calculate_button.grid(row=2, column=4, columnspan=4, padx=5, pady=5, ipadx=0, ipady=0)

    def update_display(self, value):
        current_text = self.result_var.get()
        self.result_var.set(current_text + value)

    def clear_display(self):
        self.result_var.set("")

    def calculate(self):
        try:
            expression = self.result_var.get()
            result = str(eval(expression))
            self.result_var.set(result)
        except:
            self.result_var.set("Erro")

    def key_pressed(self, event):
        key = event.keysym
        state = event.state

        if key in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            if state & (1 << 0):
                self.update_display(key)
        elif key in ("+", "-", "*", "/", ".", ","):
            if state & (1 << 0):
                self.update_display(key)
        elif key == "c":
            self.clear_display()
        elif key == "Return":
            self.calculate()

    def key_released(self, event):
        pass  # Não é necessário implementar nada aqui

root = tk.Tk()
root.title("Calculadora")

app = CalculatorApp(root)
root.mainloop()
