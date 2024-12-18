def konversi_jarak(jarak, dari_satuan, ke_satuan):
    # Mengonversi jarak dari satu satuan ke satuan lainnya.

    # Konversi ke meter
    if dari_satuan == "kilometer":
        jarak_meter = jarak * 1000
    elif dari_satuan == "meter":
        jarak_meter = jarak
    elif dari_satuan == "mil":
        jarak_meter = jarak * 1609.34
    elif dari_satuan == "yard":
        jarak_meter = jarak * 0.9144
    else:
        return "Satuan tidak dikenali."

    # Konversi dari meter ke satuan tujuan
    if ke_satuan == "kilometer":
        return jarak_meter / 1000
    elif ke_satuan == "meter":
        return jarak_meter
    elif ke_satuan == "mil":
        return jarak_meter / 1609.34
    elif ke_satuan == "yard":
        return jarak_meter / 0.9144
    else:
        return "Satuan tidak dikenali."

def main():
    
    print("Selamat datang di Program Konversi Jarak!")
    
    # Meminta input dari pengguna
    try:
        jarak = float(input("Masukkan jarak: "))
        dari_satuan = input("Masukkan satuan dari (kilometer, meter, mil, yard): ").lower()
        ke_satuan = input("Masukkan satuan ke (kilometer, meter, mil, yard): ").lower()
        
        # Mengonversi jarak
        hasil = konversi_jarak(jarak, dari_satuan, ke_satuan)
        
        # Menampilkan hasil
        if isinstance(hasil, str):
            print(hasil)  # Menampilkan pesan kesalahan
        else:
            print(f"{jarak} {dari_satuan} sama dengan {hasil:.2f} {ke_satuan}.")
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

if __name__ == "__main__":
    main()