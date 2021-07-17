from __function import validasiNasabah, getAllNasabah

def riwayatSetor():
    print("\n*** Lihat Daftar Transfer ***")
    nomor_rekening = input("Masukkan nomor rekening: ")
    cek_norek      = validasiNasabah(nomor_rekening)
    if cek_norek : 
        riwayat_setor = []
        
        for i in getAllNasabah():
            if i[0] == nomor_rekening.upper() : 
                riwayat_setor.append(i)
            else:
                continue

        if len(riwayat_setor) == 0:
            print("Tidak ada data yang ditampilkan.")
        else:
            for i in riwayat_setor:
               print("%s telah melakukan setor tunai sebesar Rp%s pada tanggal" % (i[0], i[2]))
    else:
        print("Nomor rekening tidak terdaftar. Laporan setoran tunai gagal.")