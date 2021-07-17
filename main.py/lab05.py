def cetak_nama(nama):
  # Tulis kode fungsi cetak_nama di bawah ini
  # Hapus pass jika implementasi sudah dibuat

#jika dalam variabel b tidak ada inputan/string kosong
  if (nama == ""):
  #maka cetak pesan dibawah ini
    print("Tidak ada nama yang dicetak")
    #jika tidak
  else:
    #hitung jumlah panjang string a dan ditambah 1 untuk menambahkan karakter"!"
    s = len(nama)+1
    #variabel dengan nilai awal 0 
    k = 0 
    #program melakukan while loop sejumlah variabel s
    while k < s :
    #variabel k akan ditambah 1 setiap perulangan
        k = k + 1
        #jika sudah mencapai s
        if (k == s):
        #program mencetak string yang diakhiri dengan karakter '!'
          print(nama[0:k]+"!")
        #jika tidak
        else:
          #program mencetak nama perkarakter
          print(nama[0:k])


def hitung_kesamaan(kata1, kata2):
  # Tulis kode fungsi hitung_kesamaan di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  #menghitung jumlah huruf dalam kata1 dan disimpan ke variabel p   
  p = len(kata1)
  #menghitung jumlah huruf dalam kata2 dan disimpan ke variabel q   
  q = len(kata2)
  #variabel nilai awal
  r = 0
  #jika nilai p lebih besar dari q
  if(p > q):
    #looping untuk menghasilkan persatuan bagian dalam kata1
    for element in range(q):
      #memisahkan kalimat dari variabel kata1 dan kata2 menggunakan string splicing
      a = kata1[element]
      z = kata2[element]
      #jika kata1 sama dengan kata2
      if a == z:
        #maka akan bernilai 1 yang otomatis dihitung saat looping
        r += 1
    #mengembalikan nilai hasil akhir 
    return r
  #jika tidak
  else:
    #looping untuk menghasilkan persatuan bagian dalam kata untuk dibandingkan
    for element in range(p):
      #memisahkan kalimat dari variabel kata1 dan kata2 menggunakan string splicing
      a = kata1[element]
      z = kata2[element]
      #jika kata1 sama dengan kata2
      if a == z:
        #maka akan bernilai 1 yang otomatis dihitung saat looping
        r += 1
    #mengembalikan nilai hasil akhir 
    return r

def hitung(bil1, bil2, operator='+'):
  # Tulis kode fungsi hitung() di bawah ini
  # Hapus pass jika implementasi sudah dibuat

    #jika operator berisi string kosong
    if operator == '' :
        #maka hitung hasil dengan operator default +
        hasil = (bil1) + (bil2) 
    #namun apabila operator berisi string"+"
    elif operator == "+" :
      #maka hitung hasil dengan operator
      hasil = (bil1) + (bil2)
    #namun apabila operator berisi string "-"
    elif operator == "-": 
        #maka hitung hasil dengan operator -
        hasil = (bil1) - (bil2) 
    #namun apabila operator berisi string "*"
    elif operator == "*":
        #maka hitung hasil dengan operator "*"
        hasil = (bil1) * (bil2) 
    #namun apabila operator berisi string "**"
    elif operator == "**":
        #maka hitung hasil dengan operator "**"
        hasil = (bil1) ** (bil2) 
    #namun apabila operator berisi string "/"
    elif operator == "/":
        #maka hitung hasil dengan operator "/""
        hasil = (bil1) / (bil2) 
    #namun apabila operator berisi string "//"
    elif operator == "//" :
        #maka hitung hasil dengan operator "//"
        hasil = (bil1) // (bil2) 
    #namun apabila operator berisi string "%"
    elif operator == "%":
        #maka hitung hasil dengan operator "%"
        hasil = (bil1) % (bil2) 
    #mengembalikan nilai hasil
    return hasil


# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya
# (untuk fungsi hitung_kesamaan() dan fungsi hitung()).
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  print("Hasil cetak_nama('Mawar'):")
  cetak_nama("Mawar")
  print()
  print("Hasil cetak_nama(''):")
  cetak_nama("")
  print()
  r = hitung_kesamaan('python', 'path')
  print(f"hitung_kesamaan('python', 'path') = {r} \t(solusi: 3)")
  r = hitung_kesamaan('masak', 'cuci')
  print(f"hitung_kesamaan('masak', 'cuci') = {r} \t(solusi: 0)")
  r = hitung_kesamaan('python', '')
  print(f"hitung_kesamaan('python', '') = {r} \t\t(solusi: 0)")
  print()
  r = hitung(4, 8)
  print(f'hitung(4, 8) = {r} \t\t(solusi: 12)')
  r = hitung(4, 8, '-')
  print(f"hitung(4, 8, '-') = {r} \t(solusi: -4)")
  r = hitung(4, 8, '*')
  print(f"hitung(4, 8, '*') = {r} \t(solusi: 32)")
  
if __name__ == '__main__':
  test()

