import os
import time
def hapus():
    os.system("cls")

admin ={
    'user': 'a',
    'pass': 'a'
}

nama_user = ['user1','user2','user3']
pass_user = ['12','13','14']
username_sekarang = []
pbb = {}
gaji = {}
semua_pajak_motor = {}
semua_pajak_mobil = {}

def data_pbb():
    hapus()
    if pbb == {}:
        input('Data Kosong / Tidak Ada')
        menu_admin()
    for k1,v1 in pbb.items():
        print("data ke -",k1)
        for k2,v2 in v1.items():
            print(f'{k2}{v2:,}')
        print('='*40)
        print()
    

def data_gaji():
    hapus()
    if gaji == {}:
        input('Data Kosong / Tidak Ada')
        menu_admin()
    for k1,v1 in gaji.items():
        print("data ke -",k1)
        for k2,v2 in v1.items():
            print(f'{k2}{v2:,}')
        print('='*40)
        print()

def data_pajakmotor():
    hapus()
    if semua_pajak_motor == {}:
        input('Data Kosong / Tidak Ada')
        menu_admin()
    for k1,v1 in semua_pajak_motor.items():
        print("data ke -",k1)
        for k2,v2 in v1.items():
            print(f'{k2}{v2:,}')
        print('='*40)
        print()

def data_pajakmobil():
    hapus()
    if semua_pajak_mobil == {}:
        input('Data Kosong / Tidak Ada')
        menu_admin()
    for k1,v1 in semua_pajak_mobil.items():
        print("data ke -",k1)
        for k2,v2 in v1.items():
            print(f'{k2}{v2:,}')
        print('='*40)
        print()

def rumus_pbb():
    try:
        hapus()
        jml1 = int(input("Masukan Jumlah Data yang ingin dimasukan>  "))
        if jml1 < 0:
            input("Jumlah Data tidak valid")
            rumus_pbb()
        print("\t\t\t\tTambah DATA")
        for i in range(jml1) :
            luas_tanah = int(input('\nMasukkan Luas tanah (/m)> '))
            if luas_tanah < 0:
                input('Ukuran Luas tanah Tidak valid')
                rumus_pbb()
            harga1 = int(input('Harga tanah (/m)> Rp.'))
            if harga1 < 0:
                input('Harga tanah Tidak valid')
                rumus_pbb()
            tanah = luas_tanah*harga1
            
            luas_bangunan = int(input('Masukkan Luas Bangunan> '))
            if luas_bangunan < 0:
                input('Ukuran Luas Bangunan Tidak valid')
                rumus_pbb()
            if luas_bangunan > luas_tanah:
                input('Luas bangunan Tidak boleh lebih dari Luas Tanah')
                rumus_pbb()
                
            harga2 = int(input('Harga Bangunan (/m)> Rp.'))
            if harga2 < 0:
                input('Harga bangunan Tidak valid')
                rumus_pbb()
            bangunan = luas_bangunan*harga2

            njop = tanah + bangunan

            if njop <= 1000000000:
                    njkp = 0.1/100 * njop
            elif njop > 1000000000 and njop <= 2000000000:
                    njkp = 0.2/100 * njop
            elif njop > 2000000000:
                    njkp = 0.3/100 * njop

            print("Data Ke-",i+1)
            print(f'''
<1> Total Harga Tanah       > Rp.{tanah:,}
<2> Total Harga Bangunan    > Rp.{bangunan:,}
<3> NJOP                    > Rp.{njop:,}
<4> Total Tagihan PBB adalah> Rp.{njkp:,}''')
            print('='*30)
            
            updatepbb = {
                'Luas tanah     > ': luas_tanah,
                'Luas bangunan  > ': luas_bangunan,
                'Pajak          > Rp.': njkp
            }
            pbb[len(pbb)+1]= updatepbb
        input('Tekan Enter Kembali')
        if username_sekarang[0] in nama_user:
            menuMember1()
        else:
            menu_admin()
        
    except ValueError:
        input('Inputan Harus Angka, Ulangi!')
        if username_sekarang[0] in nama_user:
            menuMember1()
        else:
            menu_admin()
        
    
def rumus_gaji():
    hapus()
    try:
        jml2 = int(input('Masukkan Jumlah Data Gaji yang ingin di input> '))
        if jml2 < 0:
            input("Jumlah Data tidak valid")
            rumus_gaji()
        print('<<<Tambah data>>>')
        for i in range(jml2):
            gajibersih = float(input('Masukkan Gaji Bersih Bulanan> Rp. '))
            if gajibersih <= 0:
                input("Gaji harus positif")
                rumus_gaji()
            gaji_per_tahun = gajibersih*12
            print(f'''
        gaji pertahun adalah Rp.{gaji_per_tahun:,}
        ''')
            if gaji_per_tahun <= 54000000:
                print('Anda tidak wajib membayar pajak')
                input('Tekan Enter Untuk kembali')
                if username_sekarang[0] in nama_user:
                    menuMember1()
                else:
                    menu_admin()
            print('''
    ====Penghasilan Tidak Kena Pajak====
    1. Pribadi
    2. Menikah
    3. Menikah, 1 anak
    4. Menikah, 2 anak
    5. Menikah, 3 anak atau lebih
    =====================================
    ''')
            ptkp = int(input('Masukkan Pilihan Sesuai Data Anda> '))
            if ptkp == 1:
                pkp = gaji_per_tahun - 54000000
            elif ptkp == 2:
                pkp = gaji_per_tahun - (54000000+ 4500000)
            elif ptkp == 3:
                pkp = gaji_per_tahun - (54000000 + 4500000 + 4500000)
            elif ptkp == 4:
                pkp = gaji_per_tahun - (54000000 + 4500000 + 4500000 + 4500000)
            elif ptkp == 5:
                pkp = gaji_per_tahun - (54000000 + 4500000 + 4500000 + 4500000 + 4500000)
            else:
                input('Inputan anda salah !, Silahkan Ulangi')
                rumus_gaji()
                
            print(f'''
        Penghasilan kena pajak Rp.{pkp:,}
        ''')
            if pkp >=0 and pkp <= 50000000:
                pph = pkp * (5/100)
            elif pkp > 50000000 and pkp <= 250000000:
                pph1 = 50000000 * (5/100)
                pph2 = (pkp-50000000) * (15/100)
                pph = pph1 + pph2
            elif pkp > 250000000 and pkp <= 500000000:
                pph1 = 50000000 * (5/100)
                pph2 = 250000000 * (15/100)
                pph3 = (pkp-50000000-250000000) * (25/100)
                pph = pph1 + pph2 + pph3
            elif pkp > 500000000:
                pph1 = 50000000 * (5/100)
                pph2 = 250000000 * (15/100)
                pph3 = 500000000 * (25/100)
                pph4 = (pkp-50000000-250000000-500000000) * (30/100)
                pph = pph1 + pph2 + pph3 + pph4
            else:
                print('Anda tidak wajib membayar pajak')
                input('Tekan Enter Kembali')
                if username_sekarang[0] in nama_user:
                    menuMember1()
                else:
                    menu_admin()

            print("Data Ke-",i+1)
            print(f'''
        gaji pertahun adalah           > Rp. {gaji_per_tahun:,}
        Penghasilan kena pajak         > Rp. {pkp:,}
        Pajak Yang Harus Dibayar adalah> Rp. {pph:,}
        ''')
            print('='*30)
            updategaji = {
                'Gaji /Tahun> Rp.': gaji_per_tahun,
                'PKP        > Rp.': pkp,
                'PPH        > Rp.': pph
            }
            gaji[len(gaji)+1]= updategaji
        input('Tekan Enter Kembali')
        if username_sekarang[0] in nama_user:
            menuMember1()
        else:
            menu_admin()

    except ValueError:
        input('Inputan Harus Angka, Ulangi !')
        if username_sekarang[0] in nama_user:
            menuMember1()
        else:
            menu_admin()

def rumus_pajakmotor():
    hapus()
    try:
        jml3 = int(input('Masukkan Jumlah Data yang mau diinput> '))
        if jml3 < 0:
            input("Jumlah Data tidak valid")
            rumus_pajakmotor()
        for i in range(jml3):
            pkb_motor = int(input('Masukkan Nominal PKB> Rp. '))
            if pkb_motor < 0:
                input('PKB Motor Tidak valid')
                rumus_pajakmotor()
            tahun_kepemilikan_motor = int(input('Masukkan Lama Tahun Kepemilikan Kendaraan> '))
            if tahun_kepemilikan_motor < 0:
                input('Tahun Kepemilikan Harus Bernilai Positif')
                rumus_pajakmotor()
            swdkllj_motor = 35000 
            administrasi_motor = 100000 
            tnkb_motor = 60000 
            if tahun_kepemilikan_motor % 5 == 0:
                pajak_motor = pkb_motor + swdkllj_motor + administrasi_motor + tnkb_motor
            else:
                pajak_motor = pkb_motor + swdkllj_motor + administrasi_motor
            
            print("Data ke-",i+1)
            print(f'''Pajak motor> Rp.{pajak_motor:,}''')
            print('='*30)
            update_pjkmtr = {
                'PKB                    > Rp.': pkb_motor,
                'Lama Tahun Kepemilikan > ': tahun_kepemilikan_motor,
                'Pajak Motor            > Rp.': pajak_motor
            }
            semua_pajak_motor[len(semua_pajak_motor)+1]= update_pjkmtr
        input('Tekan Enter Kembali')
        if username_sekarang[0] in nama_user:
            menuMember1()
        else:
            menu_admin()
        
    except ValueError:
        input('Inputan Harus angka, Ulangi !')
        if username_sekarang[0] in nama_user:
            menuMember1()
        else:
            menu_admin()
        

def rumus_pajakmobil():
    hapus()
    try:
        jml4 = int(input('Masukkan Jumlah Data yang mau di input> '))
        if jml4 < 0:
            input("Jumlah Data tidak valid")
            rumus_pajakmobil()
        for i in range(jml4):
            pkb_mobil = int(input('Masukkan Nominal PKB> Rp. '))
            if pkb_mobil < 0:
                input('PKB Mobil Tidak valid')
                rumus_pajakmobil()
            tahun_kepemilikan_mobil = int(input('Masukkan Lama Tahun Kepemilikan Kendaraan> '))
            if tahun_kepemilikan_mobil < 0:
                input('Tahun Kepemilikan Harus Bernilai Positif')
                rumus_pajakmobil()
            swdkllj_mobil = 143000
            administrasi_mobil = 200000
            tnkb_mobil = 100000 
            if tahun_kepemilikan_mobil % 5 == 0:
                pajak_mobil = pkb_mobil + swdkllj_mobil + administrasi_mobil + tnkb_mobil
            else:
                pajak_mobil = pkb_mobil + swdkllj_mobil + administrasi_mobil

            print("Data ke-", i+1)
            print(f'Pajak mobil> {pajak_mobil:,}')
            print('='*30)
            update_pjkmbl = {
                'PKB                    > Rp.': pkb_mobil,
                'Lama Tahun Kepemilikan > ': tahun_kepemilikan_mobil,
                'Pajak Mobil            > Rp.': pajak_mobil
            }
            semua_pajak_mobil[len(semua_pajak_mobil)+1]=update_pjkmbl
        input('Tekan Enter Kembali')
        if username_sekarang[0] in nama_user:
            menuMember1()
        else:
            menu_admin()
        
    except ValueError:
        input('Inputan Harus Angka, Ulangi !')
        if username_sekarang[0] in nama_user:
            menuMember1()
        else:
            menu_admin()


def update_pbb():
    hapus()
    data_pbb()
    ubah1 = int(input("Pilih data yang ingin di ubah : "))
    if 0 < ubah1 <= len(pbb):
        luas_tanah = int(input('\nMasukkan Luas tanah (/m)> '))
        if luas_tanah < 0:
            input('Ukuran Luas tanah Tidak valid')
            update_pbb()
        harga1 = int(input('Harga tanah> Rp. '))
        if harga1 < 0:
                input('Harga tanah Tidak valid')
                update_pbb()
        tanah = luas_tanah*harga1

        luas_bangunan = int(input('Masukkan Luas Bangunan> '))
        if luas_bangunan < 0:
            input('Ukuran Luas Bangunan Tidak valid')
            update_pbb()
        harga2 = int(input('Harga Bangunan> Rp. '))
        if harga2 < 0:
                input('Harga bangunan Tidak valid')
                update_pbb()
        bangunan = luas_bangunan*harga2
        njop = tanah + bangunan

        if njop <= 1000000000:
                njkp = 0.1/100 * njop
        elif njop > 1000000000 and njop <= 2000000000:
                njkp = 0.2/100 * njop
        elif njop > 2000000000:
                njkp = 0.3/100 * njop
        
        print(f'''
<1> Total Harga Tanah       > Rp.{tanah:,}
<2> Total Harga Bangunan    > Rp.{bangunan:,}
<3> NJOP                    > Rp.{njop:,}
<4> Total Tagihan PBB adalah> Rp.{njkp:,}''')
        print('='*30)
        
        add1 = {'Luas tanah     > ': luas_tanah,
                'Luas bangunan  > ': luas_bangunan,
                'Pajak          > Rp.': njkp
        }

        pbb.update({ubah1:add1})
        input("Data berhasil diubah !")
        menu_admin()
    else:
        input('Pajak Tidak ada didalam list')
        update_pbb()

def update_gaji():
    hapus()
    data_gaji()
    ubah2 = int(input("Pilih data yang ingin di ubah : "))
    if 0 < ubah2 <= len(gaji):
        gajibersih = float(input('Masukkan Gaji Bersih Bulanan> Rp.'))
        if gajibersih <= 0:
            input('Gaji harus Bernilai Positif')
            update_gaji()
        gaji_per_tahun = gajibersih*12
        print(f'''
    gaji pertahun adalah Rp.{gaji_per_tahun:,}
    ''')
        if gaji_per_tahun <= 54000000:
            print('Anda tidak wajib membayar pajak')
            input('Tekan Enter Untuk kembali')
            if username_sekarang[0] in nama_user:
                menuMember1()
            else:
                menu_admin()
            
        print('''
    ====Penghasilan Tidak Kena Pajak====
    1. Pribadi
    2. Menikah
    3. Menikah, 1 anak
    4. Menikah, 2 anak
    5. Menikah, 3 anak atau lebih
    =====================================
    ''')
        ptkp = int(input('Masukkan Pilihan Sesuai Data Anda> '))
        if ptkp == 1:
            pkp = gaji_per_tahun - 54000000
        elif ptkp == 2:
            pkp = gaji_per_tahun - (54000000+ 4500000)
        elif ptkp == 3:
            pkp = gaji_per_tahun - (54000000 + 4500000 + 4500000)
        elif ptkp == 4:
            pkp = gaji_per_tahun - (54000000 + 4500000 + 4500000 + 4500000)
        elif ptkp == 5:
            pkp = gaji_per_tahun - (54000000 + 4500000 + 4500000 + 4500000 + 4500000)
        else:
            input('Inputan anda salah !, Silahkan Ulangi')
            update_gaji()
            
        print(f'''
    Penghasilan kena pajak Rp.{pkp:,}
    ''')

        if pkp >=0 and pkp <= 50000000:
            pph = pkp * (5/100)
        elif pkp > 50000000 and pkp <= 250000000:
            pph1 = 50000000 * (5/100)
            pph2 = (pkp-50000000) * (15/100)
            pph = pph1 + pph2
        elif pkp > 250000000 and pkp <= 500000000:
            pph1 = 50000000 * (5/100)
            pph2 = 250000000 * (15/100)
            pph3 = (pkp-50000000-250000000) * (25/100)
            pph = pph1 + pph2 + pph3
        elif pkp > 500000000:
            pph1 = 50000000 * (5/100)
            pph2 = 250000000 * (15/100)
            pph3 = 500000000 * (25/100)
            pph4 = (pkp-50000000-250000000-500000000) * (30/100)
            pph = pph1 + pph2 + pph3 + pph4
        else:
            print('Anda tidak wajib membayar pajak')
            input('Tekan Enter Kembali')
            menu_admin()
            
        print(f'''
            gaji pertahun adalah           > Rp. {gaji_per_tahun:,}
            Penghasilan kena pajak         > Rp. {pkp:,}
            Pajak Yang Harus Dibayar adalah> Rp. {pph:,}
            ''')
        add2 = {
                'Gaji /Tahun> Rp.': gaji_per_tahun,
                'PKP        > Rp.': pkp,
                'PPH        > Rp.': pph
            }
        gaji.update({ubah2:add2})
        input("Data berhasil diubah !")
        menu_admin()
    else:
        input('Pajak Tidak ada didalam list')
        update_gaji()
        
def update_pajakmotor():
    hapus()
    data_pajakmotor()
    ubah3 = int(input("Pilih data yang ingin di ubah : "))
    if 0 < ubah3 <= len(semua_pajak_motor):
        pkb_motor = int(input('Masukkan Nominal PKB> Rp.'))
        if pkb_motor < 0:
            input('PKB Motor Tidak valid')
            rumus_pajakmobil()
        tahun_kepemilikan_motor = int(input('Masukkan Lama Tahun Kepemilikan Kendaraan> '))
        if tahun_kepemilikan_motor < 0:
                input('Tahun Kepemilikan Harus Bernilai Positif')
                update_pajakmotor()
        swdkllj_motor = 35000 
        administrasi_motor = 100000 
        tnkb_motor = 60000 
        if tahun_kepemilikan_motor % 5 == 0:
            pajak_motor = pkb_motor + swdkllj_motor + administrasi_motor + tnkb_motor
        else:
            pajak_motor = pkb_motor + swdkllj_motor + administrasi_motor
        
        print(f'''Pajak motor> Rp.{pajak_motor:,}''')

        add3 = {
                'PKB                    > Rp.': pkb_motor,
                'Lama Tahun Kepemilikan > ': tahun_kepemilikan_motor,
                'Pajak Motor            > Rp.': pajak_motor
            }
        semua_pajak_motor.update({ubah3:add3})
        input('Pajak Telah Di Update, tekan enter untuk')
        menu_admin()
    else:
        input('Pajak Tidak ada didalam list')
        update_pajakmotor()

def update_pajakmobil():
    hapus()
    data_pajakmobil()
    ubah4 = int(input("Pilih data yang ingin di ubah : "))
    if 0 < ubah4 <= len(semua_pajak_mobil):
        pkb_mobil = int(input('Masukkan Nominal PKB> Rp.'))
        if pkb_mobil < 0:
            input('PKB Mobil Tidak valid')
            rumus_pajakmobil()
        tahun_kepemilikan_mobil = int(input('Masukkan Lama Tahun Kepemilikan Kendaraan> '))
        if tahun_kepemilikan_mobil < 0:
                input('Tahun Kepemilikan Harus Bernilai Positif')
                update_pajakmobil()
        swdkllj_mobil = 143000
        administrasi_mobil = 200000
        tnkb_mobil = 100000 
        if tahun_kepemilikan_mobil % 5 == 0:
            pajak_mobil = pkb_mobil + swdkllj_mobil + administrasi_mobil + tnkb_mobil
        else:
            pajak_mobil = pkb_mobil + swdkllj_mobil + administrasi_mobil

        print(f'Pajak mobil> Rp.{pajak_mobil:,}')

        add4 = {
                'PKB                    > Rp.': pkb_mobil,
                'Lama Tahun Kepemilikan > ': tahun_kepemilikan_mobil,
                'Pajak Mobil            > Rp.': pajak_mobil
            }
        semua_pajak_mobil.update({ubah4:add4})
        input('Pajak Telah Di Update, tekan enter untuk kembali !')
        menu_admin()
    else:
        input('Pajak Tidak ada didalam list')
        update_pajakmobil()


def login():
    while True:
    # login
        hapus()
        print('''
    =====MENU LOGIN=====
    1. ADMIN
    2. USER
    3. BUAT AKUN
    4. EXIT
    ====================
    ''')
        log = input('Login sebagai: ')
        if log == '1':
            username_admin = input('Username: ')
            password_admin = input('password: ')
            if username_admin == admin['user'] and password_admin == admin['pass']:
                username_sekarang.append(username_admin)
                print()
                print('Checking . . . . .')
                time.sleep(2)
                menu_admin()
                
            else:
                print()
                print('Checking . . . . .')
                time.sleep(2)
                print('\nUsername atau Password salah')
                input('Tekan Enter untuk kembali !')
                login()
                
        elif log == '2':
            username_user = input('Username: ')
            password_user = input('password: ')
            for z in range(len(nama_user)):
                        if nama_user[z] == username_user and pass_user[z] == password_user:
                            username_sekarang.append(username_user)
                            print()
                            print('Checking . . . . .')
                            time.sleep(2)
                            menuMember1()
                        elif username_user == '' and password_user == '':
                            print()
                            print('Checking . . . . .')
                            time.sleep(2)
                            input('\nAkun belum terdaftar, Silahkan Registrasi!')
                            login()
                        
            print()
            print('Checking . . . . .')
            time.sleep(2)
            print('\nUsername atau Password salah')
            input('Tekan Enter untuk kembali !')
            login()
        
        elif log == '4':
            hapus()
            print('|------------------------------------------------------------|')
            print('|=== Terima kasih Telah menggunakan Aplikasi Pajak Ceria === |')
            print('|------------------------------------------------------------|')
            time.sleep(2)
            hapus()
            exit()

        elif log == '3':
            register()
            
        elif log  == '':
            print('\nUsername atau Password salah')
            input('Tekan Enter untuk kembali !')
            login()

        else:
            input('Pilihan salah, Ulangi !')

def register():
    user_baru = input('masukkan username baru> ')
    pass_baru = input('masukkan password baru> ')
    if user_baru in nama_user:
        input('Username sudah terdaftar')
        login()
    elif user_baru == '' and pass_baru == '':
        input('\nNama dan Password tidak Valid!')
        login()
    else:
        nama_user.append(user_baru)
        pass_user.append(pass_baru)
        input("\nAkun Berhasil Dibuat")
        login()

def menu_admin():
    hapus()
    while True:
        print('''===========================
         Menu Admin
===========================
<1> Lihat Pajak Yang ada
<2> Tambah Pajak
<3> Hapus Pajak
<4> Ubah Data Pajak
<0> Keluar   
===========================''')
        pilih = input('Pilih Menu> ')
        hapus()
        if pilih == '1':
            print('''=======================
       Menu Pajak
=======================
[1] Pajak Pbb
[2] Pajak gaji
[3] Pajak Motor
[4] Pajak Mobil
[5] Kembali
=======================''')
            pilih1 = input('Pilih Menu> ')
            if pilih1 == '1':
                data_pbb()
                input('Tekan Enter untuk kembali ke menu Admin !')
                menu_admin()
            
            elif pilih1 == '2':
                data_gaji()
                input('Tekan Enter untuk kembali ke menu Admin !')
                menu_admin()

            elif pilih1 == '3':
                data_pajakmotor()
                input('Tekan Enter untuk kembali ke menu Admin !')
                menu_admin()

            elif pilih1 == '4':
                data_pajakmobil()
                input('Tekan Enter untuk kembali ke menu Admin !')
                menu_admin()

            elif pilih1 == '5':
                menu_admin()
            else:
                input('Inputan salah Mohon Ulangi !')
                menu_admin()

        elif pilih == '2':
            print('''=======================
      Tambah Pajak
=======================
[1] Pajak Pbb
[2] Pajak gaji
[3] Pajak Motor
[4] Pajak Mobil
[5] Kembali
=======================''')
            
            menupajak = input('Pilihan anda> ')
            if menupajak == '1':
                rumus_pbb()

            elif menupajak == '2':
                rumus_gaji()
                    

            elif menupajak == '3':
                rumus_pajakmotor()


            elif menupajak == '4':
                rumus_pajakmobil()

            elif menupajak == '5':
                menu_admin()
            
            else:
                input('Inputan salah Mohon Ulangi !')
                menu_admin()
            

        elif pilih == '3':
            print('''=======================
      Hapus Pajak
=======================
[1] Pajak Pbb
[2] Pajak gaji
[3] Pajak Motor
[4] Pajak Mobil
[5] Kembali
=======================''')
            pilih2 = input('Pilihan Menghapus> ')
            if pilih2 == '1':
                try:
                    data_pbb()
                    no = int(input('Masukkan data pajak yang ingin dihapus> '))
                    if 0 < no <= len(pbb):
                        while 0 < no < len(pbb):
                            datacopy = no+1
                            pbb.update({no : pbb[datacopy]})
                            no+=1
                        del pbb[no]
                        input("Data Pajak berhasil di hapus")
                        menu_admin()
                    else:
                        input('Data Kosong / Tidak Ada')
                        menu_admin()
                except ValueError:
                    input('Data Kosong / Tidak Ada')
                    menu_admin()

            elif pilih2 == '2':
                try:
                    data_gaji()
                    no = int(input('Masukkan data pajak yang ingin dihapus> '))
                    if 0 < no <= len(gaji):
                        while 0 < no < len(gaji):
                            datacopy = no+1
                            gaji.update({no : gaji[datacopy]})
                            no+=1
                        del gaji[no]
                        input("Data Pajak berhasil di hapus")
                        menu_admin()
                    else:
                        input('Data Kosong / Tidak Ada')
                        menu_admin()   
                except ValueError:
                    input('Data Kosong / Tidak Ada')
                    menu_admin()
            
            elif pilih2 == '3':
                data_pajakmotor()
                no = int(input('Masukkan data pajak yang ingin dihapus> '))
                try:
                    if 0 < no <= len(semua_pajak_motor):
                        while 0 < no < len(semua_pajak_motor):
                            datacopy = no+1
                            semua_pajak_motor.update({no : semua_pajak_motor[datacopy]})
                            no+=1
                        del semua_pajak_motor[no]
                        input("Data Pajak berhasil di hapus")
                        menu_admin()
                    else:
                        input('Data Kosong / Tidak Ada')
                        menu_admin()

                except ValueError:
                    input('Data Kosong / Tidak Ada')
                    menu_admin()

            elif pilih2 == '4':
                data_pajakmobil()
                no = int(input('Masukkan data pajak yang ingin dihapus> '))
                try:
                    if 0 < no <= len(semua_pajak_mobil):
                        while 0 < no < len(semua_pajak_mobil):
                            datacopy = no+1
                            semua_pajak_mobil.update({no : semua_pajak_mobil[datacopy]})
                            no+=1
                        del semua_pajak_mobil[no]
                        input("Data Pajak berhasil di hapus")
                        menu_admin()
                    else:
                        input('Data Kosong / Tidak Ada')
                        menu_admin()

                except ValueError:
                    input('Data Kosong / Tidak Ada')
                    menu_admin()
                    
            elif pilih2 == '5':
                input('Tekan Enter untuk kembalik ke Menu Admin')
                menu_admin()
            else:
                input('Inputan salah Mohon Ulangi !')
                menu_admin()

        
        elif pilih == '4':
            print('''=======================
     Update Pajak
=======================
[1] Pajak Pbb
[2] Pajak gaji
[3] Pajak Motor
[4] Pajak Mobil
[5] Kembali
=======================''')
            pilihan1 = input('Update Pajak ke> ')
            if pilihan1 == '1':
                update_pbb()

            elif pilihan1 == '2':
                update_gaji()
            
            elif pilihan1 == '3':
                update_pajakmotor()

            elif pilihan1 == '4':
                update_pajakmobil()
            
            elif pilihan1 == '5':
                menu_admin()
            
            else:
                input('Inputan salah Mohon Ulangi !')
                menu_admin()
        
        elif pilih == '0':
            print('=== Terima kasih Telah menggunakan Aplikasi Pajak Ceria ===')
            username_sekarang.pop()
            login()
        
        else:
            input('Pilhan salah, Ulangi !')
            menu_admin()


def menuMember1():
    hapus()
    while True:
        print('''
=======================
  Aplikasi Pajak Ceria
=======================
[1] Hitung Pajak
[0] Logout
=======================''')
        menuuser = input('Pilihan anda> ')
        if menuuser == '1':
            hapus()
            print('''
    =======================
        Pilihan Pajak
    =======================
    [1] Pajak Pbb
    [2] Pajak gaji
    [3] Pajak Motor
    [4] Pajak Mobil
    [5] Kembali
    =======================''')
                    
            menupajak = input('Pilihan anda> ')
            if menupajak == '1':
                hapus()
                rumus_pbb()

            elif menupajak == '2':
                hapus()
                rumus_gaji()   

            elif menupajak == '3':
                hapus()
                rumus_pajakmotor()

            elif menupajak == '4':
                hapus()
                rumus_pajakmobil()

            elif menupajak == '5':
                hapus()
                menuMember1()     
            
            else:
                input('Inputan salah Mohon Ulangi !')
                menuMember1()
        elif menuuser  == '0':
            hapus()
            print('Loading...')
            time.sleep(1)
            username_sekarang.pop()
            hapus()
            login()
        else:
            input("Inputan anda salah")
            menuMember1()
login()
