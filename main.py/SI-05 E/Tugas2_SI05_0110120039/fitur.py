# NF BANK SI-05 E 
# NAMA KELOMPOK :
    # ANNISA PUTRI ANGGRAINI - 0110120039
    # MUHAMMAD IRFAN MAULANA - 0110120108
    # SOFIL MUNA AULIA - 0110120115
    # Z TIRRA TAUFIK - 0110120160
import random, string
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
        print("* TARIK TUNAI *")
        rek = input("Masukkan nomor rekening: ")
        nominal = int(input("Masukkan nominal yang akan ditarik:" )) 
        data = []
        found = False
        myfile = open("nasabah.txt")
        for baris in myfile:
            kata = baris.strip().split(",")
            if rek == kata[0]:
                found = True
                if str(nominal) <= str(kata[2] ) :
                    kata[2] = int(kata[2]) - nominal
                    print("Tarik tunai sebesar " + str(nominal) + " dari rekening " + rek + " berhasil")
                else:
                    print("Saldo tidak mencukupi. Tarik tunai gagal.")
            data.append(kata)
        myfile.close()
        if not found :
                print("Nomor rekening tidak terdaftar. Tarik tunai gagal.") 
        else:
            myfile = open("nasabah.txt","w")
            for kata in data:
                myfile.write( kata[0] + "," + kata[1] + "," + str(kata[2]) + "\n")
            myfile.close()

    # FITUR 4 TRANSFER 
    elif Menu == "4" :
        print("*** TRANSFER ***")
        rek_sumber = input("Masukan nomor rekening sumber: ")
        rek_tujuan = input("Masukan nomor rekening tujuan: ")
        nominal = input("Masukan nominal yang akan ditransfer: ")
        data = []
        myfile = open ("nasabah.txt")
        foundSumber = False
        foundTujuan = False
        saldoKurang = True
        for element in myfile: 
            i = element.strip().split(",") 
            if(rek_sumber == i[0]):
                foundSumber = True
                if(int(i[2]) >= int(nominal)):
                    i[2] = int(i[2]) - int(nominal) 
                    saldoKurang = False
            elif(rek_tujuan == i[0]):
                foundTujuan = True
                i[2] = int(i[2]) + int(nominal) 
            data.append(i)
        myfile.close()
        if not foundSumber: 
            print("Nomor rekening sumber tidak terdaftar. transfer gagal.")
        elif saldoKurang: 
            print("Transfer Gagal, Saldo tidak mencukupi")
        elif not foundTujuan: 
            print("Nomor rekening Tujuan tidak terdaftar. transfer gagal.")
        else: 
            myfile = open("nasabah.txt", "w+") 
            for i in data: 
                myfile.write( i[0]+","+i[1]+","+ str(i[2])+'\n') 
            myfile.close()
            kode = "TRF" + "".join(random.choice(string.digits)for _ in range(3))
            trf = open("transfer.txt", "a+") 
            trf.write(kode+","+rek_sumber+","+rek_tujuan+","+nominal+"\n") 
            trf.close()
            print("Transfer tunai sebesar "+ str(nominal) +" dari rekening " + rek_sumber+" ke rekening " + rek_tujuan+" berhasil.") 

    # FITUR 5 LIHAT DAFTAR TRANSFER 
    elif Menu == "5" :
        print("*** LIHAT DATA TRANSFER ***")
        rek_tf = input("Masukkan nomor rekening sumber transfer: ")
        # Membaca file nasabah.txt dan transfer.txt
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
        # Kondisi jika nomor rekening tidak tersedia
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
