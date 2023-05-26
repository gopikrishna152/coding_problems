import java.util.Scanner;
public class linearsearch{
    public static void main(String[] args) {
        int[]a= { 1,2,3,4,5,6,78,8 };
        Scanner sc=new Scanner(System.in);
        int target=sc.nextInt();
        int count=0;
        for (int i=0;i<a.length;i++)
        {
            if (a[i]==target) {
                //System.out.println(i);
                count=count+1;

            }
        }
if(count==0){
    System.out.println("not found");

}
else{
    System.out.println("found at index");
}
        }
    }

