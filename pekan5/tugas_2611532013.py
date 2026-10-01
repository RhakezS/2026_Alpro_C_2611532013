# Buatlah program menggunakan perulangan for

tinggi_2013 = int(input("Masukkan tinggi segitiga: "))

for a_2013 in range(1, tinggi_2013 + 1):
    for b_2013 in range(tinggi_2013 - a_2013):
        print(" ", end="")
    for c_2013 in range(a_2013):
        print("*", end=" ")
    print()