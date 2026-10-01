# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2013 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2013 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2013 = tinggi_2013
    c_2013 = a_2013
    lebar_2013 = (2 * tinggi_2013) - 2

    for i_2013 in range(1, tinggi_2013 + 1):
        b_2013 = c_2013 + 1

        for j_2013 in range(1, lebar_2013 + 1):

            # Baris atas dan bawah
            if i_2013 == 1 or i_2013 == tinggi_2013:
                if j_2013 == 1 or j_2013 == lebar_2013:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_2013 == 1 or j_2013 == lebar_2013:
                    print("|", end="")
                else:
                    if j_2013 == c_2013:
                        print("<", end="")
                    elif j_2013 == b_2013:
                        print(">", end="")
                    elif j_2013 == (lebar_2013 - c_2013):
                        print("<", end="")
                    elif j_2013 == (lebar_2013 - c_2013 + 1):
                        print(">", end="")
                    elif j_2013 > b_2013 and j_2013 < (lebar_2013 - c_2013):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli java
        a_2013 -= 2

        if a_2013 <= 0:
            c_2013 = (-a_2013 + 2)
        else:
            c_2013 = a_2013