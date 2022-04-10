# latihan konversi satuan temperature sederhana

# Program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI SEDERHANA")
print("==============================")

print("\n*Konversi Celcius Ke Satuan Temperature Lainnya")
print("==================================================")

celcius = float(input("Masukan suhu dalam celcius : "))
print("suhu dalam celcius adalah : ", celcius, "Celcius")

# Celcius - Reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah : ", reamur, "reamur")

# fahrenheit
fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit adalah : ", fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah : ", kelvin, "kelvin")

# ------------------------------------------------------------------------

# ====KONVERSI FAHRENHEIT KE KELVIN===
print("\nKonversi Fahrenheit Ke Kelvin")
print("====================================")
fahrenheit = float(input("Masukan suhu dalam fahrenheit: "))
print("suhu dalam fahrenheit adalah : ", fahrenheit, "fahrenheit")

# fahrenheit ke kelvin
kelvin = (fahrenheit + 459.67) * 5/9
print("suhu dalam kelvin : ", kelvin, "kelvin")

# ===KONVERSI KELVIN KE FAHRENHEIT===
print("\nKonversi Kelvin Ke Fahrenheit")
print("========================================")
kelvin = float(input("Masukan suhu dalam kelvin: "))
print("suhu dalam kelvin adalah : ", kelvin, "kelvin")

# kelvin ke fahrenheit
fahrenheit = (kelvin * 9/5) - 459.67
print("suhu dalam fahrenheit : ", fahrenheit, "fahrenheit")
