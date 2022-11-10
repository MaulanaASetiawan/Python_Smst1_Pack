import os
import time
def hapus():
  os.system('cls')
# Tampilan menu
def menu():
  hapus()
  print('''
  ■■■■■■■     |===========================|
 ■       ■    |     Konversi Celcius      |
■   ■  ■  ■   |===========================|
■         ■   | <1> Celcius to Reamur     |
■         ■   | <2> Celcius to Fahrenheit |
■■■■■■■■■■■   | <3> Celcius to Kelvin     |
║ ║ ║ ║ ║ ║   | <4> Exit                  |
║ ║ ║ ║ ║ ║   |===========================|
║ ║ ║ ║ ║
║ ║ ║
║
\n''')
selected_menu = str(input('Pilih Menu> '))
if selected_menu == '1':
  Reamur()
elif selected_menu == '2':
  Fahrenheit()
elif selected_menu == '3':
  Kelvin()
elif selected_menu == '4':
  keluar()
else:
  input('Inputan anda salah mohon ulangi kembali!')
  menu()

# definisi sekaligus operasi pengkonversian
def Reamur():
  try:
  suhu = float(input('Masukkan Celcius> '))
  konversi = 4/5*suhu
  print(f'Hasil konversi {suhu}°C adalah {konversi:g}°R!')
  kembali_ke_menu()
  except:
  input('Error! , Inputan harus Angka\n')
  Reamur()
  
def Fahrenheit():
  try:
  suhu = float(input('Masukkan Celcius> '))
  konversi = (9/5*suhu)+32
  print(f'Hasil konversi {suhu}°C adalah {konversi:g}°F!')
  kembali_ke_menu()
  except:
  input('Error! , Inputan harus Angka\n')
  Fahrenheit()
  
def Kelvin():
  try:
  suhu = float(input('Masukkan Celcius> '))
  konversi = suhu + 273
  print(f'Hasil konversi {suhu}°C adalah {konversi:g}°K!')
  kembali_ke_menu()
  except:
  input('Error! , Inputan harus Angka\n')
  Kelvin()

def kembali_ke_menu():
  print('\n')
  input('Tekan enter untuk kembali!')
  menu()

def keluar():
  hapus()
  print('''
  ■■■■■■■
 ■       ■
■   ■  ■  ■ Terima Kasih
■         ■ And
■         ■ See you next time
■■■■■■■■■■■
║ ║ ║ ║ ║ ║
║ ║ ║ ║ ║ ║
║ ║ ║ ║ ║
║ ║ ║
║
''')
  time.sleep(3)
  hapus()
 menu()
