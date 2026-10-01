# Buat file dengan nama nested_for2_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2021 = int(input("Masukan nilai batas: "))
for i_2021 in range(1, batas_2021 + 1):
    for j_2021 in range(1, batas_2021 + 1):
        print("*", end="")
    print()  # pindah ke baris berikutnya