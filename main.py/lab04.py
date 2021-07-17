# DDP LAB-4
# Nama: SOFIL MUNA AULIA
# NIM: 0110120115

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini

#program akan mencetak pesan ke layar
print("SOAL 1 - Mencetak nama\n")
 
#program meminta masukan pengguna
nama=input("Masukan sebuah nama: ")
#program menghitung panjang string 
s= len(nama)
#variabel dengan nilai awal 0 
k=0
#program melakukan while loop sejumlah variabel s
while k < s:
#variabel k akan ditambah 1 setiap perulangan
  k= k+1
#program mencetak setiap string 
  print (nama[0:k])

# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini
print()
#program mencetak pesan ke layar
print("SOAL 2 - Validasi teks\n")

#program melakukan perulangan 
while True:
#untuk variabel teks
    teks=input("Masukan sebuah teks: \n")
#program menghitung panjang string dalam teks
    x=len(teks)
#syarat 1 (minimal terdiri dari 8 karakter)
    a= 8
#syarat 2 (Teks mengandung minimal sebuah frase 'NF')
    b= ("nf" in teks) or ("NF" in teks) or ("Nf" in teks) or ("nF" in teks)
#syarat 3 (teks mengandung minimal sebuah angka)
    c= ("0" in teks) or ("1" in teks) or ("2" in teks) or ("3" in teks) or ("4" in teks) or ("5" in teks) or ("6" in teks) or ("7" in teks) or ("8" in teks) or ("9" in teks)
#syarat 4 (Teks diakhiri dengan 'YYY' atau 'yyy')
    d= teks.endswith('yyy') or teks.endswith('YYY')
#jika syarat dari a sampai d terpenuhi
    if x >= a and b and c and d :
#maka program akan mencetak pesan ini ke layar
        print('teks valid')
#namun jika tidak
    else: 
#program akan mencetak pesan ini ke layar
        print("teks tidak valid")