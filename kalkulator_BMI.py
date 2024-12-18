def hitung_bmi(berat, tinggi):
    # Menghitung BMI berdasarkan berat dan tinggi.
    bmi = berat / (tinggi ** 2)
    return bmi

def kategori_bmi(bmi):
    # Menentukan kategori berat badan berdasarkan nilai BMI.
    if bmi < 18.5:
        return "Kekurangan berat badan"
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal"
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan"
    else:
        return "Kegemukan (Obesitas)"

def main():
    print("Selamat datang di Kalkulator BMI!")
    
    # Meminta input dari pengguna
    try:
        berat = float(input("Masukkan berat badan Anda (dalam kg): "))
        tinggi_cm = float(input("Masukkan tinggi badan Anda (dalam cm): "))
        
        # Mengonversi tinggi dari cm ke m
        tinggi_m = tinggi_cm / 100
        
        # Validasi input
        if berat <= 0 or tinggi_m <= 0:
            print("Berat badan dan tinggi badan harus lebih besar dari 0.")
            return
        
        # Menghitung BMI
        bmi = hitung_bmi(berat, tinggi_m)
        
        # Menampilkan hasil
        print(f"Nilai BMI Anda adalah: {bmi:.2f}")
        print(f"Kategori berat badan Anda: {kategori_bmi(bmi)}")
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

if __name__ == "__main__":
    main()