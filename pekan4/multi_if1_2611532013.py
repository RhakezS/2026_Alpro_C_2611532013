# Buat file dengan nama multi_if1.py
# Buat program untuk kodisional if
# Nama variabel ditambah 4 digit terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2013 = int(input("Input Umur Anda = "))
sim_2013 = input("Apakah Anda Sudah Punya SIM (y/t): ")[0]

if umur_2013 >= 17 and sim_2013 == "y":
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_2013 >= 17 and sim_2013 != "y":
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_2013 < 17 and sim_2013 != "y":
    print("Anda Belum Cukup Umur bawa motor")

if umur_2013 < 17 and sim_2013 == "y":
    print("Anda Belum Cukup Umur punya SIM")