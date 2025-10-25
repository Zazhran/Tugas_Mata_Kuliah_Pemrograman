nama_mahasiswa = ["Ahmad", "John", "Akira", "Beethoven", "Xi Jinping"]

print(nama_mahasiswa)

nama_input = input ("Masukkan Nama Mahasiswa\n")

if nama_input == ("Ahmad"):
    print(nama_mahasiswa[0], " Ada di list")
    
elif nama_input == ("John"):
    print(nama_mahasiswa[1], "Ada di list")
    
elif nama_input == ("Akira"):
    print(nama_mahasiswa[2], "Ada di list")
elif nama_input == ("Beethoven"):
    print(nama_mahasiswa[3], "Ada di list")
elif nama_input == ("Xi Jinping"):
    print(nama_mahasiswa[4], "Ada di list")
    
else:
    print("Nama tidak ada di dalam list")
