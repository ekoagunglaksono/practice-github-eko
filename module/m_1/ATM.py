saldo = 500000

while True:
    print('\n=== ATM ===')
    print('1. Cek Saldo')
    print('2. Taril Tunai')
    print('3. Keluar')
    pilihan = input('Pilih menu (1/2/3): ')


    if pilihan == '1':
        print(f'Saldo Anda: Rp. {saldo}')
    elif pilihan == '2':
        tarik = int(input('Masukan jumlah uang: '))
        if tarik <= saldo:
            saldo -= tarik
            print(f' berhasil tarik sebesar Rp. {tarik}. sisa saldo anda sebesar: Rp. {saldo}')
        else:
            print('Saldo tidak cukup')
    elif pilihan == '3':
        print('Terimakasih telah menggunakan ATM.')
        break
    else:
        print('pilihan tidak valid.')
        
