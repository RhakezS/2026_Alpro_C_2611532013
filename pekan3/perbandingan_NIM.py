# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2013 = int(input("Input angka-1:"))
angka2_2013 = int(input("Input angka-2:"))

# Lebih besar dari
hasil_2013 = angka1_2013 > angka2_2013
print("\nOperator lebih besar dari")
print("angka1_2013 > angka2_2013 =", hasil_2013)

# Lebih kecil dari
hasil_2013 = angka1_2013 < angka2_2013
print("\nOperator lebih kecil dari")
print("angka1_2013 < angka2_2013 =", hasil_2013)

# Lebih besar dari atau sama dengan
hasil_2013 = angka1_2013 >= angka2_2013
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_2013 >= angka2_2013 =", hasil_2013)

# Lebih kecil dari atau sama dengan
hasil_2013 = angka1_2013 <= angka2_2013
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_2013 <= angka2_2013 =", hasil_2013)

# Sama dengan
hasil_2013 = angka1_2013 == angka2_2013
print("\nOperator sama dengan")
print("angka1_2013 == angka2_2013 =", hasil_2013)

# Tidak sama dengan
hasil_2013 = angka1_2013 != angka2_2013
print("\nOperator tidak sama dengan")
print("angka1_2013 != angka2_2013 =", hasil_2013)

# Tambahan: Perbandingan berantai dalam python
hasil_2013 = 0 < angka1_2013 < 100
print("\nPerbandingan berantai")
print("0 < angka1_2013 < 100 =", hasil_2013)

hasil_2013 = 0 < angka2_2013 < 100
print("0 < angka2_2013 < 100 =", hasil_2013)