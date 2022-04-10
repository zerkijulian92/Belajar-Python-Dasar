# Latihan 01

from xml.sax.xmlreader import InputSource


print("=====Latihan 01 ===== ")
# -------0 ++++++ 5-----8 +++++ 11---------
inputUser = float(input(
    "Masukan angka yang bernilai \n > 0 AND < 5 \n OR \n angka yang bernilai > 8 AND < 11 \n : "))

isLebihDariNOL = inputUser > 0
print("Lebih dari 0 = ", isLebihDariNOL)

isKurangDariLima = inputUser < 5
print("Kurang dari 5 = ", isKurangDariLima)

isLebihDariDelapan = inputUser > 8
print("Lebih dari 8 = ", isLebihDariDelapan)

isKurangDariSebelas = inputUser < 11
print("Kurang dari 11 = ", isKurangDariSebelas)

isCorrect = isLebihDariNOL and isKurangDariLima or isLebihDariDelapan and isKurangDariSebelas
print("angka yang anda masukan = ", isCorrect)

print("\n ===== Latihan 02 ======")
# +++++++0---------5+++++++++8----------11+++++++
inputUser = float(
    input("Masukan angka bernilai \n < 0 OR angka > 5 AND < 8 \n OR > 11 : "))

isKurangDariNOL = inputUser < 0
print("Kurang dari 0 = ", isKurangDariNOL)

isLebihDariLima = inputUser > 5
print("Lebih dari 5 = ", isLebihDariLima)

isKurangDariDelapan = inputUser < 8
print("Kurang dari 8 = ", isKurangDariDelapan)

isLebihDariSebelas = inputUser > 11
print("Lebih dari 11 = ", isLebihDariSebelas)

isCorrect = isKurangDariNOL or isLebihDariLima and isKurangDariDelapan or isLebihDariSebelas
print("angka yang anda masukan = ", isCorrect)
