import tkinter as tk
from time import strftime

def update_waktu():
    waktu = strftime('%H:%M:%S')
    label_jam.config(text=waktu)
    label_jam.after(1000, update_waktu)

# membuat window
root = tk.Tk()
root.title("Jam Digital")

#label untuk menampilkan jam
label_jam = tk.Label(root, font=('Arial', 50), bg='black', fg='white')
label_jam.pack(anchor='center', pady=20)

# memulai fungsi update waktu
update_waktu()

# menjalankan aplikasi
root.mainloop()