import java.util.Scanner;
public class sum_of_natural_numbers {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        System.out.println("thesum of natural numbers is   "+ a*(a+1)/2);
      /*  here the time complexity is o(1)
       but we can also write in o(n) and o(n^2)
*/
    }
}
