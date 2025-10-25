let tahun = parseInt(prompt("Masukkan Tahun : "));
let bulan = parseInt(prompt("Masukkan bulan : "));
let hari;

if (bulan === 2 ) 
{
    if((tahun % 400 === 0) || (tahun % 4 === 0 && tahun % 100 != 0))
    {
        hari = 29;
    } else
    {
        hari = 28;
    }
} else if (([1, 3, 5, 7, 8, 10, 12]).includes(bulan))
    {
        hari = 31;
    }else
        {
            hari = 30;
        }
console.log("Jumlah Hari :", hari);
