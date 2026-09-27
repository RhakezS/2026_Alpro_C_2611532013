("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_2013 = input("Masukkan Nama Pengunjung        : ")
umur_2013 = int(input("Input umur anda                 : "))
sim_c_2013 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].strip().lower()

print("\nPilihan Paket Wahana (1-5):")
print("  1. Wahana Safari Rimba         (Rp 50,000)")
print("  2. Wahana Arung Jeram          (Rp 75,000)")
print("  3. Wahana Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Wahana Roller Coaster Kilat (Rp 100,000)")
print("  5. Wahana All-Access VIP       (Rp 220,000)")
paket_2013 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_2013 = int(input("Masukkan jumlah tiket           : "))
if jumlah_tiket_2013 <= 0:
    print("Jumlah tiket tidak valid!")
    exit()
member_2013 = input("Apakah Anda member? (y/t)       : ")[0].strip().lower()
promo_2013 = input("Apakah kode promo valid? (y/t)  : ")[0].strip().lower()

wahana_2013 = ""
harga_satuan_2013 = 0

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
match paket_2013:
    case 1: # Wahana Safari Rimba
        if umur_2013 >= 10:
            print("Anda sudah dewasa dan boleh mengendarai Wahana Safari Rimba sendiri.")
        else:
            print("Anda wajib didampingi orang tua.")
        harga_satuan_2013 = 50000
    case 2: # Wahana Arung Jeram
        if umur_2013 >= 15:
            print("Anda sudah dewasa dan boleh mengendarai Wahana Arung Jeram sendiri.")
        else:
            print("Anda wajib didampingi orang tua.")
        harga_satuan_2013 = 75000
    case 3: # Wahana Motor ATV Ekstrim
        if umur_2013 >= 17 and sim_c_2013 == 'y':
            print("Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
        elif umur_2013 >= 17 and sim_c_2013 != 'y':
            print("Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
        elif umur_2013 < 17 and sim_c_2013 == 'y':
            print("Identitas tidak valid: Belum cukup umur memiliki SIM.")
        else:
            print("Anda belum cukup umur dan tidak boleh bawa motor ATV.")
        harga_satuan_2013 = 120000
    case 4: # Wahana Roller Coaster Kilat
        if umur_2013 >= 17:
            print("Anda sudah dewasa dan boleh mengendarai Wahana Roller Coaster Kilat sendiri.")
        else:
            print("Anda wajib didampingi orang tua.")
        harga_satuan_2013 = 100000
    case 5: # Wahana All-Access VIP
        if umur_2013 >= 17 and sim_c_2013 == 'y':
            print("Anda sudah dewasa dan boleh mengendarai semua wahana sendiri.")
        elif umur_2013 >= 17 and sim_c_2013 != 'y':
            print("Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
        elif umur_2013 < 17 and sim_c_2013 == 'y':
            print("Identitas tidak valid: Belum cukup umur memiliki SIM.")
        else:
            print("Anda belum cukup umur dan tidak boleh bawa motor ATV.")
        harga_satuan_2013 = 220000
    case _: 
        print("Paket wahana tidak valid!")
        exit()

diskon_2013 = 0
if harga_satuan_2013 * jumlah_tiket_2013 >= 200000:
    diskon_2013 += 10
if member_2013 in ["y","ya"]:
    diskon_2013 += 5
if promo_2013 in ["y","ya"]:
    diskon_2013 += 15
if jumlah_tiket_2013 >= 5:
    diskon_2013 += 5

nominal_2013 = harga_satuan_2013 * jumlah_tiket_2013
nominal_diskon_2013 = nominal_2013 * (diskon_2013 / 100)
total_bayar_2013 = nominal_2013 - nominal_diskon_2013
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {nominal_2013:,}")
if nominal_2013 > 300000: 
    print("Selamat! Anda berhak mendapatkan Souvenir Gratis.")
print(f"Total Diskon     : {diskon_2013}% (Rp {int(nominal_diskon_2013):,})")
print(f"Total Bayar      : Rp {int(total_bayar_2013):,}")
print("Catatan Layanan  : Terima kasih telah berkunjung.")
print("Program Selesai")