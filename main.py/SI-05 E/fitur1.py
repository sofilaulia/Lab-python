# import modul
import random, string, os.path

# Fitur Buka Rekening
def bukaRekening():
    print("\n*** Buka Rekening ***")
    nomor_rekening = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
    nama_nasabah   = input("Masukkan nama: ")
    setoran_awal   = int(input("Masukkan setoran awal: "))

    # Mengecek isi file
    if os.path.isfile("laporanTransaksi/nasabah.txt"):
        # append
        laporan_nasabah = open("laporanTransaksi/nasabah.txt", "a+")
    else:
        #overwrite
        laporan_nasabah = open("laporanTransaksi/nasabah.txt", "w+")
    
    convert_string = str("{0},{1},{2}\n".format(nomor_rekening, nama_nasabah, setoran_awal))
    laporan_nasabah.write(convert_string)
    laporan_nasabah.close()
    print("\nPembukaan rekening dengan nomor %s atas nama %s berhasil.\n" % (nomor_rekening, nama_nasabah))