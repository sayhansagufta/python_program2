import random

def tebak_angka():
    print("Selamat datang di Game Tebak Angka! ")
    print("Saya telah memilih sebuah angka antara 1 hingga 100.")
    print("Coba tebak Angka Tersebut. ")
    
    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    while True:
        try:
            tebakan = int(input("Masukkan tebakanmu: ").strip())
            percobaan += 1

            if tebakan < angka_rahasia:
                print("Terlalu Rendah! Coba Lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu Tinggi! Coba lagi.")
            else:
                print(f"Selamat! kamu berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
                break
        except ValueError:
            print("Input tidak valid. Masukkan Angka Saja!")

# jalankan program
tebak_angka()




