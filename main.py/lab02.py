# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini

#program mencetak pesan ke layar
print("SOAL 1")
#Program memberikan enter line 
print()
#program melakukan perulangan for range 3 parameter dengan selang 2
for i in range(100, 1, -2):
#program mencetak hasil i ke layar
  print(i, end=",")
#program memberikan enter line
print()
print()

# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini

#program mencetak pesan ke layar
print("SOAL 2")
#program memberikan enter line 
print()
#program meminta masukan user berupa bilangan dan mencetaknya ke layar
angka=eval(input("Masukan banyaknya angka : "))
#inisialisasi jumlah
Jumlah = 0
#program melakukan for loop berdasarkan variabel angka
for i in range(angka):
#program meminta masukan user berupa angka yang akan di average
  A=eval(input("Masukan angka : "))
#program melakukan penjumlahan angka 
  Jumlah= Jumlah+A
#program mecetak jumlah ke layar
print("Jumlah : ", Jumlah)
#program menghitung average dan mencetak hasilnya ke layar
print("Rata-rata : ", Jumlah/angka )
#program memberikan enter line 
print()

# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini 

#program mencetak pesan ke layar 
print("SOAL 3")
#program memberikan enter line 
print()
#program meminta pengguna untuk memasukan sebuah angka bilangan bulat dan mencetaknya ke layar
B=eval(input("Masukan sebuah bilangan bulat : "))
#program melakukan for loop sejumlah variabel B
for i in range(B): 
#program mencetak hasil proses for Loop "#" sebanyak variabel B
  print("# "*B)