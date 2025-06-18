

# data_angka = [1, 5, 2, 3]

# print(data_angka)

# data_string = ['ucup', 'otong', 'odah']
# print(data_string)

# data_campuran = [1, 'bala-bala', 2, 'cireng']
# print(data_campuran)

# data_range = range(0,10)
# data_list = list(data_range)
# print(data_list)

# list_pake_for = [i*2 for i in range(0,10)]
# print(list_pake_for)


# lis_pake_for_if = [i for i in range(0,10) if i != 5]
# print(lis_pake_for_if)


# list_pake_for = [i for i in range(0,10) if i % 2 == 0]
# print(list_pake_for)


# list_pake_for = [i for i in range(0,10) if i % 2 != 0]
# print(list_pake_for)

# list_pake_for = [i**2 for i in range(0,10) if i % 2 == 0]
# print(list_pake_for)


# ======================================================== #

# manipulasi data list

# menambahkan item data list

# data = ['ucup', 'otong', 'dudung']

# data.insert(1,'asep')

# print(data)


# # menambah di akhir list
# data.append('jajang')
# print(f'ini data untuk yang ditambah di akhir : {data}')


# # menggabungkan list

# data_2 = ['ujang', 'usep', 'dadang']

# data.extend(data_2)

# print(f'ini adalah data gabungan: {data}')


# # merubah data 

# data[2] = 'michel'
# print(data)


# # meremove data 

# data.remove('ujang')
# print(data)



# meremove data paling belakang
# data.pop()
# print(data)

#=================================================================== #

# operasi list

# data_angka = [1, 2, 3, 4, 3, 2, 6, 7, 4, 3]
# print(data_angka)


# jumlah_data_4 = data_angka.count(4)
# jumlah_data_3 = data_angka.count(3)

# print(f'jumlah angka 3 ada: {jumlah_data_3}')
# print(f'jumlah angka 4 ada: {jumlah_data_4}')


# # ambil posisi data
# data = ['ucup', 'otong', 'dudung']
# print(data)

# index_dudung = data.index('dudung')
# index_otong = data.index('otong')
# print(f'indek si otong ada di: {index_otong}')
# print(f'indek si duudng ada di: {index_dudung}')

# # mengurutkan data list

# print(data_angka)
# data_angka.sort()
# print(data_angka)
# data_angka.reverse()
# print(data_angka)

#==================================================================#

# duplikat / copy list

# a = ['ucup', 'otong', 'dudung']
# print(a)

# b = a
# print(b)

# # kita akan merubah member dari a

# a[1] = 'michel'
# b.sort()
# print(a)
# print(b)

# # adres dari kedua list a dan b

# print(hex(id(a)))
# print(hex(id(b)))


# # cara menduplikat data yang benar dengan menggunakan copy
# print('membuat list c  dengan a.copy')

# c = a.copy()

# # dengan menggunakan contoh copy di atas, ini akan membuat list baru
# # dan tidak akan merubah data list a, jika melakukan perubahan data di list c


# print(hex(id(a)))
# print(hex(id(b)))
# print(hex(id(c)))

# print(a)
# print(b)
# print(c)

# print('pembuktian merubah data dari list a,b,c')

# a[0] = 'batistuta'
# c[0] = 'bastian'
# print(a)
# print(b)
# print(c)

# ============================================================================ #

# nested list

# data_0 = [1, 2]
# data_1 = [3, 4]
# data_list_biasa = [1, 2, 3, 4]

# print(data_0)
# print(data_1)
# print(data_list_biasa)


# list_2 = [data_0,data_1]
# print(list_2)


# # contoh penggunaan

# peserta_0 = ['ucup', 25, 'laki-laki']
# peserta_1 = ['otong', 10, 'laki-laki']
# peserta_2 = ['dedeh', 50, 'wanita']
# list_peserta = [peserta_0,peserta_1,peserta_2]
# print(list_peserta)

# for peserta in list_peserta:
#     print(f'nama\t: {peserta[0]}')
#     print(f'umur\t: {peserta[1]}')
#     print(f'gender\t: {peserta[2]}\n')



# ===================================================================================== #

# deep copy nested list


# data_0 = [1, 2]
# data_1 = [3, 4]
# data_list_biasa = [1, 2, 3, 4]


# list_2 = [data_0,data_1]
# print(list_2)

# # mengambil data dari nested list
# data = list_2[1]
# print(data)
# data = list_2[1][0]
# print(data)


# # harus menggunakan import di bawah

# from copy import deepcopy



# ============================================================================================= #


# Looping dari list
# for loop

# kumpulan_angka = [4, 3, 2, 5, 6, 1]

# for angka in kumpulan_angka:
#     print(angka)


# peserta = [ 'ucup', 'otong', 'dadang', 'diding', 'dudung']


# for nama in peserta:
#     print(nama)
 

# # enumerate

# peserta = [ 'ucup', 'otong', 'dadang', 'diding', 'dudung']

# for index, data in enumerate(peserta):
#     print(index, data)



# ================================================================================ #

# LATIHAN DATA LIST

daftar_buah = [['Apel', 20, 10000], ['Jeruk', 15, 15000], ['Anggur', 25, 20000]]


print('''
      === Selamat Datang di Pasar Buah===
      
      List Menu :
      1. Menampilkan Daftar Buah
      2. Menambahkan Buah
      3. Menghapus Buah
      4. Membeli Buah
      5. Exit Program
      ''')

while True:
    pilihan = int(input('Masukkan angka Menu yang ingin dijalankan: '))
    if pilihan == 1:
        print('Daftar Buah\n')
        print('Index\t|Nama\t\t|Stock\t\t|Harga')
        for i,j in enumerate(daftar_buah):
            print(f'{i+1}\t|{j[0]}\t\t|{j[1]}\t\t|{j[2]}')


    elif pilihan == 2:
        nama_buah = input('Masukkan Nama Buah: ')
        stock = int(input('Masukkan Stock Buah: '))
        harga = int(input('Masukkan Harga Buah: '))
        daftar_baru = [nama_buah, stock, harga]
        daftar_buah.append(daftar_baru)
        print('Index\t|Nama\t\t|Stock\t\t|Harga')
        for i, j in enumerate(daftar_buah):
            print(f'{i+1}\t|{j[0]}\t\t|{j[1]}\t\t|{j[2]}')


    elif pilihan == 3:
        for i, j in enumerate(daftar_buah):
            print(f'{i+1}\t|{j[0]}\t\t|{j[1]}\t\t|{j[2]}')

        hapus = int(input('Masukkan index buah yang ingin dihapus: '))
        hapus -= 1
        del daftar_buah[hapus]
        print('Index\t|Nama\t\t|Stock\t\t|Harga')
        for i, j in enumerate(daftar_buah):
            print(f'{i+1}\t|{j[0]}\t\t|{j[1]}\t\t|{j[2]}')


    elif pilihan == 4:
        list_belanja = []
        while True:
        
            import math
            print('Daftar Buah\n')
            print('Index\t|Nama\t\t|Stock\t\t|Harga')
            for i, j in enumerate(daftar_buah):
                print(f'{i+1}\t|{j[0]}\t\t|{j[1]}\t\t|{j[2]}')
            beli = int(input('Masukkan index yang ingin dibeli: '))
            beli -= 1
            jumlah = 0
            while True:
                jumlah = int(input('Masukkan jumlah yang ingin dibeli: '))
                if jumlah > daftar_buah[beli][1]:
                    print('terlalu banyak')
                else:
                    break
                
                
            a = daftar_buah[beli][0]
            b = jumlah
            c = daftar_buah[beli][2]
            d = jumlah * daftar_buah[beli][2]
            belanja = [a,b,c,d]
            list_belanja.append(belanja)
            print('Isi Cart:')
            print('Nama\t|QTY\t|Harga')
            for j,i in enumerate(list_belanja):
                print(f'{i[0]}\t|{i[1]}\t|{i[2]}')


            lanjut = input('Mau beli yang lain? (ya/tidak) = ')
            if lanjut == 'tidak':
                print('Daftar Belanja')
                print('Nama\t|QTY\t|Harga\t|Total Harga')
                for j,i in enumerate(list_belanja):
                    print(f'{i[0]}\t|{i[1]}\t|{i[2]}\t|{i[3]}')
                
                print(f'Total yang harus dibayar = {sum(item[3] for item in list_belanja)}')
                bayar = int(input('Masukkan Jumlah uang: '))

                if bayar == sum(item[3] for item in list_belanja):
                    print('Terimakasih')
                elif bayar > sum(item[3] for item in list_belanja):
                    print('Terimakasih')
                    print(f'Uang kembalian anda sebesar {bayar-sum(item[3] for item in list_belanja)}')
                elif bayar < sum(item[3] for item in list_belanja):
                    print(f'Uang anda kurang sebesar {sum(item[3] for item in list_belanja)-bayar}')
            
                break
            
    elif pilihan == 5:
        print('Exit Program')
        break
        
        












