import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):

        self.master = master
        master.title("Simple Calculator")
        master.geometry("300x400")
        master.resizable(False, False)
        master.configure(bg="#2c3e50")

        self.expression = ""
        self.input_text = tk.StringVar()


        input_frame = tk.Frame(master, bd=0, relief=tk.RIDGE, bg="#34495e")
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        self.input_field = tk.Entry(input_frame, font=('Arial', 24, 'bold'),
                                    textvariable=self.input_text, width=50,
                                    bg="#ecf0f1", bd=0, justify=tk.RIGHT,
                                    insertbackground="#2c3e50", fg="#2c3e50")
        self.input_field.grid(row=0, column=0, ipadx=8, ipady=8, pady=10, padx=10, sticky="nsew")
        input_frame.grid_rowconfigure(0, weight=1)
        input_frame.grid_columnconfigure(0, weight=1)


        btns_frame = tk.Frame(master, bg="#2c3e50")
        btns_frame.pack(fill=tk.BOTH, expand=True)

        # Define button layout
        button_chars = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]


        for i in range(4):
            btns_frame.grid_rowconfigure(i, weight=1)
            btns_frame.grid_columnconfigure(i, weight=1)

        row_val = 0
        col_val = 0
        for button_char in button_chars:
            button_color = "#3498db" if button_char in ['/', '*', '-', '+', '='] else "#95a5a6"
            text_color = "#ffffff" if button_char in ['/', '*', '-', '+', '='] else "#2c3e50"
            active_bg_color = "#2980b9" if button_char in ['/', '*', '-', '+', '='] else "#7f8c8d"

            if button_char == 'C':
                button = tk.Button(btns_frame, text=button_char, fg=text_color,
                                   bg="#e74c3c", bd=0, font=('Arial', 18, 'bold'),
                                   command=self.clear_all, relief=tk.FLAT,
                                   activebackground="#c0392b", activeforeground="#ffffff")
            elif button_char == '=':
                button = tk.Button(btns_frame, text=button_char, fg=text_color,
                                   bg="#27ae60", bd=0, font=('Arial', 18, 'bold'),
                                   command=self.evaluate_expression, relief=tk.FLAT,
                                   activebackground="#229a56", activeforeground="#ffffff")
            else:
                button = tk.Button(btns_frame, text=button_char, fg=text_color,
                                   bg=button_color, bd=0, font=('Arial', 18, 'bold'),
                                   command=lambda char=button_char: self.button_click(char), relief=tk.FLAT,
                                   activebackground=active_bg_color, activeforeground="#ffffff")

            button.grid(row=row_val, column=col_val, sticky="nsew", padx=1, pady=1)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, char):

        self.expression += str(char)
        self.input_text.set(self.expression)

    def clear_all(self):

        self.expression = ""
        self.input_text.set("")

    def evaluate_expression(self):

        try:
            result = str(eval(self.expression)) # Using eval for simplicity, but be cautious in production
            self.input_text.set(result)
            self.expression = result # Set the result as the new expression for continuous calculations
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            self.expression = ""
            self.input_text.set("")
        except SyntaxError:
            messagebox.showerror("Error", "Invalid Expression!")
            self.expression = ""
            self.input_text.set("")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.expression = ""
            self.input_text.set("")

# Main part of the script
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
