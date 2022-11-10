import os
import time
def hapus():
    os.system('cls')
    
# Container dari seluruh data yang ada
data = {
    'admin' : {
        'username' : 'miaw',
        'password' : 'admins123',
    },
    'user' : {
        'user_member' :'undifined',
        'user_password' : 'undifined'}
}
roti = {
    1 :{'Roti Buah      ' : '6000'},
    2 :{'Roti Cokelat   ' : '6000'},
    3 :{'Roti Gepeng    ' : '2000'},
    4 :{'Roti Vanilla   ' : '7000'}
}


# Menu Awal
def awal():
    hapus()
    print('''==========================
<1> Login
<2> Registrasi
<3> keluar
==========================''')
# Kondisi Pilihan menu
    pilih = input('\nPilih Menu> ')
    if pilih == '1':
        login()
    elif pilih == '2':
        registrasi()
    elif pilih == '3':
        print('''
Sampai Jumpa Lagi ≋≋≋≋≋̯̫⌧̯̫(ˆ•̮ ̮•ˆ) ''')
        time.sleep(3)
        exit()
    else:
        input('Pilihan harus Angka, Tekan Enter untuk kembali !')
        awal()
# Login menu (Sebagai Admin/user)
def login():
    hapus()
    print('='*30)
    login1 = input('Masukkan Username> ')
    pass1 = input('Masukkan Password> ')
    if login1 == data['admin']['username'] and pass1 == data['admin']['password']:
        menu_admin()
    elif login1 == data['user']['user_member'] and pass1 == data['user']['user_password']:
        menu_member()
    elif login1 == '' and pass1 == '':
        input('Anda belum terdaftar, Silahkan Registrasi !')
        awal()
    else:
        input('username/password salah, Tekan Enter untuk kembali!')
        login()

# Registrasi (Khsuus untuk user harus registrasi terlebih dahulu)
def registrasi():
    hapus()
    print('='*30)
    data['user']['user_member'] = input('Masukkan Username> ')
    data['user']['user_password'] = input('Masukkan Password> ')
    print('='*30)
    input("Registrasi Berhasil, Sekarang Tekan Enter untuk ke Menu_Login !")
    awal()

# Menu dari Admin, Untuk CRUD data Roti
def menu_admin():
    hapus()
    percobaan = 3
    while True:
        print('''
           =＾● ⋏ ●＾=
=========  Menu Admin  =========
|        ==============        |
|                              |
|   <1> Tambah Roti            |
|   <2> List Roti              |
|   <3> Hapus Roti             |
|   <4> Perbarui Jumlah roti   |
|   <0> Keluar                 |
================================
==>        Miaw Bakery       <==
================================''')
        pilih = input('\nPilih Menu> ')
        hapus()
        # Pilihan 1 (Penambahan Roti)
        if pilih == '1':
            print('='*30)
            print("No | Nama\t\t|Harga")
            print('='*30)
            for i,j in roti.items():
                print(f"{i}.)", end='')
                for nama,harga in j.items():
                    print(f' {nama}\t|{harga}')
                print()
                continue
            #Try and Except untuk error handling
            data = int(input('Masukkan Jumlah Roti yang ingin Di input> '))
            try:
                for i in range(data):
                    no = int(input('\nMasukkan No Roti Selanjutnya> '))
                    nr = input('Masukkan Nama Roti> ')
                    hr = input('Masukkan Harga Roti> ')
                    roti[no] = {(f'{nr}   '):hr,}
                    input('Roti Telah Ditambahkan')
                    continue
                menu_admin()
            except:
                print('Inputan anda salah ')
                input('Tekan enter untuk kembali')
                menu_admin()
        
        # Pilihan 2 (List Seluruh Roti)
        elif pilih == '2':
            print('='*30)
            print("No | Nama\t\t|Harga")
            print('='*30)
            for i,j in roti.items():
                print(f"{i}.)", end='')
                for nama,harga in j.items():
                    print(f' {nama}\t|{harga}')
                print()
                continue
            print('='*30)
            input('\nTekan Enter untuk kembali ke menu_admin')
            menu_admin()

        # Pilihan 3 (Menghapus Data Roti berdasarakan Index)
        elif pilih == '3':
            print('='*30)
            print("No   Nama\t\t|Harga")
            print('='*30)
            for i,j in roti.items():
                print(f"{i}.)", end='')
                for nama,harga in j.items():
                    print(f' {nama}\t|{harga}')
                print()
                continue
            print('='*30)
            try: 
                no = int(input('Masukkan Nomor Roti yang ingin dihapus> '))
                if 0 < no <= len(roti):
                    while 0 < no < len(roti):
                        nm = no+1
                        roti.update({no : roti[nm]})
                        no+=1
                    del roti[no]
                input("Roti berhasil di hapus")
                menu_admin()
            except:
                input('Inputan salah, Ulangi')
                menu_admin()
        # Pilihan 4 (Perubahan Data Roti, Mulai dari nama,harga,dan stoknya)
        elif pilih == '4':
            print('='*30)
            print("No   Nama\t\t|Harga")
            print('='*30)
            for i,j in roti.items():
                print(f"{i}.)", end='')
                for nama,harga in j.items():
                    print(f' {nama}\t|{harga}')
                print()
                continue
            print('='*30)
            
            ur = input('Ingin ubah Harga?> ')
            if ur == 'y' or ur == 'Y':
                no = int(input('\nMasukkan No Roti> '))
                nr = input('Masukkan Nama Roti> ')
                hb = int(input('Masukkan Harga Baru Roti> '))
                roti[no] = ({f'{nr}      ' : hb})
                input('OK')
                menu_admin()
            
            elif ur == 't' or ur == 'T':
                input('Tekan Enter untuk kembali !')
                menu_admin()
            
            else:
                input('Inputan anda salah, Ulangi')
                menu_admin()
                        
        
        # Pilihan 0 (Kembali ke menu awal)
        elif pilih == '0':
           awal()
        # Jika User menginputkan string
        else:
            input("Pilihan harus angka, tekan Enter untuk kembali")
            menu_admin()

# Menu untuk member, Jika ingin membeli Roti
def menu_member():
    hapus()
    print('''
========= =＾● ⋏ ●＾= ==========
|       ===============        |
|                              |
|       <1> List Roti          |
|       <2> Keluar             |
================================
==>        Miaw Bakery       <==
================================''')

    menu = input('\nPilih Menu> ')

    # Pilihan 1 (Melihat Daftar Roti)
    if menu == '1':
        hapus()
        print('='*30)
        print("No | Nama\t\t|Harga")
        for i,j in roti.items():
            print(f"{i}.)", end='')
            for nama,harga in j.items():
                print(f' {nama}\t|{harga}')
            print()
            continue
        print('='*30)
        input('\nTekan Enter untuk kembali ke menu_admin')
        menu_member()

    # Menu Keluar dari tampilan member/user setelah membeli/melihat Roti
    elif menu == '2':
        hapus()
        print('============================================')
        print("Terima kasih telah mampir ke Miaw Bakery :3 ")
        print('Sampai Jumpa Dilain waktu ≋≋≋≋≋̯̫⌧̯̫(ˆ•̮ ̮•ˆ)')
        print('============================================')
        time.sleep(1)
        exit()

    else:
        input('Pilihan harus angka, tekan Enter untuk kembali ke menu_member')
        menu_member()

awal()
