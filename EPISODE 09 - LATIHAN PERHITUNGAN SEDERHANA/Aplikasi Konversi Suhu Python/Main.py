# APLIKASI KONVERSI SUHU SEDERHANA 1.0

print("\nAPLIKASI KONVERSI SUHU SEDERHANA 1.0 By Zerki")
print("===============================================")

print("\nKonversi Celcius (℃ ) Ke Temperature Lainnya")
print("================================================")

celcius = (float(input("Masukan Suhu dalam Celcius (℃ ) : ")))
print("Suhu dalam Celcius adalah : ", celcius, "℃")

# Celcius Ke Fahrenheit
fahrenheit = celcius * (9/5) + 32
print("Konversi Celcius (℃ ) ke Fahrenheit (℉ ) adalah : ", fahrenheit, "℉")

# Celcius Ke Kelvin
kelvin = celcius + 273.15
print("Konversi Celcius (℃ ) ke Kelvin (K) adalah : ", kelvin, "K")

# Celcius Ke Reamur
reamur = celcius * (4/5)
print("Konversi Celcius (℃ ) ke Reamur (°Ré) adalah : ", reamur, "°Ré")

# ------------------------------------------------------------------------------

print("\nKonversi Fahrenheit (°F ) Ke Temperature Lainnya")
print("================================================")

fahrenheit = (float(input("Masukan Suhu dalam Fahrenheit (°F ) : ")))
print("Suhu dalam Fahrenheit (°F ) adalah : ", fahrenheit, "℉")

# Fahrenheit Ke Celcius
celcius = (fahrenheit - 32) * (5/9)
print("Konversi Fahrenheit (°F ) ke Celcius (°C ) adalah : ", celcius, "°C")

# Fahrenheit Ke Kelvin
kelvin = (fahrenheit + 459.67) * (5/9)
print("Konversi Fahrenheit (°F ) ke Kelvin (K) adalah : ", kelvin, "K")

# Fahrenheit Ke Reamur
reamur = (fahrenheit - 32) * (4/9)
print("Konversi Fahrenheit (°F ) ke Reamur (°Ré) adalah : ", reamur, "°Ré")
