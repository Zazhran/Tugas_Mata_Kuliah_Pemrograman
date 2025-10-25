nama_mahasiswa = ["Ahmad", "John", "Akira", "Beethoven", "Xi Jinping"]

print(nama_mahasiswa)

nama_input = input ("Masukkan Nama Mahasiswa\n").lower()

found = None
for nama in nama_mahasiswa:
    if nama.lower() == nama_input: #.lower() agar tidak mempedulikan kapital atau tidaknya
        found = nama
        break
    
if found:
    print(found, "Ada di list")
else:
    print("Nama tidak ada di dalam list")
