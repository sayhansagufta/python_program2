import tkinter as tk
from time import strftime

def update_waktu():
    waktu = strftime('%H:%M:%S')  # Mendapatkan waktu saat ini dalam format HH:MM:SS
    label_jam.config(text=waktu)  # Mengatur teks di label menjadi waktu saat ini
    label_jam.after(1000, update_waktu)  # Memanggil fungsi ini lagi setelah 1000 milidetik (1 detik)

# membuat window
root = tk.Tk()
root.title("Jam Digital")

#label untuk menampilkan jam
label_jam = tk.Label(root, font=('Arial', 50), bg='white', fg='black')
label_jam.pack(anchor='center', pady=50)

# memulai fungsi update waktu
update_waktu()

# menjalankan aplikasi
root.mainloop()