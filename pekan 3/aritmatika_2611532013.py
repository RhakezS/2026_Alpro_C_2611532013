# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2013 = int(input("Input angka-1: "))
angka2_2013 = int(input("Input angka-2: "))

# Penjumlahan
hasil_2013 = angka1_2013 + angka2_2013
print("\nOperator Penjumlahan")
print("Hasil =",hasil_2013)

# Pengurangan
hasil_2013 = angka1_2013 - angka2_2013
print("\nOperator Pengurangan")
print("Hasil =",hasil_2013)

# Perkalian
hasil_2013 = angka1_2013 * angka2_2013
print("\nOperator Perkalian")
print("Hasil =",hasil_2013)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2013 != 0:
    hasil_2013 = angka1_2013 / angka2_2013
    print("\nOperator Pembagian")
    print("Hasil =",hasil_2013)

    hasil_2013 = angka1_2013 // angka2_2013
    print("\nOperator Pembagian Bulat")
    print("Hasil =",hasil_2013)

    hasil_2013 = angka1_2013 % angka2_2013
    print("\nOperator Sisa Bagi")
    print("Hasil =",hasil_2013)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2013 = angka1_2013 ** angka2_2013
print("\nOperator Pangkat")
print("Hasil =",hasil_2013)