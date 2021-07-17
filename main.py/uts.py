#membuat fungsi hitung dengan parameter a
def hitung(a):
    #jika var_angka di modulo 20 hasilnya sama dengan 5
    if var_angka % 20 == 5 :
        #program akan merubah nilai a menjadi desimal ditambah 0.1 
        var_desimal = (a * 0.1) + 0.1
        #program akan mengembalikan nilai pembulatan dari var_desimal 
        pembulatan = round(var_desimal)
        #program akan merubah nilai variabel pembulatan menjadi bentuk string diakhiri "0"
        hasil = str(pembulatan) + "0"
        #program akan mencetak hasil ke layar
        print(hasil)
    #namun jika nilai y > 1 atau nilai var_angka > 5
    elif y > 1 or var_angka > 5 :
        #program akan merubah nilai a menjadi desimal 
        var_desimal = a * 0.1
        #program akan mengembalikan nilai pembulatan dari var_desimal 
        pembulatan = round(var_desimal)
        #program akan merubah nilai variabel pembulatan menjadi bentuk string diakhiri "0"
        hasil = str(pembulatan) + "0"
        #program akan mencetak hasil ke layar
        print(hasil)
    #namun jika nilai y sama dengan 1
    elif y == 1 :
        #program akan merubah nilai a menjadi desimal
        var_desimal = a * 0.1
        #program akan mengembalikan nilai pembulatan dari var_desimal 
        pembulatan = round(var_desimal)
        #program akan merubah nilai variabel pembulatan menjadi bentuk string 
        hasil = str(pembulatan) 
        #program akan mencetak hasil ke layar
        print(hasil)
#program meminta input pengguna berupa angka
var_angka = eval(input("Masukan angka: "))
#program akan merubah value var_angka menjadi bentuk string 
x = str(var_angka)
#program akan menghitung panjang string 
y = len(x)
#nilai parameter untuk fungsi hitung diambil dari value var_angka
hitung(var_angka)