# OPERASI DAN MANIPULASI STRING (PART 2)

# # merubah case dari string

# merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)

salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KeCee AbiIIEeEzZZZZZZZ"
print("normal = " + alay)

alay = alay.lower()
print("lower = " + alay)

# # pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()  # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()  # hasilny bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <----------- untuk mengecek semuanya huruf
alpha01 = "dibalikawan"
apakah_alpha = alpha01.isalpha()  # hasilnya bool
print(alpha01 + " is alpha = " + str(apakah_alpha))

alpha02 = "menghapus jejakmu"
apakah_alpha = alpha02.isalpha()
print(alpha02 + " is alpha = " + str(apakah_alpha))

# isalnum() <----------- untuk mengecek huruf dan angka
alnum = "iniNomorku0821345677"
apakah_alnum = alnum.isalnum()
print(alnum + " is alnum = " + str(apakah_alnum))
# isdecimal() <--------- untuk mengecek angka saja
# isspace() <---------- untuk mengecek spasi, tab, newline (\n)

# istitle() <---------- semua kata dimulai dengan huruf besar
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()  # bool
print(judul + " is title = " + str(cek_judul))

judul = "It is Okay Not To Be Orkay"
cek_judul = judul.istitle()  # bool
print(judul + " is title = " + str(cek_judul))

# ngecek komponen startswitch() endswitch() <--- keren
# jika kata di awal sama maka akan true
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

# jika kata di akhir sama makan akan true
cek_end = "Sangjanim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

# penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = '-'.join(pisah)
print(gabungan)

# split
gabungan = "aku,sayang,kamu"
print(gabungan.split(','))

# alokasi karakter rjust(), ljust() center()
kanan = "kanan".rjust(10)
print(""+kanan+"")

kiri = "kiri".ljust(10)
print(""+kiri+"")

kiri = "kiri".ljust(10, ":")
print(""+kiri+"")

tengah = "tengah".center(20, ":")
print(""+tengah+"")

# kebalikannya -> strip()
tengah = tengah.strip(":")  # menghilangkan tanda :
print(""+tengah+"")
