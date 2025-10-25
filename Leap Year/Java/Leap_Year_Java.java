import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Masukkan Tahun: ");
        int tahun = input.nextInt();
        
        System.out.print("Masukkan Bulan: ");
        int bulan = input.nextInt();
        
        int hari;

        if (bulan == 2) {
            if ((tahun % 400 == 0) || (tahun % 4 == 0 && tahun % 100 != 0)) {
                hari = 29;
            } else {
                hari = 28;
            }
        } else if (bulan == 1 || bulan == 3 || bulan == 5 || bulan == 7 || bulan == 8 || bulan == 10 || bulan == 12) {
            hari = 31;
        } else {
            hari = 30;
        }

        System.out.println("Jumlah hari: " + hari);
    }
}

