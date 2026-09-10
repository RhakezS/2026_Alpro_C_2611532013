is_lulus = True
is_cumlaude = True

nilai = 85
batas_lulus = 75

status_kelulusan = nilai >= batas_lulus

print("=== Check Kelulusan ===")
print("nilai", nilai)
print("Apakah lulus?", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda lulus dengan predikat cumlaude!")