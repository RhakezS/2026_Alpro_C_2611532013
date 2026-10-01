# Buat file dengan nama jumlah_genap_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2013 = int(input("Masukan nilai batas: "))

jumlah_2013 = 0
for i in range(1, ulang_2013 + 1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah_2013 = jumlah_2013 + i

        if i < ulang_2013:
            print(" + ", end="")
        else:
            print(" = ", jumlah_2013, end="")
print()
print("Jumlah =", jumlah_2013)