tahun = int(input("Masukkan Tahun :"))
bulan = int(input("Masukkan bulan :")) 

if bulan == 2:
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        hari = 29
        
    else:
        hari = 28
        
elif bulan in [1, 3, 5, 7, 8, 10, 12]:
    hari = 31
else:
    hari = 30
    
print("Jumlah hari :", hari)

