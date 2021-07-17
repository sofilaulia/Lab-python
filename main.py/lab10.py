# Nama: Sofil Muna Aulia
# NIM: 0110120115
# Kelas: Sistem Informasi 05

class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next
    
class LinkedList:
  def __init__(self, head = None):
    self.head = head
  
  def add_last(self, new_data):
    if self.head is None:
      self.head = Node(new_data)
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = Node(new_data)
  
  def cetak(self):
    if self.head is None:
      print('List kosong')
    else:
      current = self.head
      while current is not None:
        print(current.data, end=' ')
        current = current.next
      print()

  def sum_odd(self):
    # Tuliskan implementasi fungsi sum_odd() di bawah ini
    # Hapus pass jika implementasi sudah dibuat
    
    result= 0
    #nilai variabel awal 0
    current = self.head
    #nilai variabel current sama dengan self.head 
    while current is not None:
    #apabila variabel current bukan None maka akan menjalankan perulangan
      if current.data%2==1 :
      #jika data dibagi 2 memiliki sisa bagi 1
        result+= current.data
        #maka nilai variabel result akan menjadi nilai current ditambah dengan nilai current saat ini
      current=current.next
      #melakukan pemindahan data dengan increment
    return result
    #mengembalikan nilai result
  
  def get_max(self):
    # Tuliskan implementasi fungsi get_max() di bawah ini
    # Hapus pass jika implementasi sudah dibuat

    current = self.head
    #nilai variabel current sama dengan self head
    if current is None:
    #jika nilai current None
      return None
      #maka akan mengembalikan nilai None
    else:
    #sebaliknya
      maks = current.data
      #membuat variabel maks dengan nilai current
      while current is not None:
      #melakukan perulangan apabila nilai current tidak None
        if maks<current.data:
        #jika nilai variabel maks kurang dari nilai current.data
          maks=current.data
          #nilai maks akan menjadi nilai current.data
        current=current.next
        #nilai current akan melakukan increment
      return maks
      #mengembalikan nilai maks





# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  list1 = LinkedList()
  list1.add_last(1)
  list1.add_last(2)
  list1.add_last(3)
  list1.add_last(4)
  list1.add_last(5)
  print('list1 : ', end='')
  list1.cetak()
  r1 = list1.sum_odd()
  print(f"list1.sum_odd() = {r1} \t(solusi: 9)")
  r2 = list1.get_max()
  print(f"list1.get_max() = {r2} \t(solusi: 5)")
  print()

  list2 = LinkedList()
  list2.add_last(9)
  list2.add_last(9)
  list2.add_last(9)
  print('list2 : ', end='')
  list2.cetak()
  r1 = list2.sum_odd()
  print(f"list2.sum_odd() = {r1} \t(solusi: 27)")
  r2 = list2.get_max()
  print(f"list2.get_max() = {r2} \t(solusi: 9)")
  print()

  list3 = LinkedList()
  list3.add_last(6)
  list3.add_last(2)
  list3.add_last(8)
  list3.add_last(4)
  print('list3 : ', end='')
  list3.cetak()
  r1 = list3.sum_odd()
  print(f"list3.sum_odd() = {r1} \t(solusi: 0)")
  r2 = list3.get_max()
  print(f"list3.get_max() = {r2} \t(solusi: 8)")
  print()

  list4 = LinkedList()
  print('list4 : ', end='')
  list4.cetak()
  r1 = list4.sum_odd()
  print(f"list4.sum_odd() = {r1} \t(solusi: 0)")
  r2 = list4.get_max()
  print(f"list4.get_max() = {r2} \t(solusi: None)")
  print()

if __name__ == '__main__':
  test()