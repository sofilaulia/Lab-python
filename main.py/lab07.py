# Nama: Sofil Muna Aulia
# NIM: 0110120115
# Kelas: Sistem Informasi 05

def convert_list(multilist):
  # Tulis kode fungsi convert_list() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  gabung = sum(multilist, [])  
  return gabung
    
def get_nilai(filename, nama):
  # Tulis kode fungsi get_nilai() di bawah ini
  f = open(filename,'r')
  for baris in f:
    if nama.lower() in baris.lower():
      data = baris.split()
      nama = data[0]
      nilai = float(data[1])
      angka = round(nilai)
      return angka
  f.close()

def nilai_max(filename):
  # Tulis kode fungsi nilai_max() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  
 pass



# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = convert_list([[1,2], [3,4], [5,6]])
  print(f"convert_list([[1,2], [3,4], [5,6]]) = {r} \n(solusi: [1, 2, 3, 4, 5, 6])")
  print()
  r = get_nilai('nilai1.txt','joni')
  print(f"get_nilai('nilai1.txt','joni') = {r} \n(solusi: 76)")
  print()
  r = get_nilai('nilai2.txt','joni')
  print(f"get_nilai('nilai2.txt','joni') = {r} \n(solusi: None)")
  print()
  r = nilai_max('nilai1.txt')
  print(f"nilai_max('nilai1.txt') = {r} \n(solusi: ('Zack', 88.05)")
  print()
  r = nilai_max('nilai2.txt')
  print(f"nilai_max('nilai2.txt') = {r} \n(solusi: ('Arya', 90.00)")
  print()

if __name__ == '__main__':
  test()