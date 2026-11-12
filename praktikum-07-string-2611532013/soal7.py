# Name: Rhakez Elvano Stonie
# NIM: 2611532013
# Question: 7

name        = input("Masukkan nama anda: ")
nim         = input("Masukkan NIM anda: ")

full_name   = name
nim = nim
usn_kampus  = (full_name[1:5] + nim[7:11])

print("=" * 30)
print(" " * 10,"STUDENT CARD", " " * 10)
print("=" * 30)
print("Name     :" ,name)
print("NIM      :", nim)
print("Username :", usn_kampus.lower())
print("Intake   : 2026")
print("=" * 30)