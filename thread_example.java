import java.io.*;
import java.util.*;
public class thread_example{
    public static void main(String[] args){ 
        try{
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the number"); 
        int count=sc.nextInt();

       // Numbergenerator g=new Numbergenerator(count);
        Thread t=new Thread(new Numbergenerator(count));
        t.start();

        System.out.println("enter the number to read"); 
        count=sc.nextInt();
        NumberReader r=new NumberReader(count); 
        }
        catch(NoSuchElementException e){
            System.out.println("sorry");
        }
       
        



    }
}
 class Numbergenerator implements Runnable {
    private int count;
    public Numbergenerator(int count){
        this.count=count;
    }
   public  void run(){
        generator();
    }

    public  void generator(){
    try{
        Random r=new Random();
        FileWriter writer =new FileWriter("numbers.txt");
        for(int i=0;i<count;i++){
            //int a=r.nextInt(+ "\n");
            writer.write(r.nextInt()+ "\n");
            Thread.sleep(1000);

        }
        writer.close();
    } 
    
    catch (IOException e){} 
    catch(InterruptedException e){}
   }

} 
class NumberReader{
    public NumberReader(int count){
        reader(count);
    } 
    public int[] reader(int count){ 
        int arr[]=new int [count];
       try{
        File file=new File("numbers.txt"); 
        Scanner reader=new Scanner(file); 
            for(int i=0;i<count;i++){ 
                arr[i]=reader.nextInt();
                    

            } 
            reader.close();

       }
       catch( FileNotFoundException e){} 
       System.out.println(Arrays.toString(arr));
      return arr;
        }
}