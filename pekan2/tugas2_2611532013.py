print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_2013 = input("Masukkan Nama Mahasiswa : ")
kelamin_2013 = input("Masukkan Jenis Kelamin (L/P): ")
umur_2013 = int(input("Masukkan Umur : "))
skor_2013 = float(input("Masukkan Skor Tes Awal : "))

alamat_2013 = """
Kampung Kalawi,
Kecamatan Kuranji,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_2013: Final = 75.0
token_2013 = 100+3j
lulus_2013 = skor_2013 > kkm_2013

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_2013," | ",type(nama_2013))
print("Jenis Kelamin : ",kelamin_2013," | ",type(kelamin_2013))
print("Alamat Domisili : ",alamat_2013," | ",type(alamat_2013))
print("Umur : ",umur_2013," tahun | ",type(umur_2013))
print("Skor Tes Awal : ",skor_2013," | ",type(skor_2013))
print("ID Token Sinyal: ",token_2013," | ",type(token_2013))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_2013," | ",type(kkm_2013))
print("Apakah Dinyatakan Lulus?: ",lulus_2013," | ",type(lulus_2013))