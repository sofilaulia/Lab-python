from __function import validasiNasabah, getAllTransfer

def riwayatTransfer():
    print("\n*** Lihat Daftar Transfer ***")
    nomor_rekening = input("Masukkan nomor rekening sumber transfer: ")
    cek_norek      = validasiNasabah(nomor_rekening)
    if cek_norek : 
        riwayat_transfer = []
        
        for i in getAllTransfer(): 
            if i[1] == nomor_rekening.upper() : 
                riwayat_transfer.append(i)
            else:
                continue
            
        if len(riwayat_transfer) == 0:
            print("Tidak ada data yang ditampilkan.")
        else:
            for i in riwayat_transfer:
               print("{0}, {1}, {2}, {3}".format(i[0], i[1], i[2], i[3]))
    else:
        print("Nomor rekening tidak terdaftar. Lihat data transfer gagal.")