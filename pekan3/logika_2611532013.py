# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
# Program ini menngunakan fungsi input()
# Program operator logika dalam Python

# Memasukan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_2013 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_2013 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 = ",a1_2013)
print("A2 = ",a2_2013)

# Konjungsi: bernilai True jika keduanya True
hasil_2013 = a1_2013 and a2_2013
print("\nKonjungsi (AND)")
print("A1 and A2 =",hasil_2013)

# Disjungsi: bernilai True jika salah satunya False
hasil_2013 = a1_2013 or a2_2013
print("\nDisjungsi (OR)")
print("A1 or A2 =",hasil_2013)

# Negasi A1: membalik nilai A1
hasil_2013 = not a1_2013
print("\nNegasi A1(NOT)")
print("not A1",hasil_2013)

# Negasi A2: membalik nilai A2
hasil_2013 = not a2_2013
print("\nNegasi A2(NOT)")
print("not A2",hasil_2013)

# XOR: bernilai True jika kedua nilai berbeda
hasil_2013 = a1_2013 != a2_2013
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2",hasil_2013)