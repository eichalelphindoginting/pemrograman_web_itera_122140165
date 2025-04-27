import math_operations as mo
from math_operations import celsius_to_kelvin, celsius_to_fahrenheit

sisi = 5
print(f"Luas Persegi (sisi={sisi}): {mo.luas_persegi(sisi)}")
print(f"Keliling Persegi (sisi={sisi}): {mo.keliling_persegi(sisi)}")


panjang = 8
lebar = 4
print(f"\nLuas Persegi Panjang (panjang={panjang}, lebar={lebar}): {mo.luas_persegi_panjang(panjang, lebar)}")
print(f"Keliling Persegi Panjang (panjang={panjang}, lebar={lebar}): {mo.keliling_persegi_panjang(panjang, lebar)}")

jari_jari = 7
print(f"\nLuas Lingkaran (jari-jari={jari_jari}): {mo.luas_lingkaran(jari_jari):.2f}")
print(f"Keliling Lingkaran (jari-jari={jari_jari}): {mo.keliling_lingkaran(jari_jari):.2f}")

suhu_celsius = 25
print(f"\n{suhu_celsius}°C ke Fahrenheit: {celsius_to_fahrenheit(suhu_celsius):.2f}°F")
print(f"{suhu_celsius}°C ke Kelvin: {celsius_to_kelvin(suhu_celsius):.2f}K")

print(f"\nNilai konstanta PI adalah: {mo.PI}")
