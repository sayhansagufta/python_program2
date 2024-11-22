from datetime import datetime, timedelta

def hitung_umur():
    print("Program Penghitung Umur")
    try:
        tanggal_lahir = input("Masukkan tanggal lahir (format: YYYY-MM-DD):").strip()
        tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
        hari_ini = datetime.now()

        umur_tahun = hari_ini.year - tanggal_lahir.year
        umur_bulan = hari_ini.month - tanggal_lahir.month
        umur_hari = hari_ini.day -  tanggal_lahir.day

        # jika bulan / hari belum mencapai tanggal lahir
        if umur_bulan < 0:
            umur_tahun -= 1
            umur_bulan += 12
        if umur_hari < 0:
            umur_bulan -= 1
            hari_di_bulan_sebelumnya = (hari_ini.replace(month=hari_ini.month - 1, day=1) - timedelta(days=1)).day
            umur_hari += hari_di_bulan_sebelumnya

        print(f"Umur Anda adalah {umur_tahun} tahun, {umur_bulan} bulan, dan {umur_hari} hari. ")
    except ValueError:
        print("Format Tanggal Tidak Valid. Harap Masukkan dalam format YYYY-MM-DD.")

# jalankan program
hitung_umur()
