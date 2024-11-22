print("Pilih Operasi: ")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (x)")
print("4. Bagi")

# input angka dari pengguna
angka1 = float(input("Masukkan Angka Pertama:"))
angka2 = float(input("Masukkan Angka Kedua:"))

#input pilihan operasi
pilihan = input("Masukkan Pilihan Operasi (1/2/3/4):")

#fungsi penjumlahan
def tambah(a, b):
    return a + b

#fungsi pengurangan
def kurang(a, b):
    return a - b

# fungsi perkalian
def kali(a, b):
    return a * b

# fungsi pembagian
def bagi(a, b):
    if b != 0: #cek untuk menghindari pembagian dengan nol
        return a / b
    else:
        return "Error: Pembagian dengan nol tidak diperbolehkan"
    
if pilihan == '1':
    print("Hasil:", tambah(angka1, angka2))
elif pilihan == "2":
    print("Hasil:", kurang(angka1, angka2))
elif pilihan == "3":
    print("Hasil:", kali(angka1, angka2))
elif pilihan == "4":
    print("Hasil:", bagi(angka1, angka2))
else:
    print("Pilihan Operasi Tidak Valid!!")