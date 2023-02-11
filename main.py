from transaksi import *

trnsct_123 = Transaction() 

# memasukkan item belanjaan
trnsct_123.add_item()
# menampilkan tabel dari item-item belanjaan
trnsct_123.check_order()
# mengganti nama item
trnsct_123.update_item_name()
# mengganti jumlah item
trnsct_123.update_item_qty()
# mengganti harga item
trnsct_123.update_item_price()
# menampilkan total transaksi yang harus dibayarkan
trnsct_123.total_price()
# menghapus 1 baris item
trnsct_123.delete_item()
# menghapus seluruh riwayat transaksi
trnsct_123.reset_transaction()