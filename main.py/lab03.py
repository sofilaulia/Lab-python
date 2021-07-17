# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini

#program mencetak pesan ke layar
print("SOAL 1 - Permainan Gunting-Batu-Kertas")

#program mencetak pesan ke layar
print("------------------------------------------")
print("Ketentuan Permainan : ")
print("Player hanya dapat memasukan 1 dari 3 pilihan")
print ("yaitu Gunting/Batu/Kertas")
print()

#program meminta masukan pengguna player-1 
A=input("Masukkan pilihan Player-1: ")
#program meminta masukan pengguna player-2 
B=input("Masukkan pilihan Player-2: ")

#jika inputan A sama dengan inputan B
if A==B:
#maka cetak permainan seri
  print("Permainan Seri")

#jika inputan A gunting dan B kertas
if A=="gunting" and B=="kertas":
#maka cetak player 1 menang 
  print("Player-1 Menang")
#jika inputan A gunting dan B batu 
elif A=="gunting"and B=="batu":
#maka cetak player-2 menang
  print("Player-2 Menang")

#jika inputan A kertas dan inputan B gunting
if A=="kertas" and B=="gunting": 
#maka cetak print player 2 menang
  print("Player-2 Menang")
#jika inputan A kertas dan batu
elif A=="kertas"and B=="batu":
#maka cetak player 1 menang
  print("Player-1 Menang")

#jika inputan A batu dan inputan B gunting
if A=="batu" and B=="gunting":
#maka cetak player 1 menang 
  print("Player-1 Menang")
#jika inputan A batu dan inputan B kertas
elif A=="batu"and B=="kertas":
#maka cetak player 2 menang
  print("Player-2 Menang")

print()
# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini

#program mencetak pesan ke layar
print("SOAL 2 - Toko Buku Bekas")

#program mencetak pesan ke layar
print("------------------------------------------")
print("Program akan menghitung harga dari jumlah")
print("buku yang akan dibeli")
print("ketentuan harga buku : ")
print(" <=10 buku : Rp.20.000,-/buku")
print("11-25 buku : Rp.18.000,-/buku")
print("26-50 buku : Rp.15.000,-/buku")
print(">50 buku   : Rp.10.000,-/buku")
print()

#program meminta masukan pengguna berupa bilangan positif
buku=int(input("Masukan banyak buku yang akan dibeli: "))

#harga satuan buku tiap variabel
A = 20000
B = 18000
C = 15000
D = 10000

#menghitung total harga yang harus dibayar
var_a= buku * A
var_b= buku * B
var_c= buku * C
var_d= buku * D

#jika jumlah buku kurang dari sama dengan 10
if buku >= 1 and buku <= 10: 
#maka program akan mencetak pesan dibawah ini
  print("Total harga yang harus dibayar: Rp.", var_a)

#jika jumlah buku 11-25 buku 
elif buku >=11 and buku <= 25:
#maka program akan mencetak pesan dibawah ini
  print("Total harga yang harus dibayar: Rp.",var_b)

#jika jumlah buku 26-50 
elif buku >= 26 and buku <= 50:
#maka program akan mencetak pesan dibawah ini
  print("Total harga yang harus dibayar: Rp.",var_c)

#jika jumlah buku lebih dari 50
elif buku > 50:
#maka program akan mencetak pesan dibawah ini 
  print("Total harga yang harus dibayar: Rp.",var_d)
#jika tidak ada kondisi yang tercapai
else:
#program akan mencetak
  print("------------TERJADI KESALAHAN-------------")
  print("---bilangan tidak boleh bernilai negatif---")

print()
# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini

#program mencetak pesan ke layar
print("SOAL 3 - Mencetak Persegi")

#program mencetak pesan ke layar
print("------------------------------------------")
print("ketentuan :")
print("Baris ganjil dicetak dengan #")
print("Baris genap dicetak dengan $")
print()

#program meminta masukan pengguna berupa bilangan bulat
x=int(input("Masukan bilangan bulat: "))

#program akan melakukan for loop mulai dari 1 sebanyak variabel x
for i in range(1,x+1):
#jika i dalam variabel X dimodulo 2 hasilnya 0 menunjukan angka genap
  if (i%2 == 0):
#maka print "$ " sebanyak variabel x
    print ("$ "*x)
#jika i dimodulo 2 hasilnya tidak sama dengan 0 menunjukan angka ganjil
  elif (i%2 != 0):
#maka print "# " sebanyak variabel x
    print("# "*x)






  
     
   
    

 