import os
import time

# Def hapus untuk membersihkan Layar terminal
def hapus():
    os.system('cls')

# Def menu untuk menampilkan Menu satuan
def menu():
    hapus()
    print('''
────▓▓▓▓▓▓──────        |========================|
───▓▄▓▓▓▓▓▓─────        |     Satuan Panjang     |
──────▓▓▓▓▓─▒▒──        |========================|
─▓▓▓▓▓▓▓▓▓──▒▒▒─        | [1] Kilometer          |
▓▓▓▓▓──────▒▒▒▒▒        | [2] Hektometer         |
─▓▓▓──▒▒▒▒▒▒▒▒▒─        | [3] Dekameter          |
──▓▓─▒▒▒▒▒──────        | [4] Meter              |
─────▒▒▒▒▒▒▀▒───        | [5] Desimeter          |
──────▒▒▒▒▒▒────        | [6] Centimeter         |
                        | [7] Milimeter          |
                        | [0] Keluar             |
                        |========================|''')
    menu = str(input('Pilih Menu satuan> '))
    if menu == '1':
        km()
    elif menu == '2':
        hm()
    elif menu == '3':
        dam()
    elif menu == '4':
        m()
    elif menu == '5':
        dm()
    elif menu == '6':
        cm()
    elif menu == '7':
        mm()
    elif menu == '0':
        keluar()
    else:
        menu_kembali()

# Def km,hm,dam,m,dm,cm,mm adalah tempat untuk menjalankan langkah
# Pengkonverian satuan panjang yang telah di-inputkan

def km():
    try:
        a = float(input('Masukkan Angka> '))
    except:
        input('Inputan harus angka, Tekan Enter Untuk kembali !')
        km()
    
    while True:
        print('''
────▓▓▓▓▓▓──────        |========================|
───▓▄▓▓▓▓▓▓─────        |        Konversi        |
──────▓▓▓▓▓─▒▒──        |========================|
─▓▓▓▓▓▓▓▓▓──▒▒▒─        | [1] Ke Hektometer      |
▓▓▓▓▓──────▒▒▒▒▒        | [2] Ke Dekameter       |
─▓▓▓──▒▒▒▒▒▒▒▒▒─        | [3] Ke Meter           |
──▓▓─▒▒▒▒▒──────        | [4] Ke Desimeter       |
─────▒▒▒▒▒▒▀▒───        | [5] Ke Centimeter      |
──────▒▒▒▒▒▒────        | [6] Ke Milimeter       |
                        |========================|''')
        pilih = str(input('Pilihan> '))
        if pilih == '1':
            try:
                hasil = a*10.0
                print(f'hasil konversinya adalah {hasil} hm')
                kembali()
            except:
                input('Inputan harus angka !')
                km()
        elif pilih == '2':
            try:
                hasil = a*100
                print(f'hasil Konversinya adalah {hasil} dam')
                kembali()
            except:
                input('Inputan Harus angka!')
                km()
        elif pilih == '3':
            try:
                hasil = a*1000
                print(f'hasil Konversinya adalah {hasil} m')
                kembali()
            except:
                input('Inputan Harus angka!')
                km()
        elif pilih == '4':
            try:
                hasil = a*10000
                print(f'hasil Konversinya adalah {hasil} dm')
                kembali()
            except:
                input('Inputan Harus angka!')
                km()
        elif pilih == '5':
            try:
                hasil = a*100000
                print(f'hasil Konversinya adalah {hasil} cm')
                kembali()
            except:
                input('Inputan Harus angka!')
                km()
        elif pilih == '6':
            try:
                hasil = a*1000000
                print(f'hasil Konversinya adalah {hasil} mm')
                kembali()
            except:
                input('Inputan Harus angka!')
                km()
        else:
            input('Salah gan :))')
            km()

def hm():
    try:
        a = float(input('Masukkan Angka> '))
    except:
        input('Inputan harus angka, Tekan Enter Untuk kembali !')
        hm()
    
    while True:
        print('''
────▓▓▓▓▓▓──────        |========================|
───▓▄▓▓▓▓▓▓─────        |        Konversi        |
──────▓▓▓▓▓─▒▒──        |========================|
─▓▓▓▓▓▓▓▓▓──▒▒▒─        | [1] Ke Kilometer       |
▓▓▓▓▓──────▒▒▒▒▒        | [2] Ke Dekameter       |
─▓▓▓──▒▒▒▒▒▒▒▒▒─        | [3] Ke Meter           |
──▓▓─▒▒▒▒▒──────        | [4] Ke Desimeter       |
─────▒▒▒▒▒▒▀▒───        | [5] Ke Centimeter      |
──────▒▒▒▒▒▒────        | [6] Ke Milimeter       |
                        |========================|''')
        pilih = str(input('Pilihan> '))
        if pilih == '1':
            try:
                hasil = a/10
                print(f'hasil konversinya adalah {hasil} km')
                kembali()
            except:
                input('Inputan harus angka !')
                hm()
        elif pilih == '2':
            try:
                hasil = a*10
                print(f'hasil Konversinya adalah {hasil} dam')
                kembali()
            except:
                input('Inputan Harus angka!')
                hm()
        elif pilih == '3':
            try:
                hasil = a*100
                print(f'hasil Konversinya adalah {hasil} m')
                kembali()
            except:
                input('Inputan Harus angka!')
                hm()
        elif pilih == '4':
            try:
                hasil = a*1000
                print(f'hasil Konversinya adalah {hasil} dm')
                kembali()
            except:
                input('Inputan Harus angka!')
                hm()
        elif pilih == '5':
            try:
                hasil = a*10000
                print(f'hasil Konversinya adalah {hasil} cm')
                kembali()
            except:
                input('Inputan Harus angka!')
                hm()
        elif pilih == '6':
            try:
                hasil = a*100000
                print(f'hasil Konversinya adalah {hasil} mm')
                kembali()
            except:
                input('Inputan Harus angka!')
                hm()
        else:
            input('Salah gan :))')
            hm()

def dam():
    try:
        a = float(input('Masukkan Angka> '))
    except:
        input('Inputan harus angka, Tekan Enter Untuk kembali !')
        dam()
    
    while True:
        print('''
────▓▓▓▓▓▓──────        |========================|
───▓▄▓▓▓▓▓▓─────        |        Konversi        |
──────▓▓▓▓▓─▒▒──        |========================|
─▓▓▓▓▓▓▓▓▓──▒▒▒─        | [1] Ke Kilometer       |
▓▓▓▓▓──────▒▒▒▒▒        | [2] Ke Hektometer      |
─▓▓▓──▒▒▒▒▒▒▒▒▒─        | [3] Ke Meter           |
──▓▓─▒▒▒▒▒──────        | [4] Ke Desimeter       |
─────▒▒▒▒▒▒▀▒───        | [5] Ke Centimeter      |
──────▒▒▒▒▒▒────        | [6] Ke Milimeter       |
                        |========================|''')
        pilih = str(input('Pilihan> '))
        if pilih == '1':
            try:
                hasil = a/100
                print(f'hasil konversinya adalah {hasil} km')
                kembali()
            except:
                input('Inputan harus angka !')
                dam()
        elif pilih == '2':
            try:
                hasil = a/10
                print(f'hasil Konversinya adalah {hasil} hm')
                kembali()
            except:
                input('Inputan Harus angka!')
                dam()
        elif pilih == '3':
            try:
                hasil = a*10
                print(f'hasil Konversinya adalah {hasil} m')
                kembali()
            except:
                input('Inputan Harus angka!')
                dam()
        elif pilih == '4':
            try:
                hasil = a*100
                print(f'hasil Konversinya adalah {hasil} dm')
                kembali()
            except:
                input('Inputan Harus angka!')
                dam()
        elif pilih == '5':
            try:
                hasil = a*1000
                print(f'hasil Konversinya adalah {hasil} cm')
                kembali()
            except:
                input('Inputan Harus angka!')
                dam()
        elif pilih == '6':
            try:
                hasil = a*10000
                print(f'hasil Konversinya adalah {hasil} mm')
                kembali()
            except:
                input('Inputan Harus angka!')
                dam()
        else:
            input('Salah gan :))')
            dam()

def m():
    try:
        a = float(input('Masukkan Angka> '))
    except:
        input('Inputan harus angka, Tekan Enter Untuk kembali !')
        m()
    
    while True:
        print('''
────▓▓▓▓▓▓──────        |========================|
───▓▄▓▓▓▓▓▓─────        |        Konversi        |
──────▓▓▓▓▓─▒▒──        |========================|
─▓▓▓▓▓▓▓▓▓──▒▒▒─        | [1] Ke Kilometer       |
▓▓▓▓▓──────▒▒▒▒▒        | [2] Ke Hektometer      |
─▓▓▓──▒▒▒▒▒▒▒▒▒─        | [3] Ke Dekameter       |
──▓▓─▒▒▒▒▒──────        | [4] Ke Desimeter       |
─────▒▒▒▒▒▒▀▒───        | [5] Ke Centimeter      |
──────▒▒▒▒▒▒────        | [6] Ke Milimeter       |
                        |========================|''')
        pilih = str(input('Pilihan> '))
        if pilih == '1':
            try:
                hasil = a/1000
                print(f'hasil konversinya adalah {hasil} km')
                kembali()
            except:
                input('Inputan harus angka !')
                m()
        elif pilih == '2':
            try:
                hasil = a/100
                print(f'hasil Konversinya adalah {hasil} hm')
                kembali()
            except:
                input('Inputan Harus angka!')
                m()
        elif pilih == '3':
            try:
                hasil = a/10
                print(f'hasil Konversinya adalah {hasil} dam')
                kembali()
            except:
                input('Inputan Harus angka!')
                m()
        elif pilih == '4':
            try:
                hasil = a*10
                print(f'hasil Konversinya adalah {hasil} dm')
                kembali()
            except:
                input('Inputan Harus angka!')
                m()
        elif pilih == '5':
            try:
                hasil = a*100
                print(f'hasil Konversinya adalah {hasil} cm')
                kembali()
            except:
                input('Inputan Harus angka!')
                m()
        elif pilih == '6':
            try:
                hasil = a*1000
                print(f'hasil Konversinya adalah {hasil} mm')
                kembali()
            except:
                input('Inputan Harus angka!')
                m()
        else:
            input('Salah gan :))')
            m()
def dm():
    try:
        a = float(input('Masukkan Angka> '))
    except:
        input('Inputan harus angka, Tekan Enter Untuk kembali !')
        dm()
    
    while True:
        print('''
────▓▓▓▓▓▓──────        |========================|
───▓▄▓▓▓▓▓▓─────        |        Konversi        |
──────▓▓▓▓▓─▒▒──        |========================|
─▓▓▓▓▓▓▓▓▓──▒▒▒─        | [1] Ke Kilometer       |
▓▓▓▓▓──────▒▒▒▒▒        | [2] Ke Hektometer      |
─▓▓▓──▒▒▒▒▒▒▒▒▒─        | [3] Ke Dekameter       |
──▓▓─▒▒▒▒▒──────        | [4] Ke Meter           |
─────▒▒▒▒▒▒▀▒───        | [5] Ke Centimeter      |
──────▒▒▒▒▒▒────        | [6] Ke Milimeter       |
                        |========================|''')
        pilih = str(input('Pilihan> '))
        if pilih == '1':
            try:
                hasil = a/1000
                print(f'hasil konversinya adalah {hasil} km')
                kembali()
            except:
                input('Inputan harus angka !')
                dm()
        elif pilih == '2':
            try:
                hasil = a/1000
                print(f'hasil Konversinya adalah {hasil} hm')
                kembali()
            except:
                input('Inputan Harus angka!')
                dm()
        elif pilih == '3':
            try:
                hasil = a/100
                print(f'hasil Konversinya adalah {hasil} dam')
                kembali()
            except:
                input('Inputan Harus angka!')
                dm()
        elif pilih == '4':
            try:
                hasil = a/10
                print(f'hasil Konversinya adalah {hasil} m')
                kembali()
            except:
                input('Inputan Harus angka!')
                dm()
        elif pilih == '5':
            try:
                hasil = a*10
                print(f'hasil Konversinya adalah {hasil} cm')
                kembali()
            except:
                input('Inputan Harus angka!')
                dm()
        elif pilih == '6':
            try:
                hasil = a*100
                print(f'hasil Konversinya adalah {hasil} mm')
                kembali()
            except:
                input('Inputan Harus angka!')
                dm()
        else:
            input('Salah gan :))')
            dm()
def cm():
    try:
        a = float(input('Masukkan Angka> '))
    except:
        input('Inputan harus angka, Tekan Enter Untuk kembali !')
        cm()
    
    while True:
        print('''
────▓▓▓▓▓▓──────        |========================|
───▓▄▓▓▓▓▓▓─────        |        Konversi        |
──────▓▓▓▓▓─▒▒──        |========================|
─▓▓▓▓▓▓▓▓▓──▒▒▒─        | [1] Ke Kilometer       |
▓▓▓▓▓──────▒▒▒▒▒        | [2] Ke Hektometer      |
─▓▓▓──▒▒▒▒▒▒▒▒▒─        | [3] Ke Dekameter       |
──▓▓─▒▒▒▒▒──────        | [4] Ke Meter           |
─────▒▒▒▒▒▒▀▒───        | [5] Ke Desimeter       |
──────▒▒▒▒▒▒────        | [6] Ke Milimeter       |
                        |========================|''')
        pilih = str(input('Pilihan> '))
        if pilih == '1':
            try:
                hasil = a/100000
                print(f'hasil konversinya adalah {hasil} km')
                kembali()
            except:
                input('Inputan harus angka !')
                cm()
        elif pilih == '2':
            try:
                hasil = a/10000
                print(f'hasil Konversinya adalah {hasil} hm')
                kembali()
            except:
                input('Inputan Harus angka!')
                cm()
        elif pilih == '3':
            try:
                hasil = a/1000
                print(f'hasil Konversinya adalah {hasil} dam')
                kembali()
            except:
                input('Inputan Harus angka!')
                cm()
        elif pilih == '4':
            try:
                hasil = a/100
                print(f'hasil Konversinya adalah {hasil} m')
                kembali()
            except:
                input('Inputan Harus angka!')
                cm()
        elif pilih == '5':
            try:
                hasil = a/10
                print(f'hasil Konversinya adalah {hasil} dm')
                kembali()
            except:
                input('Inputan Harus angka!')
                cm()
        elif pilih == '6':
            try:
                hasil = a*10
                print(f'hasil Konversinya adalah {hasil} mm')
                kembali()
            except:
                input('Inputan Harus angka!')
                cm()
        else:
            input('Salah gan :))')
            cm()

def mm():
    try:
        a = float(input('Masukkan Angka> '))
    except:
        input('Inputan harus angka, Tekan Enter Untuk kembali !')
        mm()
    
    while True:
        print('''
────▓▓▓▓▓▓──────        |========================|
───▓▄▓▓▓▓▓▓─────        |        Konversi        |
──────▓▓▓▓▓─▒▒──        |========================|
─▓▓▓▓▓▓▓▓▓──▒▒▒─        | [1] Ke Kilometer       |
▓▓▓▓▓──────▒▒▒▒▒        | [2] Ke Hektometer      |
─▓▓▓──▒▒▒▒▒▒▒▒▒─        | [3] Ke Dekameter       |
──▓▓─▒▒▒▒▒──────        | [4] Ke Meter           |
─────▒▒▒▒▒▒▀▒───        | [5] Ke Desimeter       |
──────▒▒▒▒▒▒────        | [6] Ke Centimeter      |
                        |========================|''')
        pilih = str(input('Pilihan> '))
        if pilih == '1':
            try:
                hasil = a/1000000
                print(f'hasil konversinya adalah {hasil} km')
                kembali()
            except:
                input('Inputan harus angka !')
                m()
        elif pilih == '2':
            try:
                hasil = a/100000
                print(f'hasil Konversinya adalah {hasil} hm')
                kembali()
            except:
                input('Inputan Harus angka!')
                m()
        elif pilih == '3':
            try:
                hasil = a/10000
                print(f'hasil Konversinya adalah {hasil} dam')
                kembali()
            except:
                input('Inputan Harus angka!')
                m()
        elif pilih == '4':
            try:
                hasil = a/1000
                print(f'hasil Konversinya adalah {hasil} m')
                kembali()
            except:
                input('Inputan Harus angka!')
                m()
        elif pilih == '5':
            try:
                hasil = a/100
                print(f'hasil Konversinya adalah {hasil} dm')
                kembali()
            except:
                input('Inputan Harus angka!')
                m()
        elif pilih == '6':
            try:
                hasil = a/10
                print(f'hasil Konversinya adalah {hasil} cm')
                kembali()
            except:
                input('Inputan Harus angka!')
                m()
        else:
            input('Salah gan :))')
            m()


# Def keluar untuk menampilkan tampilan keluar / berhenti dari program
def keluar():
    hapus()
    print("""
⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣩⣉⢻⣿⡇
⣿⣿⣿⠀⣿⣶⣕⣈⠹⠿⠿⠿⠿⠟⠛⣛⢋⣰⠣⣿⣿⠀⣿⣿
⣿⣿⣿⡀⣿⣿⣿⣧⢻⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠶⡝⠀⣿⣿
⣿⣿⣿⣷⠘⣿⣿⣿⢏⣿⣿⣋⣀⣈⣻⣿⣿⣷⣤⣤⣿⡐⢿⣿
⣿⣿⣿⣿⣆⢩⣝⣫⣾⣿⣿⣿⣿⡟⠿⠿⠦⠀⠸⠿⣻⣿⡄⢻           
⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⠇⣼    Dadah. . .
⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⣿
⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿⣿
⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿
⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿
⣿⣿⣿⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿⣿
⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿
⣿⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇ ⣿⡇""")
    time.sleep(3)
    exit()

# Def menu_kembali untuk kembali ke menu saat menginputkan pilihan yang salah
def menu_kembali():
    print('\n')
    input('Pilihan Anda salah, tekan Enter Untuk kembali ! ')
    menu()

# Def kembali untuk kembali ke def konversi satuan saat menginputkan pilihan yang salah
def kembali():
    print('\n')
    input('tekan enter untuk kembali')
    menu()

menu()
