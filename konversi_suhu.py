def konversi_suhu():
    print("Program Konversi Suhu")
    print("1. Celcius ke Fahrenheit ")
    print("2. Fahrenheit ke Celcius")

    pilihan = input("Pilih Jenis Konversi (1/2): ")

    if pilihan == "1":
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        fahrenheit = (celcius * 9/5) + 32
        print(f"{celcius}°C sama dengan {fahrenheit}°F")
    elif pilihan == "2":
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celcius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F sama dengan {celcius}°C")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
konversi_suhu()