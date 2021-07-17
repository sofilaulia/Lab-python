import random, string, os.path
from __function import searchNasabah, prosesTransfer

def transfer():
    print("\n*** Transfer ***")
    nomor_transfer      = "TRF" + ''.join(random.choice(string.digits) for _ in range(3))
    norek_sumber        = input("Masukkan nomor rekening sumber: ").upper()
    data_rekeningSumber = searchNasabah(norek_sumber)
    norek_tujuan        = input("Masukkan nomor rekening tujuan: ").upper()
    data_rekeningTujuan = searchNasabah(norek_tujuan)

    if data_rekeningSumber:    
        if data_rekeningTujuan:
            nominal_transfer = int(input("Masukkan nominal yang akan ditransfer: "))
            if nominal_transfer <= int(data_rekeningSumber[2]):
                if os.path.isfile("laporanTransaksi/transfer.txt"):
                    laporan_transfer = open("laporanTransaksi/transfer.txt", "a+")
                else:
                    laporan_transfer = open("laporanTransaksi/transfer.txt", "w+")

                convert_string = str("{0},{1},{2},{3}\n".format(nomor_transfer, norek_sumber, norek_tujuan, nominal_transfer))
                laporan_transfer.write(convert_string)
                laporan_transfer.close()

                prosesTransfer(norek_sumber, norek_tujuan, nominal_transfer)
                print("Transfer sebesar: Rp%d dari rekening: %s ke rekening: %s berhasil." % (nominal_transfer, data_rekeningSumber[0], data_rekeningTujuan[0]))
            elif nominal_transfer > int(data_rekeningSumber[2]):
                print("Saldo rekening sumber tidak mencukupi. Transfer Gagal.")
        else:
            print("Nomor rekening tujuan tidak terdaftar. Transfer gagal.")
    else:
        print("Nomor rekening sumber tidak terdaftar. Transfer gagal.")