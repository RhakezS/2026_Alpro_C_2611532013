# Buat file dengan nama assigment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Python

angka1_2013 = int(input("Input angka-1: "))
angka2_2013 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =",angka1_2013)
print("Nilai angka2 =",angka2_2013)

# Assigment biasa
hasil_2013 = angka1_2013 
print("\nAssigment biasa (=)")
print("Hasil =",hasil_2013)

# Assigment penambahan
hasil_2013 = angka1_2013 
hasil_2013 += angka2_2013 
print("\nAssigment penambahan (+=)")
print("Hasil =",hasil_2013)

# Assigment pengurangan
hasil_2013 = angka1_2013 
hasil_2013 -= angka2_2013 
print("\nAssigment pengurangan (-=)")
print("Hasil =",hasil_2013)

# Assigment perkalian
hasil_2013 = angka1_2013 
hasil_2013 *= angka2_2013
print("\nAssigment perkalian (*=)")
print("Hasil =",hasil_2013)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_2013 != 0:
    hasil_2013 = angka1_2013 
    hasil_2013 /= angka2_2013
    print("\nAssigment pembagian (/=)")
    print("Hasil =",hasil_2013)
    # Operator tambahan
    hasil_2013 = angka1_2013 
    hasil_2013 //= angka2_2013
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =",hasil_2013)
    hasil_2013 = angka1_2013 
    hasil_2013 %= angka2_2013
    print("\nOperator sisa bagi (%=)")
    print("Hasil =",hasil_2013)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil_2013 = angka1_2013 
hasil_2013 **= angka2_2013
print("\nOperator perpangkatan (**=)")
print("Hasil =",hasil_2013)