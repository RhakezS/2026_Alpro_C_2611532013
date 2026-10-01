# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2013= int(input("Masukkan jumlah perulangan: "))

jumlah_2013 = 0
for i in range(1,ulang_2013 + 1):
    print(i,end="")
    jumlah_2013 += i

    if i < ulang_2013:
        print("+",end="")
    else:
        print("=",jumlah_2013, end="")
print()
print("jumlah =",jumlah_2013)