public class bubble_sort {
    public static void main(String[] args) {
        int a[]={98,7,6,5,4,3,2,1};
        int c[]={ };
        int b=a.length;
        int temp;
        for(int i=0;i<b;i++){
            for(int j=1;j<b-i;j++){
                if( a[j-1]>a[j]){
                    temp=a[j];
                    a[j]=a[j-1];
                    a[j-1]=temp;
                }

            }
        }
        for(int k=0;k<b;k++){
            System.out.print(a[k]+" ");
        }

    }
}
