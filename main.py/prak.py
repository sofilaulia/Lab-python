def cetak_nama(a):
    s = len(a)
    k = 0 
    while k < s :
        k = k + 1
        print(a[0:k])


b = input(">>> cetak_nama['']")
if b == "" :
    print("harus terdapat string")
else :
    a = b + ("!")
    cetak_nama(a)

def hitung(bil1, bil2, operator="+") :
    if operator == '' :
        hasil = (bil1) + (bil2) 
    elif operator == "-": 
        hasil = (bil1) - (bil2) 
    elif operator == "*":
        hasil = (bil1) * (bil2) 
    elif operator == "**":
        hasil = (bil1) ** (bil2) 
    elif operator == "/":
        hasil = (bil1) / (bil2) 
    elif operator == "//" :
        hasil = (bil1) // (bil2) 
    elif operator == "%":
        hasil = (bil1) % (bil2) 
    return hasil

bil1 = eval(input("masukan bilangan:")) 
bil2 = eval(input("masukan bilangan:"))
operator = input("masukan parameter:")

hitung(bil1, bil2, operator)
print("solusi", hitung(bil1, bil2, operator))