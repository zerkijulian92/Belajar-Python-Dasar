# EPISODE input user

#  data yang dimasakun pasti string
data = input("Masukan data: ")
print("data = ", data, "type =", type(data))

# jika kita ingin mengambil int, maka
angka = float(input("masukan angka: "))
angka = int(input("masukan"))
print("data = ", angka, "type = ", type(angka))

# bagaimana dengan boolean
biner = bool(input("masukan nilai boolean: "))
print("data = ", biner, "type =", type(biner))

# Casting tipe data boolean ke integer
biner = bool(int(input("masukan nilai boolean: ")))
print("data =", biner, "type =", type(biner))
