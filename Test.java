import java.io.*;
import java.util.*;
public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("How many numbers? ");
        int count = sc.nextInt();

        Thread t = new Thread(new NumberGenerator(count));
        t.start();
       
        System.out.println("How many numbers you want? ");
        count = sc.nextInt();

        NumberReader r = new NumberReader(count);
        Thread t2 = new Thread(r);

        System.out.println("Waiting for numbers to be generated...");
        try {
            t.join(); // wait till t does not complete
        } catch (InterruptedException e) {}
       
        t2.start();

        System.out.println("Waiting for numbers to be read...");
        try {
            t2.join(); // wait till t2 does not complete
        } catch (InterruptedException e) {}
       
        int[] arr = r.getArray();
        System.out.println(Arrays.toString(arr));
       
    }
}
class NumberGenerator implements Runnable {
    private int count;
    public NumberGenerator(int count) {
        this.count = count;
    }
    public void run() {
        generate();
    }
    public void generate() {
        try {
            Random r = new Random();
            FileWriter writer = new FileWriter("numbers.txt");
            for (int i = 1; i <= count; ++i) {
                writer.write(r.nextInt() + "\n");
                Thread.sleep(1000);
            }
            writer.close();
        } catch (IOException e) {}
        catch (InterruptedException e) {}
    }
}
class NumberReader implements Runnable {
    private int count;
    private int[] arr;
    public NumberReader(int count) {
        this.count = count;
    }
    public void run() {
        read();
    }
    public void read() {
        arr = new int[count];
        try {
            File file = new File("numbers.txt");
            Scanner reader = new Scanner(file);
            for (int i = 0; i < count; ++i) {
                arr[i] = reader.nextInt();
                Thread.sleep(1500);
            }
            reader.close();
        } catch (IOException e) {}
        catch (InterruptedException e) {}
    }
    public int[] getArray() {
        return arr;
    }
}