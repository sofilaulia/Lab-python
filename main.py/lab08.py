# Nama: Sofil Muna Aulia
# NIM: 0110120115
# Kelas: Sistem Informasi 05

def hitung_kemunculan(s):
  # Tulis kode fungsi hitung_kemunculan() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
    import collections
    pecah = s.split()
    hitung = collections.Counter(pecah).most_common()
    for kata in hitung:
        x = ((kata[0],kata[1]))
        return x
 

def urut_unik(s):
  # Tulis kode fungsi urut_unik() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  
  pass

def read(filename):
  # Tulis kode fungsi read() di bawah ini
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
  r = hitung_kemunculan("pisang jambu apel jambu pisang jeruk")
  print(f"hitung_kemunculan('pisang jambu apel jambu pisang jeruk') = {r} \n(solusi: {{'pisang': 2, 'jambu': 2, 'apel': 1, 'jeruk': 1}})")
  print()
  r = urut_unik("pisang jambu apel jambu pisang jeruk")
  print(f"urut_unik('pisang jambu apel jambu pisang jeruk') = {r} \n(solusi: ['apel', 'jambu', 'jeruk', 'pisang'])")
  print()
  r = urut_unik('kecapi melon kecapi kecapi kecapi')
  print(f"urut_unik('kecapi melon kecapi kecapi kecapi') = {r} \n(solusi: ['kecapi', 'melon'])")
  print()
  r = read('data1.txt')
  print(f"read('data1.txt') = {r} \n(solusi: {{'101': 'Teddy-Bear', '102': 'Kelereng', '201': 'Laptop', '202': 'Smartphone', '203': 'Speaker', '301': 'Avanza', '302': 'Supra-X', '401': 'Topi', '402': 'Jaket', '403': 'Scarf'}}")
  print()
  r = read('data2.txt')
  print(f"read('nilai2.txt') = {r} \n(solusi: {{'711': 'Malaysia', '712': 'Singapura', '713': 'Indonesia', '814': 'USA', '815': 'Canada'}}")
  print()

if __name__ == '__main__':
  test()