# Buat file dengan nama multi_if2_2611531015.py
# Buat program untuk kondisional If
# Nama variabel ditambah 4 digit nim terakhir contoh ipk_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon belanja

# Input dari user
total_belanja_1015 = float(input("Input Total Belanja (Rp): "))

# Input status member
input_member_1015 = input("Apakah Anda Member (y/t): ").strip().lower()
is_member_1015 = input_member_1015 in ["y", "ya"]

#Input status kode promo
input_promo_1015 = input("Apakah Kode Promo valid (y/t): ").strip().lower()
kode_promo_valid_1015 = input_promo_1015 in ["y", "ya"]

total_diskon_persen_1015 = 0

# MULTI-IF terpisah Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk jika memenuhi beberapa syarat sekaligus

if total_belanja_1015 >= 1000000:
    total_diskon_persen_1015 += 10  # Diskon 10% untuk belanja >= 1 juta

if is_member_1015:
    total_diskon_persen_1015 += 5  # Diskon tambahan 5% untuk member

if kode_promo_valid_1015:
    total_diskon_persen_1015 += 15  # Diskon tambahan 15% untuk kode promo valid

# Menghitung nominal diskon dan total bayar
nominal_diskon_1015 = (total_diskon_persen_1015 / 100) * total_belanja_1015
total_bayar_1015 = total_belanja_1015 - nominal_diskon_1015

# Output hasil perhitungan diskon
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_1015}% (Rp {nominal_diskon_1015:.0f})")
print(f"Total Bayar   : Rp {total_bayar_1015:.0f}")

print(f"Total Diskon yang anda dapatkan : {total_diskon_persen_1015}%")
#Output: Total diskon yang anda dapatkan : 30% jika belanja > 1 juta, member, dan kode promo valid