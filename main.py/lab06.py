# Nama: Sofil Muna Aulia
# NIM: 0110120115
# Kelas: Sistem Informasi 05

def jumlah_batas(nums, batas):
  # Tulis kode fungsi jumlah_batas() di bawah ini
  for elemen in nums:
    # untuk seluruh elemen yang ada dalam list nums
    if elemen < batas :
      #jika nilai elemennya < batas
      nums.remove(elemen) 
      #program akan mengahapus elemen tersebut dari list nums
      return jumlah_batas(nums, batas)
      #lalu kembali menjalankan fungsi jumlah_batas()
  return sum(nums)
  #ketika nilai elemen < batas telah tidak ada, maka program akan mengembalikan nilai seluruh elemen dalam nums yang tersisa untuk dijumlahkan


def list_nonvokal(s):
  # Tulis kode fungsi list_nonvokal() di bawah ini
  vokal = []
  #variabel berisi list kosong yang akan menyimpan elemen
  for elemen in s:
    #untuk semua elemen yang berada di dalam s
    if not (elemen.lower() in 'aiueo'):
      #jika tidak ada elemen berisi huruf kecil dalam aiueo
      vokal.append(elemen)
      #maka program akan menambahkan elemen terakhir pada list vokal
  return vokal
  #program akan mengembalikan nilai vokal
  

def list_modify(alist, command, position, value=None):
  # Tulis kode fungsi list_modify() di bawah ini
  if (command == "add") and ( position == "start") :
    #jika elemen command adalah "add" dan elemen position adalah "start"
    alist.insert(0, value)
    #maka program akan menyisipkan elemen value kedalam alist di indeks ke-0
    return alist
    #lalu program akan mengembalikan nilai alist
  elif (command == "add") and ( position == "end") :
    #jika elemen command adalah "add" dan elemen position adalah "end"
    alist.append(value)
    #maka program akan menambahkan value sebagai elemen terakhir dalam list
    return alist
    #program akan mengembalikan nilai alist
  elif (command == "remove") and ( position == "start") :
    #jika elemen command adalah "remove" dan elemen position adalah "start"
    del alist [0]
    #maka program akan menghapus elemen alist di indeks ke-0
    return alist
    #program akan mengembalikan nilai alist
  elif (command == "remove") and ( position == "end") :
    #jika elemen command adalah remove dan elemen position adalah "end"
    sum_indeks = len(alist) - 1 
    #maka program akan menghitung jumlah indeks dalam alist dan dikurangi 1 agar berada di indeks terakhir
    del alist [sum_indeks]
    #lalu program akan menghapus elemen alist yang berada di indeks yang sama dengan elemen sum_indeks
    return alist
    #program akan mengembalikan nilai alist




# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = jumlah_batas([8, 7, 6, 10, 1], 5)
  print(f"jumlah_batas([8, 7, 6, 10, 1], 5) = {r} \n(solusi: 31)")
  print()
  r = jumlah_batas([1, -7, -10, 1], -5)
  print(f"jumlah_batas([1, -7, -10, 1], -5) = {r} \n(solusi: 2)")
  print()
  r = list_nonvokal('Halo')
  print(f"list_nonvokal('Halo') = {r} \n(solusi: ['H', 'l'])")
  print()
  r = list_nonvokal('AAAAAooooo')
  print(f"list_nonvokal('AAAAAooooo') = {r} \n(solusi: [])")
  print()
  r = list_nonvokal('Saya cinta programming')
  print(f"list_nonvokal('Saya cinta programming') = {r} \n(solusi: ['S', 'y', ' ', 'c', 'n', 't', ' ', 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek') = {r} \n(solusi: ['bebek', 'ayam', 'ikan', 'kucing'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek') = {r} \n(solusi: ['ayam', 'ikan', 'kucing', 'bebek'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start') = {r} \n(solusi: ['ikan', 'kucing'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end') = {r} \n(solusi: ['ayam', 'ikan'])")
  print()

if __name__ == '__main__':
  test()