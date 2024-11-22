def daftar_belanja():
    print("Program Pembuatan Daftar Belanja")
    daftar = []

    while True:
        print("\nMenu:")
        print("1. Tambah item ke Daftar Belanja")
        print("2. Lihat Daftar Belanja")
        print("3. Hapus item dari Daftar Belanja")
        print("4. Keluar")

        try: 
            pilihan = int(input("Pilih Menu (1-4):").strip())
            if pilihan == 1:
                item = input("Masukkan nama item yang ingin ditambahkan: ").strip()
                daftar.append(item)
                print(f"'${item}' berhasil ditambahkan ke daftar belanja.")
            elif pilihan == 2:
                if daftar:
                    print("\nDaftar Belanja Anda:")
                    for i, item in enumerate(daftar, start=1):
                        print(f"{i}. {item}")
                else: 
                    print("Dafta Belanja Kosong.")
            
            elif pilihan == 3:
                if daftar:
                    print("\nDaftar Belanja Anda:")
                    for i, item in enumerate(daftar, start=1):
                        print(f"{i}. {item}")
                    try:
                        hapus = int(input("Masukkan nomor item yang ingin dihapus: ").strip())
                        if 1 <= hapus <= len(daftar):
                            removed_item = daftar.pop(hapus - 1)
                            print(f"'{removed_item}' berhasil dihapus dari daftar belanja.")
                        else:
                            print("Nomor item tidak valid.")
                    except ValueError:
                            print("Masukkan nomor yang valid.")
                else:
                    print("Daftar Belanja Kosong.")
                
            elif pilihan == 4:
                print("Terima Kasih telah Menggunakan program Daftar Belanja.")
                break
            else:
                print("Pilihan tidak valid. Masukkan Angka 1 - 4.")
        except ValueError:
            print("Input Tidak Valid. Masukkan Angka 1 - 4")

# jalankan program
daftar_belanja()