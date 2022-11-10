import os
import time
def hapus():
    os.system('cls')
    
# Container dari seluruh data yang ada
user = ['miaw','undifined']
password = ['admins123','undifined']
note = ['admin','member']
roti = [['Roti Cokelat', 6000, 30],
        ['Roti Buah', 6000, 30],
        ['Roti Vanilla', 7000, 30],
        ['Roti Gepeng', 2000, 100]]

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
    if login1 == 'miaw' and pass1 == 'admins123':
        menu_admin()
    elif login1 == user[1] and pass1 == password[1]:
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
    login2= input('Masukkan Username> ')
    pass2 = input('Masukkan Password> ')
    print('='*30)
    user[1] = login2
    password[1] = pass2
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
            #Try and Except untuk error handling
            try:
                print('='*30)
                rb = input('Masukkan Nama Roti> ')
                hr = int(input('Masukkan Harga Roti> '))
                stok = int(input('Masukkan Stok Roti> '))
                roti.append([rb,hr,stok])
                roti.sort()
                input('Roti Telah Ditambahkan, tekan enter untuk kembali!')
                menu_admin()
            except:
                print('Inputan anda salah ')
                input('Tekan enter untuk kembali')
                menu_admin()
        
        # Pilihan 2 (List Seluruh Roti)
        elif pilih == '2':
            print('='*57)
            print("Nama\t\t\t|Harga\t\t|Stok\t\t|")
            for i in range(len(roti)):
                for j in range(len(roti[i])):
                    print(roti[i][j], end='\t\t|')
                print()
                continue
            print('='*57)
            input('\nTekan Enter untuk kembali ke menu_admin')
            menu_admin()

        # Pilihan 3 (Menghapus Data Roti berdasarakan Index)
        elif pilih == '3':
            print('='*30)
            baris = int(input('Masukkan Baris/Index Roti> '))
            a = 3
            try:
                del roti[baris]
                a-=1
                roti.sort()
                input('Roti Telah Dihapus, tekan enter untuk kembali!')
                menu_admin()     
            except:
                hapus()
                print('Data Kosong / Roti Sudah dihapus')
                input('Tekan Enter untuk kembali')
                menu_admin
        
        # Pilihan 4 (Perubahan Data Roti, Mulai dari nama,harga,dan stoknya)
        elif pilih == '4':
                cr2 = len(roti) - 1
                nr2 = input("Masukkan Nama Roti> ")
                while (cr2 >= 0):
                    if (nr2 == roti[cr2][0]):
                        break
                    else:
                        cr2 -= 1
                if (cr2 >= 0):
                    harga = int(input("Masukkan Harga Roti> "))
                    roti[cr2][1] = harga
                    stok = int(input("Masukkan Stok Roti> "))
                    roti[cr2][2] = stok
                    hapus()
                else:
                    hapus()
                    print("Maaf nama barang yang anda masukkan tidak ada")
        
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
|       <2> Beli Roti          |
|       <3> Keluar             |
================================
==>        Miaw Bakery       <==
================================''')

    menu = input('\nPilih Menu> ')

    # Pilihan 1 (Melihat Daftar Roti)
    if menu == '1':
        hapus()
        print('='*57)
        print("Nama\t\t\t|Harga\t\t|Stok\t\t|")
        for i in range(len(roti)):
            for j in range(len(roti[i])):
                print(roti[i][j], end='\t\t|')
            print()
            continue
        print('='*57)
        input('\nTekan Enter untuk kembali ke menu_admin')
        menu_member()

    # Pilihan 2 (Pembelian Roti)
    elif menu == '2':
        hapus()
        print('='*57)
        print("Nama\t\t\t|Harga\t\t|Stok\t\t|")
        for i in range(len(roti)):
            for j in range(len(roti[i])):
                print(roti[i][j], end='\t\t|')
            print()
            continue
        print('='*57)
        y = 1
        while True:
            y+=1
            print('#Note : Pemilihan baris harus dimulai dari 0')
            baris = int(input("\nMasukkan Baris (0/1/2/3/...)> "))
            x = int(input("Masukkan jumlah pesanan :"))
            y = roti[baris][1] * x
            roti[baris][2]-= x
            print(f"\nHarga> Rp.{y:,}")
            print(f'Total Harga yang harus Dibayar> Rp.{y:,}')
            pesan1 = input("\nApakah anda ingin memesan lagi?(y/t)> ")
            
            # Jika user ingin memesan lagi, maka code dibawah akan di eksekusi kembali
            while pesan1 == "y" or pesan1 == "Y":
                print('#Note : Pemilihan baris harus dimulai dari 0')
                baris1 = int(input("\nMasukkan Baris (0/1/2/3/...)> "))
                x1 = int(input("Masukkan jumlah pesanan : "))
                y1 = roti[baris1][1] * x1
                roti[baris1][2]-= x1
                y+=y1
                print(f"\nHarga> Rp.{y1:,}")
                print(f'Total Harga yang harus Dibayar> Rp.{y:,}')
                pesan2 = input("\nApakah anda ingin memesan lagi?(y/t)>")
                if pesan2 == 't' or pesan2 == 'T':
                    hapus()
                    print(f"           Total Tagihan Anda> Rp.{y:,}")
                    print("=========================================================")
                    print("     Terima kasih telah membeli Di Miaw Bakery :3        ")
                    print("=========================================================")
                    input('      Tekan enter untuk kembali ke menu_member')
                    menu_member()
                    break
            # Jika user hanya membeli 1 jenis Roti maka, Code dibawah akan di eksekusi
            else:
                hapus()
                print(f"           Total Tagihan Anda> Rp.{y:,}")
                print("=========================================================")
                print("       Terima kasih telah membeli Di Miaw Bakery :3 ")
                print("=========================================================")
                input('        Tekan enter untuk kembali ke menu_member')
                menu_member()

                
    # Menu Keluar dari tampilan member/user setelah membeli/melihat Roti
    elif menu == '3':
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
