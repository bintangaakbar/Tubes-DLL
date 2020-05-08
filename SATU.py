# barang =  ['kunci', 'ember', 'ban', 'mobil', 'motor']
# print(barang)

# # beberp method
# # method untk menambah data ke list
# barang.append('sepeda')
# print(barang)

# barang.extend('dompet')
# print(barang)

# barang.insert(3, 'sepeda')
# print(barang)

# # method untuk menghitung anggota

# jumlahsepeda = barang.count('sepeda')
# print(jumlahsepeda)
 
# # print("TEST")
# # data = 'test'

# # for i in data:
# #     print(i)

# barang.remove('sepeda')
# print(barang)

# barang.reverse()
# print(barang)
# print("="*100)
# stuff = barang.copy()
# stuff.append('gelas')
# print(stuff)
# print(barang)

# print("\t PROGRAM KONVERSI HARI")
# hari=('minggu','senin','selasa','rabu','kamis','jumat','sabtu')
# test = int(input("Hari Ke ? :   "))
# if (1 <= test <= 7):
#     print(hari[test-1])
# else:
#     print("hari tidak ada")

# buah1 = str(input("Masukkan Buah Ke-1 : "))
# buah2 = str(input("Masukkan Buah Ke-2 : "))
# buah3 = str(input("Masukkan Buah Ke-3 : "))
# buah4 = str(input("Masukkan Buah Ke-4 : "))
# buah5 = str(input("Masukkan Buah Ke-5 : "))


# print("\t PROGRAM DATA STOK BUAH")
# buah = {'jeruk', 'apel', 'naga', 'mangga', 'pisang'}
# print("Stok Buah", buah)
# mau = str(input("Cari Buah Apa ?    "))
# if mau in buah:
#     print("buah", mau, "tersedia")
# c = str(input("Mau beli [y/n] :   "))
# if c == 'y':
#     print(buah.discard(mau))
# else:
#     print("Oke")
# print(buah)


daftar_lab = {
     'DASPRO' : {
         'praktikum' : 'Algoritma dan pemrograman',
         'semester' : 2
     },
     'ERP' : {
         'Praktikum' : 'SAP 01 Fundamental',
         'semester' : 1
     }
 }

print(daftar_lab)
for key, value in daftar_lab.items():
     print('Nama Lab  : ', key)
     for key2 in value:
         print(key2, ':', value[key2])
     print()
