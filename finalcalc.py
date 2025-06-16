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

# Uygulama penceresi
ctk.set_appearance_mode("dark")  # Dark mode
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("340x540")
app.title("cagan onar calc")

# Giriş alanı
entry = ctk.CTkEntry(app, font=("Arial", 36), justify="right", width=320, height=80)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Tuş yerleşimi
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"],
    ["C"]
]

for row_index, row in enumerate(buttons, start=1):
    for col_index, char in enumerate(row):
        if char == "C":
            button = ctk.CTkButton(app, text=char, corner_radius=15,
                                   font=("Arial", 24), width=320, height=60,
                                   fg_color="white", text_color="black",
                                   command=lambda x=char: button_click(x))
            button.grid(row=row_index + 3, column=0, columnspan=4, padx=10, pady=10)
        else:
            button = ctk.CTkButton(app, text=char, corner_radius=15,
                                   font=("Arial", 24), width=75, height=60,
                                   fg_color="white", text_color="black",
                                   command=lambda x=char: button_click(x))
            button.grid(row=row_index, column=col_index, padx=5, pady=5)

app.mainloop()