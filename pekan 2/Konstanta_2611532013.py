from typing import final
PI: final = 3.14
print("pi: %f" % (PI))
jari_2013 = float (input('Masukkan nilai jari-jari:'))
luas_2013 = PI * jari_2013 * jari_2013
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2013, luas_2013))