#Nama  : Sofil Muna Aulia
#NIM   : 0110120115
#kelas : Sistem Informasi 05

#program akan mencetak pesan ke layar
print("------------------FITUR INPUT NILAI MAHASISWA-------------------")
#new line
print()
#Program meminta masukan pengguna berupa input NIM
nim = input("Masukan NIM : ")
#Nilai awal untuk perulangan
x = 1
c = 0
indeks = 0
total_sks = 0
#Program akan melakukan perulangan jika kondisi x > 0
while x > 0 :
    #Program meminta masukan pengguna berupa jumlah matkul yang akan diambil 
    matkul = eval(input("Berapa jumlah mata kuliah yang akan diambil? "))
    #enter line
    print()
    #Jika value dari variabel matkul kurang dari 1 atau lebih dari 8 
    if matkul < 1 or matkul > 8 :
        #maka program akan mencetak pesan dibawah ini ke layar 
        print("Jumlah mata kuliah harus antara 1-8")
        print()
    #namun jika tidak
    else:
        #program akan melakukan perulangan sebanyak nilai variabel matkul
        for i in range (matkul) :
                #ketika looping dilakukan, variabel c akan ditambah 1
                c = c + 1
                #program akan mencetak pesan ke layar diakhiri nilai dalam variabel c
                print("Nilai Mata Kuliah", c )
                #program meminta masukan pengguna berupa nama matkul
                nama_matkul = input("Nama mata kuliah : ")
                #program meminta masukan pengguna berupa jumlah sks
                ks_matkul = eval(input("Beban SKS mata kuliah : "))
                #program akan menyimpan nilai variabel ks_matkul ditambah nilai total_sks
                total_sks += ks_matkul
                #program meminta masukan pengguna berupa nilai kuis
                nilai_kuis = eval(input("Nilai kuis : "))
                #program meminta masukan pengguna berupa nilai tugas 1
                nilai_tugas1 = eval(input("Nilai Tugas 1 : "))
                #program meminta masukan pengguna berupa nilai tugas 2
                nilai_tugas2 = eval(input("Nilai Tugas 2 : "))
                #program meminta masukan pengguna berupa nilai uts
                nilai_uts = eval(input("Nilai UTS : "))
                #program meminta masukan pengguna berupa nilai uas
                nilai_uas = eval(input("Nilai UAS : "))

                #program akan menghitung total nilai berdasarkan persentase bobot nilai yang telah ditentukan
                total_nilai = 0.15 * nilai_kuis + 0.15 * nilai_tugas1 + 0.20 * nilai_tugas2 + 0.25 * nilai_uts + 0.25 * nilai_uas
                #program akan mencetak total nilai yang telah dihitung ke layar 
                total = print("Nilai untuk mata kuliah ", nama_matkul, "adalah ",round(total_nilai,2), end=" ")
                #nilai variabel grade sama dengan nilai variabel total_nilai
                grade = total_nilai
                #jika 85 kurang dari total nilai dan kurang dari sama dengan 100
                if 85 < total_nilai <= 100:
                    #maka program akan mengitung nilai indeks 
                    indeks += (4.0 *ks_matkul) 
                    #program akan mencetak pesan dibawah ini ke layar
                    print("(Grade A)")
                #namun jika 70 kurang dari total nilai dan kurang dari 85
                elif 70 < total_nilai < 85:
                    #maka program akan mengitung nilai indeks 
                    indeks += (3.0 *ks_matkul)      
                    #maka program akan mencetak pesan dibawah ini ke layar
                    print("(Grade B)")
                #namun jika 55 kurang dari total nilai dan kurang dari 70
                elif 55 < total_nilai < 70 :
                    #maka program akan mengitung nilai indeks 
                    indeks += (2.0 *ks_matkul) 
                    #maka program akan mencetak pesan dibawah ini ke layar
                    print("(Grade C)")
                #namun jika 40 kurang dari total nilai dan kurang dari 50
                elif 40 < total_nilai < 55 :
                    #maka program akan mengitung nilai indeks 
                    indeks += (1.0 *ks_matkul)
                    #maka program akan mencetak pesan dibawah ini ke layar
                    print("(Grade D)")                     
                #namun jika total nilai kurang dari 40 
                elif total_nilai < 40 :
                    #maka program akan mengitung nilai indeks 
                    indeks += (0.0 *ks_matkul) 
                    #maka program akan mencetak pesan dibawah ini ke layar
                    print("(Grade E)")
                #new line
                print()
                
        #jika nilai grade tidak kosong atau null
        if grade  != "" :
            #maka program akan berhenti melakukan perulangan
            break

#program akan menghitung nilai indeks prestasi yang didapatkan
indeks_prestasi = indeks/total_sks 

#new line
print()
#program akan mencetak pesan ke layar
print("-------------------------RANGKUMAN--------------------------")
#new line
print()
#program akan mencetak pesan ke layar diakhiri nilai nim
print("NIM : ",nim)
#program akan mencetak pesan ke layar diakhiri total jumlah sks
print("Total SKS : ",total_sks)
#program akan mencetak pesan ke layar diakhiri nilai indeks prestasi yang didapatkan
print("Indeks Prestasi : ", round(indeks_prestasi,2))