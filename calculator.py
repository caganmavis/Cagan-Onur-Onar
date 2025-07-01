import customtkinter as ctk

def button_click(value):
    if value == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, "end")
            entry.insert("end", result)
        except:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    elif value == "C":
        entry.delete(0, "end")
    else:
        entry.insert("end", value)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Cagan Onur Onar")


for i in range(7):
    app.rowconfigure(i, weight=1)
for i in range(4):
    app.columnconfigure(i, weight=1)

entry = ctk.CTkEntry(app, font=("Arial", 36), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"]
]

for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        btn = ctk.CTkButton(app, text=char, font=("Arial", 24),
                            command=lambda x=char: button_click(x))
        btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

btn_clear = ctk.CTkButton(app, text="C", font=("Arial", 24),
                          command=lambda: button_click("C"))
btn_clear.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

app.mainloop()
