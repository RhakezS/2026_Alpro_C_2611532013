# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("======================================")
print("3. OPERATOR BITWISE")
print("======================================")

angka1_2013 = int(input("Masukkan angka bitwise-1: "))
angka2_2013 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =",angka1_2013,"| biner =",bin(angka1_2013))
print("angka1 =",angka2_2013,"| biner =",bin(angka2_2013))

# Bitwise AND
hasil_2013 = angka1_2013 & angka2_2013
print("\nBitwise AND (&)")
print(angka1_2013,"&",angka2_2013,hasil_2013)
print("Biner hasil =",bin(hasil_2013))
print("Biner hasil (8 bit) =",format(hasil_2013,"08b"))

# Bitwise OR
hasil_2013 = angka1_2013 | angka2_2013
print("\nBitwise OR (|)")
print(angka1_2013,"|",angka2_2013,hasil_2013)
print("Biner hasil =",bin(hasil_2013))
print("Biner hasil (8 bit) =",format(hasil_2013,"08b"))

# Bitwise XOR
hasil_2013 = angka1_2013 ^ angka2_2013
print("\nBitwise XOR (^)")
print(angka1_2013,"^",angka2_2013,hasil_2013)
print("Biner hasil =",bin(hasil_2013))
print("Biner hasil (8 bit) =",format(hasil_2013,"08b"))

# Bitwise NOT
hasil_2013 = ~angka1_2013
print("\nBitwise NOT (~)")
print(angka1_2013,"~",angka2_2013,hasil_2013)
print("Biner hasil =",bin(hasil_2013))
print("Biner hasil (8 bit) =",format(hasil_2013,"08b"))

# Bitwise geser kiri
jumlah_geser_2013 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2013 = angka1_2013 << jumlah_geser_2013
print("\nBitwise geser kiri (<<)")
print(angka1_2013,"<<",jumlah_geser_2013,"=",hasil_2013)
print("Biner hasil =",bin(hasil_2013))
print("Biner hasil (8 bit) =",format(hasil_2013,"08b"))

# Bitwise geser kanan
hasil_2013 = angka1_2013 >> jumlah_geser_2013
print("\nBitwise geser kiri (>>)")
print(angka1_2013,">>",jumlah_geser_2013,"=",hasil_2013)
print("Biner hasil =",bin(hasil_2013))
print("Biner hasil (8 bit) =",format(hasil_2013,"08b"))