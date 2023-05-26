import java.util.Scanner;
public class binary_search {
    public static void main(String[] args) {
        int a[]={ 1,2,3,4,5,6,7,8,9,10};
        int low=1;
        int index;
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the searchiong element" );
        int key=sc.nextInt();
        int count=0;
        int high=a.length;
        while(low<=high){
            int mid=(low+high)/2;
            if(a[mid]>key){
                high=mid-1;
            }
            else if(a[mid]<key){
                low=mid+1;
            }
            else if (a[mid]==key){
                count=count+1;
                index=mid;
                System.out.println("index is "+ index);
                break;


            }
        }
        if(count==0){
            System.out.println("element not found");
        }
        else{
            System.out.println("element found");

        }
    }
}
