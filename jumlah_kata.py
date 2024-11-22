def hitung_jumlah_kata():
    print("Program Penghitung Jumlah Kata")
    kalimat = input("Masukkan Sebuah Kalimat:").strip()

    if kalimat:
        jumlah_kata = len(kalimat.split())
        print(f"Jumlah kata dalam kalimat adalah: {jumlah_kata}")
    else:
        print("Input tidak boleh kosong. Silahkan Masukan Kalimat. ")

#jalankan program
hitung_jumlah_kata()