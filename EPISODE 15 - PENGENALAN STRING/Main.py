# PENGENALAN STRING

from cgi import print_arguments


data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '-------'
    2. dengan menggunakan dounle quote "-----"
'''

data = 'Menggunakan singel qoute'
print(data)

data = "Menggunakan double qoute"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \
# membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it')

# backslash
print("C:\\user\\Ucup")

# tab
print("ucup\t\t\totong, semakin jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama. \nbaris kedua.")  # LF -> line feed -> unix, macos, linux
print("baris pertama. \rbaris kedua.")  # commodore, acorn, lisp
print("baris pertama. \r\nbaris kedua.")  # dipakai oleh windows

# 3. String literal atau raw

# hati-hati
print('c:\nnew folder')  # akan salah pathnya

# menggunakan raw string (r)
print(r'C:\new \t\r\folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD
Webiste " www.ucup.com/newID
""")
