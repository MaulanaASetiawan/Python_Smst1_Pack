import os
import time
def hapus():
  os.system('cls')
data = {
  'NIM': '',
  'Nama': '',
  'Prodi': '',
  'Umur' : '',
  'Tinggi': ''
}
def isi():
  hapus()
  print('Silahkan Input data anda terlebih dahulu\n')
  try:
    data['NIM'] = int(input('Input NIM anda> '))
    data['Nama'] = str(input('Input Nama anda> '))
    data['Prodi'] = str(input('Input Prodi anda> '))
    data['Umur'] = int(input('Input Umur anda> '))
    data['Tinggi'] = float(input('Input Tinggi badan anda (m)> '))
  except:
    input('Inputan anda salah, tekan ENTER untuk mengulang')
    isi()
  while True:
    print('\n')
    print('Hasil, Ubah, Keluar?>> ')
    next = str(input('Pilihan>> '))
    if next == 'Hasil' or next == 'hasil':
      hapus()
      hasil()
      time.sleep(1)
    elif next == 'Ubah' or next == 'ubah':
      hapus()
      main = input('Input Kunci> ')
      perbarui = input('Input Pembaruan> ')
      data[main] = perbarui
      time.sleep(1)

    elif next == 'Keluar' or next == 'keluar':
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
      exit()
    else:
      input('Pilihan salah!')

def hasil():
  print(f'''
    ■■■■■■■       ==================================
   ■       ■                Biodata Anda
  ■   ■  ■  ■     ==================================
  ■         ■      NIM > {data['NIM']}
  ■         ■      Nama > {data['Nama']}
  ■■■■■■■■■■■      Prodi > {data['Prodi']}
  ║ ║ ║ ║ ║ ║      Umur > {data['Umur']} Tahun
  ║ ║ ║ ║ ║ ║      Tinggi > {data['Tinggi']} meter
  ║ ║ ║ ║ ║       ==================================
  ║ ║ ║
  ║
  \n
  ''')
isi()
