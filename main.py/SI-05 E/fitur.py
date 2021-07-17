# NF BANK SI-05 E 
# NAMA KELOMPOK :
    # ANNISA PUTRI ANGGRAINI - 0110120039
    # MUHAMMAD IRFAN MAULANA - 0110120108
    # SOFIL MUNA AULIA - 0110120115
    # Z TIRRA TAUFIK - 0110120160
from fitur4 import transfer
x = 1
while x > 0:
    print ("\n" """ ***** SELAMAT DATANG DI NF BANK *****
    MENU: 
    [1] Buka Rekening
    [2] Setoran tunai
    [3] Tarik tunai 
    [4] Transfer 
    [5] Lihat daftar transfer
    [6] Keluar """)
    Menu = input("Masukkan menu pilihan Anda : ") 
    print()
    # FITUR 1 BUAT REKENING 
    if Menu == "1" :
        print("*** BUKA REKENING ***")
        nama = input("Masukkan nama: ")
        setoran_awal = eval(input("Masukkan setoran awal: "))
        import random, string
        norek = "REK" + "".join(random.choice(string.digits)for _ in range(3))
        nasabah = (str(norek)) + "," + nama + "," + (str(setoran_awal)) 
        myfile = open ("nasabah.txt","a")
        for element in nasabah:
            myfile.write(str(element))
        myfile.close()
        
    # FITUR 2 SETORAN TUNAI 
    elif Menu == "2" :
        print("*** SETORAN TUNAI ***")
        rekening = input("Masukan nomor rekening: ") 
        setor_nominal = int(input("Masukan nominal yang akan disetor: "))
        myfile = open ("nasabah.txt") 
        data = [] 
        found = False 
        for element in myfile: 
            i = element.strip().split(",") 
            if(rekening == i[0]): 
                found = True 
                i[2] = int(i[2]) + setor_nominal 
            data.append(i) 
        myfile.close()
        if not found: 
            print("Nomor rekening tidak terdaftar. Setoran tunai gagal.")
        else: 
            myfile = open("nasabah.txt", "w+") 
            for i in data: 
                myfile.write( i[0]+","+i[1]+","+ str(i[2])+'\n') 
            myfile.close() 
            print("Setoran tunai sebesar "+ str(setor_nominal) +" ke rekening " + rekening+" berhasil.") 
        
    # FITUR 3 TARIK TUNAI 
    elif Menu == "3" :
        print("*** TARIK TUNAI ***")
        rekening = input("Masukan nomor rekening: ")
        tarik_tunai = int(input("Masukan nominal yang akan ditartik: "))
        myfile = open ("nasabah.txt") 
        data = [] 
        found = False 
        for element in myfile:
            i = element.strip().split(",") 
            if(rekening == i[0]): 
                found = True 
                i[2] = int(i[2]) - tarik_tunai 
            data.append(i)
        myfile.close()
        if not found:
            print("Nomor rekening tidak terdaftar. Tarik tunai gagal.")
        else:
            myfile = open("nasabah.txt", "w+")
            for i in data:
                myfile.write( i[0]+","+i[1]+","+ str(i[2])+'\n')
            myfile.close()
            print("Tarik tunai sebesar "+ str(tarik_tunai) +"   ke rekening " + rekening+" berhasil.")

    # FITUR 4 TRANSFER 
    elif Menu == "4" :
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
        transfer()

    # FITUR 5 LIHAT DAFTAR TRANSFER 
    elif Menu == "5" :
        print("*** LIHAT DATA TRANSFER ***")
        rek_tf = input("Masukkan nomor rekening sumber transfer: ")
        myfile1 = open ("nasabah.txt", "r")
        myfile2 = open ("transfer.txt", "r")
        for baris in myfile1:
            if rek_tf in baris:
                for element in myfile2:
                    data = element.split(",")
                    rek_sumber = data[1]
                    if rek_tf == rek_sumber:
                        print(element)
                    else:
                        pass
                break
        if rek_tf not in baris:
            print("Nomor rekening tidak tersedia")
        myfile2.close()
        myfile1.close()
 
    # KELUAR 
    elif Menu == "6" :
        print("Terima kasih atas kunjungan Anda...")
        break
    else : 
        print("Pilihan Anda salah. Ulangi.")
