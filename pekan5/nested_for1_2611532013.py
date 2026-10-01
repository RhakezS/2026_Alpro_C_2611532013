# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2013 = int(input("Masukkan nilai batas : "))
for line_2013 in range(1,batas_2013 + 1):
    for j in range(1,(-1*line_2013+batas_2013)+1):
        print(".",end="")
    print(line_2013)