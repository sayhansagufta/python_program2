import time
import winsound  # Hanya untuk Windows. Untuk sistem lain, Anda bisa menggunakan modul lain untuk suara.

def set_alarm():
    # Mengatur alarm berdasarkan input pengguna.
    alarm_time = input("Masukkan waktu alarm (format HH:MM:SS, contoh 14:30:00): ")
    return alarm_time

def check_alarm(alarm_time):
    # Memeriksa apakah waktu saat ini sama dengan waktu alarm.
    while True:
        # Mendapatkan waktu saat ini
        current_time = time.strftime("%H:%M:%S")
        print(f"Waktu saat ini: {current_time}", end="\r")  # Menampilkan waktu saat ini
        if current_time == alarm_time:
            print("\nAlarm berbunyi!")
            # Memutar suara alarm
            for _ in range(3):  # Memutar suara 3 kali
                winsound.Beep(1000, 1000)  # Frekuensi 1000 Hz selama 1 detik
            break
        time.sleep(1)  # Tunggu 1 detik sebelum memeriksa lagi

def main():
    print("Selamat datang di Alarm Clock!")
    alarm_time = set_alarm()
    print(f"Alarm disetel untuk {alarm_time}.")
    check_alarm(alarm_time)


if __name__ == "__main__":
    main()
























