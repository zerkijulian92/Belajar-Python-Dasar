# Operasi dan manipulasi string (Part 1)

# 1 Menyambung string (concatenate)
from cgi import print_arguments


nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_Lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_Lengkap)

# 2. Menghitung Panjang String
panjang = len(nama_Lengkap)
print("panjang dari " + nama_Lengkap + " = " + str(panjang))

# 3. Operator untuk string
# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_Lengkap
print(d + " ada di " + nama_Lengkap + " = ", str(status))

D = "D"
status = D in nama_Lengkap
print(D + " ada di " + nama_Lengkap + " = ", str(status))

D = "D"
status = D in nama_Lengkap
print(D + " ada di " + nama_Lengkap + " = ", str(status))

d = "d"
status = d not in nama_Lengkap
print(d + " tidak ada di " + nama_Lengkap + " = ", str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_Lengkap[0])
print("index ke-6 : " + nama_Lengkap[6])
print("index ke-(-1) : " + nama_Lengkap[-1])
print("index ke-(-2) : " + nama_Lengkap[-2])
print("index ke-[0:3]: " + nama_Lengkap[0:4])
print("index ke-[3:7]: " + nama_Lengkap[3:8])
print("index ke-[0,2,4,6,8,10]: " + nama_Lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_Lengkap))

# item paling besar
print("paling besar : " + max(nama_Lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))
