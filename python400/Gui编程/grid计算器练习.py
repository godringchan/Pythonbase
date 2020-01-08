import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.createCalculator()

    def createCalculator(self):
        btnText = (("MC", "M+", "M-", "MR"),
                   ("C", "+-", "/", "X"),
                   (7, 8, 9, "-"),
                   (4, 5, 6, "+"),
                   (1, 2, 3, "="),
                   (0, "."))
        count_entry = tk.Entry(self)
        count_entry.grid(row=0, column=0, columnspan=4, pady=10)
        for row_index, r_value in enumerate(btnText):
            # print(row_index)
            # print(r_value)
            for column_index, one_value in enumerate(r_value):
                btn = tk.Button(self, text=one_value, width=3)
                btn.grid(row=(row_index+1), column=column_index, pady=5,
                         padx=1,  sticky="NSEW")
                if one_value == "=":
                    btn.grid(row=(row_index+1), column=column_index, pady=5,
                             padx=1,  sticky="NSEW", rowspan=2)
                if one_value == 0:
                    btn.grid(row=(row_index+1), column=column_index, pady=5,
                             padx=1,  sticky="NSEW", columnspan=2)
                if one_value == ".":
                    btn.grid(row=(row_index+1), column=column_index+1,
                             pady=5, padx=1,  sticky="NSEW")


def main():
    master = tk.Tk(className="计算器")
    master.geometry("250x280+100+100")
    app = Application(master)
    app.pack()
    master.mainloop()


if __name__ == "__main__":
    main()
