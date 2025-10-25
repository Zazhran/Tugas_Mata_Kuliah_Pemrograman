const namaMahasiswa = ["Ahmad", "John", "Akira", "Beethoven", "Xi Jinping"];
alert("Daftar Mahasiswa:\n" + namaMahasiswa.join(", "));
let namaInput = prompt("Masukkan Nama Mahasiswa: ").toLowerCase();
let ditemukan = false;

for (let i = 0; i < namaMahasiswa.length; i++){
    if(namaMahasiswa[i].toLowerCase() === namaInput){
        alert(`${namaMahasiswa[i]} ada di dalam list`);
        ditemukan = true;
        break;
    }
}
if (!ditemukan){
    alert("Nama tidak ada di dalam list");
}
