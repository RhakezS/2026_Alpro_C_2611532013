# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("======================================")
print("1. OPERATOR KEANGGOTAAN")
print("======================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2013 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2013 = [int(angka.strip() for angka in input_data_2013.split(','))]

nilai_dicari_2013 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_2013 = nilai_dicari_2013 in data_2013
print("\nOperator keanggotaan IN")
print(nilai_dicari_2013,"in",data_2013,"=",hasil_2013)

# Operator not in
hasil_2013 = nilai_dicari_2013 not in data_2013
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2013,"not in",data_2013,"=",hasil_2013)

print("======================================")
print("2. OPERATOR IDENTIAS")
print("======================================")

# objek1 menggunakan list dari input perngguna
object1_2013 = data_2013

# objek2 merujuk pada objek yang sama dengan objek1
object2_2013 = object1_2013

# objek3 memiliki isi sama, tetapi merupakan objek baru
object3_2013 = data_2013.copy()

print("object1 =",object1_2013)
print("object2 =",object2_2013)
print("object3 =",object3_2013)

# Operator is
hasil_2013 = object1_2013 is object2_2013
print("\nOperator identitas IS")
print("objek1 is objek2 =",hasil_2013)

# Operator is not
hasil_2013 = object1_2013 is not object2_2013
print("\nOperator identitas IS NOT")
print("objek1 is not objek2 =",hasil_2013)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =",object1_2013 is object3_2013)
print("objek1 == objek3 =",object1_2013 == object3_2013)