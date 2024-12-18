def faktorial(n):
    # Menghitung faktorial dari n secara rekursif 
    if n < 0:
        return None # faktorial tidak terdefinisi untuk bilangan negatif
    elif n == 0 or n == 1:
        return 1 # Faktorial dari 0 dan 1 adalah 1 
    else:
        return n * faktorial(n - 1) # Rekursi

def main():
    print("Selamat Datang di Program Faktorial!")

    # Meminta input dari user
    try:
        angka = int(input("Masukkan angka bilangan bulat non-negatif: "))

        # Validasi Input
        if angka < 0:
            print("Faktorial tidak terdefinisi untuk bilangan negatif.")
            return
        
        # Menghitung Faktorial 
        hasil = faktorial(angka)

        # Menampilkan hasil
        print(f"Faktorial dari {angka} adalah: {hasil}")
    
    except ValueError:
        print("Input tidak valid. harap masukkan angka bilangan bulat non-negatif.")

if __name__ == "__main__":
    main()