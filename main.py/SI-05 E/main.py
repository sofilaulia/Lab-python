# Untuk memanggil fitur yang ada
from fitur1 import bukaRekening
from fitur2 import setoranTunai
from fitur3 import tarikTunai
from fitur4 import transfer
from fitur5 import riwayatTransfer
from fitur6 import riwayatSetor

# Pilihan Menu
def menu():
    print("\n***** SELAMAT DATANG DI NF BANK *****")
    print("MENU: ")
    print("[1] Buka Rekening")
    print("[2] Setoran Tunai")
    print("[3] Tarik Tunai")
    print("[4] Transfer")
    print("[5] Lihat Daftar Transfer")
    print("[6] Laporan Setoran Tunai")
    print("[7] Keluar")
    
    while True:
        pilihanMenu = input("Masukkan menu pilihan Anda: ")

        if pilihanMenu == "1":
            bukaRekening()
            tanya()
        elif pilihanMenu == "2":
            setoranTunai()
            tanya()
        elif pilihanMenu == "3":
            tarikTunai()
            tanya()
        elif pilihanMenu == "4":
            transfer()
            tanya()
        elif pilihanMenu == "5":
            riwayatTransfer()
            tanya()
        elif pilihanMenu == "6":
            riwayatSetor()
            tanya()
        elif pilihanMenu == "7":
            print("\nTerima kasih atas kunjungan Anda...")
            exit()
        else:
            print("\nPilihan Anda salah. Ulangi.")

# Konfirmasi Kembali Ke Menu
def tanya():
    tanya = input("\n\tKembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        print("\nTerima kasih atas kunjungan Anda...")
        exit()
    else:
        print("\n\tPilihan tidak ada !!!")
menu()