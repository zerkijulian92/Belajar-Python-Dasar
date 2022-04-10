# LATIHAN KOMPARASI DAN LOGIKA

# membuat gabungan area rentang dari angka

# ++++++3--------------10+++++++++
inputUser = float(input(
    "Masukan angka yang bernilai \n kurang dari 3 \n atau \n lebih besar dari 10 :"))

# ++++++3--------------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari)

# -----------10+++++++++++++
# Memeriksaa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 = ", isLebihDari)

# +++++++3-----------10+++++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)

# ----3++++++++10------------
# kasus irisan
print("\n", 10*"=", "\n")
inputUser = float(
    input("Masukan angka yang bernilai \n lebih dari 3 \n dan \n kurang dari 10 : "))

# ---------3+++++++++++
isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

# +++++++10--------------
isKurangDari = inputUser < 10
print("Kurang dari 10 = ", isKurangDari)

# ----3++++++++10------------
isCorrect = isLebihDari and isKurangDari
print("angka yang anda masukan: ", isCorrect)
