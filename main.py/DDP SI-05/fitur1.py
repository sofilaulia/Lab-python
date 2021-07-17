# NF BANK SI-05 E 
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

    # FITUR 1 BUAT REKENING 
    if Menu == "1" :
        nama = input("Masukkan nama: ")
        setoran_awal = eval(input("Masukkan setoran awal: "))
        # Membuat Nomor Rekening
        import random, string
        norek = "REK" + "".join(random.choice(string.digits)for _ in range(3))
        nasabah = (str(norek)) + "," + nama + "," + (str(setoran_awal)) 
        # Menambahkan data rekening baru ke file nasabah.txt
        myfile = open ("nasabah.txt","a")
        for element in nasabah:
            myfile.write(str(element))
        myfile.close()
        
    # FITUR 2 SETORAN TUNAI 
    elif Menu == "2" :
        rekening = input("Masukan nomor rekening: ") #masukan nama penggguna atau menggunakan inputan
        setor_nominal = int(input("Masukan nominal yang akan disetor: "))#masukan nama penggguna atau menggunakan inputan
        myfile = open ("nasabah.txt") #membuka file nasabah.txt
        data = [] #membuat atau inisialisasi list kosong untuk menyimpan data-data yang akan diupdate atau mneyimpan data sementara
        found = False #membuat atau inisialisasi data found di set ke False
        for element in myfile: #melakukan perulangan sebanyak data file
            i = element.strip().split(",") #strip() untuk membersihkan whitespace dan split() untuk memisahkan data berdasarkan koma
            if(rekening == i[0]): #kondisi untuk pengecekan apakah rekening terdaftar di dalam file nasabah.txt
                found = True #jika terdaftar set found jati True
                i[2] = int(i[2]) + setor_nominal #merubah saldo/ menambahkan saldo
            data.append(i) #menambahkan data baru ke dalam list
        myfile.close() #menutup file atau menandakan proses pemanggilan file sudah selesai
        if not found: #jika kondisi tidak found, tampilkan pesan
            print("Nomor rekening tidak terdaftar. Setoran tunai gagal.")
        else: #kondisi lain
            myfile = open("nasabah.txt", "w+") #membuka file nasabah.txt dan w+ (data baru akan ditulis menggantikan data lama di file)
            for i in data: #melakukan perulangan sebanyak data yang sudah ditambahkan
                myfile.write( i[0]+","+i[1]+","+str(i[2])+'\n') #menulis text ke dalam file nasabah.txt
            myfile.close() #menutup file atau menandakan proses pemanggilan file sudah selesai
            print("Setoran tunai sebesar "+str(setor_nominal)+" ke rekening "+rekening+" berhasil.") #menampilkan pesan yang menandakan proses sudah selesai

    # FITUR 3 TARIK TUNAI 
    elif Menu == "3" :
        pass
    # FITUR 4 TRANSFER 
    elif Menu == "4" :
        pass
    # FITUR 5 LIHAT DAFTAR TRANSFER 
    elif Menu == "5" :
        pass
    # KELUAR 
    elif Menu == "6" :
        print("Terima kasih atas kunjungan Anda...")
    else : 
        print("Pilihan Anda salah. Ulangi.")

