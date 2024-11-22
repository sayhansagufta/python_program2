def ganjil_genap():
    print("====  Program Penentu Bilangan Ganjil atau Genap ====")
    try:
        angka = int(input("Masukkan Sebuah Bilangan: ").strip())
        if angka % 2 == 0:
            print(f"{angka} adalah bilangan Genap.")
        else: 
            print(f"{angka} adalah bilangan Ganjil. ")
    except ValueError:
        print("Input tidak Valid. Masukkan Bilangan Bulat Saja.")

 #jalankan program
ganjil_genap()