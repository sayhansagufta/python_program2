# Nilai Tukar 
usd_to_idr = 15000
idr_to_ud = 0.000067

# input dari pengguna
print("Pilih Jenis Konversi:")
print("1. USD ke IDR")
print("2. IDR ke USD")

pilihan = int(input("Masukkan Pilihan (1/2): "))

jumlah = float(input("Masukkan jumlah uang: "))

# konversi
if pilihan == 1:
    hasil = jumlah * usd_to_idr
    print(f"{jumlah} USD = {hasil:.2f} IDR")
elif pilihan == 2:
    hasil = jumlah * idr_to_ud
    print(f"{jumlah} IDR = {hasil:.2f} USD")
else:
    print("Pilihan Tidak Valid!")