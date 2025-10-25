import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
       String[] namaMahasiswa = {"Ahmad", "John", "Akira", "Beethoven", "Xi Jinping"};
       
       for (String nama : namaMahasiswa){
           System.out.println(nama);
       }
       
       Scanner input = new Scanner(System.in);
       System.out.println("Masukkan Nama Mahasiswa");
       String namaInput = input.nextLine();
       
       boolean ditemukan = false;
       for (String nama : namaMahasiswa){
           if(nama.equalsIgnoreCase(namaInput)){
               System.out.println(nama + " Ada di list");
               ditemukan = true;
               break;
           }
       }
       if (!ditemukan){
           System.out.println("Nama tidak ada di dalam list");
       }
       input.close();
    }
}

