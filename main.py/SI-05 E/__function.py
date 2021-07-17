import os.path

def getAllNasabah():
    dataNasabah = []
    if os.path.isfile("laporanTransaksi/nasabah.txt"):
        fileNasabah = open("laporanTransaksi/nasabah.txt")
        for each_line in fileNasabah:
            if each_line != "\n" or "":
                data = each_line.split(",")
                dataNasabah.append([data[0], data[1], data[2]])
            else:
                continue
        fileNasabah.close()
    return dataNasabah


def validasiNasabah(nomor_rekening):
    validasiNasabah = False

    for nasabah in getAllNasabah():
        if nasabah[0] == nomor_rekening.upper():
            validasiNasabah = True
            break
    return validasiNasabah


def searchNasabah(nomor_rekening):
    cariNasabah = []

    for nasabah in getAllNasabah():
        if nasabah[0] == nomor_rekening.upper():
            cariNasabah.extend((nasabah[0], nasabah[1], nasabah[2]))
            break
    return cariNasabah


def saveProses(data, file):
    openFile = open(file, 'w+')
    for each_line in data:
        if each_line != "\n":
            convertString = str('{0},{1},{2}\n'.format(each_line[0], each_line[1], each_line[2]))
            openFile.write(convertString)
    openFile.close()


def kurangiSaldo(nomor_rekening, saldo, dataAllNasabah = getAllNasabah()):
    for i in range(0, len(dataAllNasabah)):
        if dataAllNasabah[i][0] == nomor_rekening.upper():
            # print(dataAllNasabah[i][2])
            dataAllNasabah[i][2] = int(dataAllNasabah[i][2]) - int(saldo)
            # print(dataAllNasabah[i][2])
    return dataAllNasabah
 

def tambahSaldo(nomor_rekening, saldo, dataAllNasabah = getAllNasabah()):
    for i in range(0, len(dataAllNasabah)):
        if dataAllNasabah[i][0] == nomor_rekening.upper():
            # print(dataAllNasabah[i][2])
            dataAllNasabah[i][2] = int(dataAllNasabah[i][2]) + int(saldo)
            # print(dataAllNasabah[i][2])
    return dataAllNasabah


def prosesTransfer(rekening_sumber, rekening_tujuan, nominal):
    kurang = kurangiSaldo(rekening_sumber, nominal)
    tambah = tambahSaldo(rekening_tujuan, nominal, kurang)
    saveProses(tambah, 'laporanTransaksi/nasabah.txt')


def getAllTransfer():
    dataTransfer = []

    if os.path.isfile("laporanTransaksi/transfer.txt"):
        fileNasabah = open("laporanTransaksi/transfer.txt")
        for each_line in fileNasabah:
            if each_line != "\n" or "":
                data = each_line.split(",")
                dataTransfer.append([data[0], data[1], data[2], data[3]])
            else:
                continue
        fileNasabah.close()
    return dataTransfer