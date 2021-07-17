from __function import validasiNasabah, getAllNasabah, saveProses

def tarikTunai():
    print("\n*** Tarik Tunai ***")
    nomor_rekening = input("Masukkan nomor rekening: ")
    nominal        = int(input("Masukkan nominal yang akan ditarik: "))
    cek_norek      = validasiNasabah(nomor_rekening)
    if cek_norek:
        data_nasabah = getAllNasabah()
        for i in range(0, len(data_nasabah)):
            if data_nasabah[i][0] == nomor_rekening.upper():
                if int(data_nasabah[i][2]) < nominal :
                    print("Saldo tidak mencukupi. Tarik tunai gagal.")
                    break
                elif int(data_nasabah[i][2]) >= nominal:
                    data_nasabah[i][2] = int(data_nasabah[i][2]) - nominal
                    saveProses(data_nasabah, 'laporanTransaksi/nasabah.txt')
                    print("Tarik tunai sebesar Rp%d dari rekening %s berhasil" % (nominal, nomor_rekening.upper()))
                    break
            else:
                continue
    else:
        print("Gagal Tarik Tunai! - Rekening tidak terdaftar!")