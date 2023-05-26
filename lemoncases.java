import java.util.Scanner;

public class lemoncases {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the no of lemons");
        int lemons;
        lemons=sc.nextInt();
        if(lemons==21){
            System.out.println("sufficient");
        }
        else if(lemons>21 && lemons>0){
            int more;
            more=lemons-21;
            System.out.println("you have "+" "+more+" "+"no of lemons extra");
        }
        else if(lemons<21 && lemons>0){
            int less;
            less=21-lemons;
            System.out.println(less+"   are required lemons so pls buy those no of lemons");
        }
        else{
            System.out.println("pls enter the valid data");
        }
    }
}
