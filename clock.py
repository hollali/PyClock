import tkinter as tk
import time

def update_clock():
    ora_curenta = time.strftime("%H:%M:%S")
    ceas.config(text=ora_curenta)  # Corrected the typo in 'config'
    ceas.after(1000, update_clock)

app = tk.Tk()  # Corrected the typo in 'Tk'
app.title("Ceas Python")

ceas = tk.Label(app, text="", font=("Helvetica", 48))
ceas.pack()

update_clock()
app.mainloop()
