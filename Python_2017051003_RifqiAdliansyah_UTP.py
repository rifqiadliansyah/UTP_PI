"""
Nama Program    : Menghitung pembelian Telur di Toko Cendana (Digunakan oleh kasir toko)
Dibuat oleh     : Rifqi Adliansyah
Dibuat pada     : 23 Oktober 2021
Selesai pada    : 24 Oktober 2021
Revisi pada     : -
"""
username = input("Masukkan username: ")
password = input("Masukkan password: ")

if (username == "cendana" and password == "kasir"):
   print("\n")
   print('Program Hitung Pembelian Telur '.center(100, '='))
   print("\n")
   listTelor = ["Telor ayam kampung\t\tRp10.0000",
                "Telor ayam negri\t\tRp9.000", 
                "Telor Bebek\t\t\tRp12.000", 
                "Telor burung puyuh\t\tRp13.500"]
   hargaTelor = {'1':10000,'2':9000,'3':12000,'4':13500}
   print("================")
   print("Jenis telur")
   print("================")
   x=1
   total=0
   pil='y'
   for i in listTelor:
       print(x, ".", i)
       x = x+1
   while pil=='y':
    try:
        #input pilihan telor berupa angka (integer) dan banyaknya telor yang ingin dibeli(bisa integer/float) 
        pilihan, n = input(
        "Masukkan jenis telor yang akan dibeli dan jumlah (per kg) : ").split()
        #mengambil value dari dictionary hargaTelor 
        harga = hargaTelor.get(pilihan)
        #perhitungan total belanja telor dari harga telor di kali banyaknya telor(per/kg)
        total = total+float(harga)*float(n)
        print("Sukses , dimasukkan ke keranjang")
        pil=input("Ingin menambah telur lagi ?(y/n): ")
        if pil != 'y' and pil != 'n':
            print("Salah inputan,Input harus (y/n),Silahkan ulang dari awal")
            break
        if pil=='n':
            print("==========================================")
            print("Total yang harus dibayar : %.2f" % (total))
            uangPembayaran=float(input("Uang yang dibayarkan: "))
            print("==========================================")
            if uangPembayaran<total:
                #Menghitung kekurangan pembayaran
                print("Maaf, uang kurang sebesar %.2f"%(total-uangPembayaran))
            else:
                #Menghitung besarnya kembalian
                print("Kembalian sebesar : %.2f" %(uangPembayaran-total))
            break 
    except:
        print("Terjadi kesalahan, silahkan ulangi dari login")
        break
else:
    print("Terdapat kesalahan username atau password")
