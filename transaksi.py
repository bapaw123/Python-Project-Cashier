from tabulate import tabulate
import numpy as np

class Transaction:

    def __init__(self):
      # membuat list utama untuk menyimpan list data nama, jumlah, dan harga
      self.list_item = []

    def add_item(self):
      """
      Fungsi ini menanyakan data Nama Item, Jumlah Item, dan Harga Item yang
      akan dibentuk sebagai list dan dimasukkan ke dalam list utama (list_item) 
      dengan metode append. 
      
      Selain itu sekaligus membuat variabel 'nomor' untuk membuat urutan dari 
      data-data tersebut dan membentuk data total barang yang merupakan hasil
      kali dari Jumlah Item dengan Harga Item.
    
      Return-nya berbentuk list dalam list: 
      [['Tahu', 1 buah, Rp. 1.000, Rp. 1.000], [...], [...], ....]

      """
      # penggunaan looping while untuk mengulangi pengumpulan data
      while True:
        
        # input dari data-data yang dibutuhkan
        nama_item = input("Silakan Masukan Nama Barang: ").capitalize()
        jumlah_item = int(input("Silakan Masukan Jumlah Barang: "))
        harga_item = int(input("Silakan Masukan Harga Per Barang: "))
        
        nomor = len(self.list_item)+1
        
        # mengumpulkan data-data berbentuk ke dalam list_item
        self.list_item.append([nomor,
                              nama_item,
                              f'{jumlah_item} buah',
                              f'Rp. {harga_item:,}',
                              f'Rp. {jumlah_item*harga_item:,}'])
        
       
        # memberikan keterangan bahwa data sudah tersimpan ke list utama
        print('Item Sudah Dimasukkan ke Dalam Daftar.')

        # input yang menanyakan jika user ingin menambah item lain
        i_opsi = (input('Tambah Lagi (ya/tidak)? ').capitalize())

        # jika pilihan yang dimasukkan 'Ya', maka while akan kembali berjalan
        if i_opsi == 'Ya':
          continue
        
        # jika pilihan yang dimasukkan 'Tidak', maka while akan berhenti 
        elif i_opsi == 'Tidak':
          break

        # jika pilihan bukan 'Ya' atau 'Tidak', maka pesan error akan keluar
        else:
          print('Hanya Menerima Jawaban Ya atau Tidak.')

          i_opsi = (input('Tambah Lagi (ya/tidak)? ').capitalize())

      # menampilkan hasilnya dalam bentuk tabel
      self.check_order

      # hasil dari fungsi ini disimpan ke list utama
      return self.list_item
      
    def update_item_name(self):
      """
      Fungsi ini dan dua fungsi lainnya di bawah fungsi ini, bertugas untuk 
      mengganti Nama Item, Jumlah Item, atau Harga Item secara terpisah tanpa
      mengintervensi data lainnya.

      Cara kerjanya dengan menggunakan nomor urut Nama Item yang kemudian 
      dijadikan index untuk menemukan nama yang dicari dan menggantinya sesuai
      input yang diberikan.

      Return-nya berbentuk list yang dikembalikan lagi ke list utama.

      """
      # membuat index dari urutan Nama Item
      urutan = (int(input('Masukan No. Barang yang Akan Diubah: '))-1)

      # mengambil element list utama dan membentuknya menjadi "list baru"
      ilist = [*self.list_item[urutan]]

      # mencari index dari Nama Item yang akan diubah
      lama = input('Masukan Nama Barang Sebelumnya: ')
      i = ilist.index(lama.capitalize())
      
      # menyisipkan Nama Item yang baru di antara data-data lainnya
      baru = input('Masukan Nama Barang Setelahnya: ')
      ilist = ilist[:i]+[baru.capitalize()]+ilist[i+1:]

      # menghapus element list utama (ilist) yang diinterfensi
      self.list_item.pop(urutan)

      # mengembalikan element tersebut ke posisi semula dengan Nama Item baru
      self.list_item.insert(urutan, ilist)

      # menampilkan hasilnya dalam bentuk tabel
      self.check_order

      return self.list_item

    def update_item_qty(self):
      
      # membuat index dari urutan Jumlah Item
      urutan = (int(input('Masukan No. Jumlah yang Akan Diubah: '))-1)
      
      # mengambil element list utama dan membentuknya menjadi "list baru"
      ilist = [*self.list_item[urutan]]
      
      # mencari index dari Jumlah Item yang akan diubah
      lama = int(input('Masukan Jumlah Barang Sebelumnya: '))
      i = ilist.index(f'{lama} buah')
      
      # menyisipkan Jumlah Item yang baru di antara data-data lainnya
      baru = int(input('Masukan Jumlah Barang Setelahnya: '))
      ilist = ilist[:i]+[f'{baru} buah']+ilist[i+1:]
      
      # menghapus element list utama (ilist) yang diinterfensi
      self.list_item.pop(urutan)
      
      # mengembalikan element tersebut ke posisi semula dengan Jumlah Item baru
      self.list_item.insert(urutan, ilist)

      # menampilkan hasilnya dalam bentuk tabel
      self.check_order

      return self.list_item
    
    def update_item_price(self):

      # membuat index dari urutan Harga Item
      urutan = (int(input('Masukan No. Harga yang Akan Diubah: '))-1)

      # mengambil element list utama dan membentuknya menjadi "list baru"
      ilist = [*self.list_item[urutan]]
      
      # mencari index dari Harga Item yang akan diubah
      lama = int(input('Masukan Harga Barang Sebelumnya: '))
      i = ilist.index(f'Rp. {lama:,}')
      
      # menyisipkan Harga Item yang baru di antara data-data lainnya
      baru = int(input('Masukan Harga Barang Setelahnya: '))
      ilist = ilist[:i]+[f'Rp. {baru:,}']+ilist[i+1:]
      
      # menghapus element list utama (ilist) yang diinterfensi
      self.list_item.pop(urutan)
      
      # mengembalikan element tersebut ke posisi semula dengan Harga Item baru
      self.list_item.insert(urutan, ilist)

      # menampilkan hasilnya dalam bentuk tabel
      self.check_order

      return self.list_item
        

    def delete_item(self):
      """
      Fungsi ini bertujuan untuk menghilangkan satu baris Item atau element di
      dalam list utama.

      Cara kerjanya dengan menggunakan nomor urut Item yang kemudian dijadikan 
      index untuk method pop(index).

      Return-nya berbentuk list in list tanpa element yang sudah dihapus.

      """
      # memasukkan urutan item dan menjadikannya sebagai index
      urutan1 = (int(input('Masukan Urutan Barang yang Akan Dihapus: '))-1)
      
      # memanggil list utama dan mengilangkan element berdasarkan index di atas
      self.list_item.pop(urutan1)

      # memberikan keterangan bahwa item sudah berhasil dihapus
      print('Item Sudah Terhapus.')

      return self.list_item

    def reset_transaction(self):
      """
      Fungsi ini bertujuan untuk menghilangkan seluruh Item atau element di
      dalam list utama.

      Cara kerjanya dengan menggunakan method clear(index) pada list utama. 
      
      Return-nya list kosong.

      """
      # menggunakan method clear() pada list utama
      self.list_item.clear()

      # memberikan pesan bahwa item sudah terhapus
      print('Seluruh Barang Dalam Transaksi Sudah Terhapus.')

      return self.list_item

    def check_order(self):
      """
      Fungsi ini bertujuan untuk menampilkan seluruh data dalam list utama dalam
      bentuk tabel dengan Modul Tabulate.

      Return-nya tabel.

      """
      # menentukan headers dari tabel
      headers = ["No.",
                  "Nama Barang", 
                  "Jumlah Barang",
                  "Harga/Barang",
                  "Total Harga"]
      print('')
      # memasukkan ID User
      id_cust = input('Silakan Masukan ID Anda: ')

      print('')
      # menampilkan ID User
      print(f'Berikut Daftar Belanja Anda - ID {id_cust}: ')
      print('')

      #menampilkan tabel data transaksi 
      print(tabulate(self.list_item, headers, tablefmt="github"))
      print('|-------|---------------|-----------------|----------------|---------------|')
      print('')
      
      return


    def total_price(self):
      """
      Fungsi ini bertujuan untuk menghitung Total Transaksi yang merupakan sum
      dari element Total Harga fungsi add_item dan menerapkan diskon yang 
      diterima dengan syarat-syarat yang berlaku.
      
      Return-nya berbentuk string:
      Rp. 10,000.0

      """
      # mengambil element Total Harga dari setiap element list utama
      total = [sublist[4] for sublist in 
            [list(ele) for ele in self.list_item]]

      # mengembalikan tipe element Total Harga menjadi int
      total_int = []
      for th in total:
        total_int.append(int(th.translate({ord(i): None for i in 'Rp. ,'})))

      
      # menghitung total dari semua Total Harga
      gross = sum(total_int)
      # empty string untuk menyimpan hasil Total Transaksi setelah diskon
      nett = ''

      # memeriksa syarat-syarat diskon yang diterima
      if gross > 500_000:
        diskon_10 = gross - (gross*0.1)
      
        print('Selamat Anda Mendapatkan Diskon Sebesar 10%!')
        print('Total Transaksi Anda: ' + nett + f'Rp. {diskon_10:,}')

      elif gross > 300_000:
        diskon_8 = gross - (gross*0.08)

        print('Selamat Anda Mendapatkan Diskon Sebesar 8%!')
        print('Total Transaksi Anda: ' + nett + f'Rp. {diskon_8:,}') 

      elif gross > 200_000:
        diskon_5 = gross - (gross*0.05)
  
        print('Selamat Anda Mendapatkan Diskon Sebesar 5%!')
        print('Total Transaksi Anda: ' + nett + f'Rp. {diskon_5:,}') 

      else:
        print('Total Transaksi Anda: ' + nett + f'Rp. {gross:,}')
        
      return 
