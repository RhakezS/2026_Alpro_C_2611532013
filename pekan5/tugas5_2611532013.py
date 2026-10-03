print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_2013 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Border Atas:
print("#", end="")
for i_2013 in range(4 * n_2013 + 5):
    print("=", end="")
print("#")

# Jam Pasir Atas
for baris_2013 in range(n_2013, 0, -1):
    print("| ", end="")
    
    for spasi_2013 in range(2 * (n_2013 - baris_2013)):
        print(" ", end="")

    for angka_2013 in range(baris_2013, 0, -1):
        print(f"{angka_2013} ", end="")
        
    print("<*>", end="")

    for angka_2013 in range(1, baris_2013 + 1):
        print(f" {angka_2013}", end="")
        
    for spasi_2013 in range(2 * (n_2013 - baris_2013)):
        print(" ", end="")
        
    print(" |")

# Poros Titik Pusat Jam Pasir 
print("|", end="")
for spasi_2013 in range(2 * n_2013 + 1):
    print(" ", end="")
    
print("<*>", end="")

for spasi_2013 in range(2 * n_2013 + 1):
    print(" ", end="")
    
print("|")

# Jam Pasir Bawah
for baris_2013 in range(1, n_2013 + 1):
    print("| ", end="")
    
    for spasi_2013 in range(2 * (n_2013 - baris_2013)):
        print(" ", end="")

    for angka_2013 in range(baris_2013, 0, -1):
        print(f"{angka_2013} ", end="")    
        
    print("<*>", end="")

    for angka_2013 in range(1, baris_2013 + 1):
        print(f" {angka_2013}", end="") 
        
    for spasi_2013 in range(2 * (n_2013 - baris_2013)):
        print(" ", end="")
        
    print(" |")

# Border Bawah
print("#", end="")
for i_2013 in range(4 * n_2013 + 5):
    print("=", end="")
print("#")