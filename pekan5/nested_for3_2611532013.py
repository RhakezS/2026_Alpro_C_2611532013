# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2013 = int(input("Masukan nilai batas: "))
for i_2013 in range(batas_2013 + 1):
    for j_2013 in range(batas_2013 + 1):
        print(i_2013 + j_2013, end=" ")
    print()  # pindah ke baris berikutnya