from __function import validasiNasabah, getAllNasabah, saveProses

def setoranTunai():
    print("\n*** Setoran Tunai ***")
    nomor_rekening = input("Masukkan nomor rekening: ")
    nominal        = int(input("Masukkan nominal yang akan disetor: "))
    cek_norek      = validasiNasabah(nomor_rekening)
    if cek_norek:
        data_nasabah = getAllNasabah()
        for i in range(0, len(data_nasabah)):
            if data_nasabah[i][0] == nomor_rekening.upper():
                data_nasabah[i][2] = int(data_nasabah[i][2]) + nominal
                saveProses(data_nasabah, 'laporanTransaksi/nasabah.txt')
                print("Setor tunai sebesar Rp%d dengan nomor rekening %s berhasil" % (nominal, nomor_rekening.upper()))
                break
            else:
                continue
    else:
        print("Gagal Setor Tunai! - Rekening tidak terdaftar!")