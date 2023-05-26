public class first_and_secondmax_from_an_array {

    public static void main(String[] args) {
        int a[]={ 1,2,3,4,56,6,7,9,23};
        int max=a[0];
        int max1=a[0];
        // here the time complexity is o(a.length)


        for(int i=0;i<a.length;i++){
            if (a[i]>max){
                max=a[i];

            }
            if(max1<a[i] && max>a[i]){
                max1=a[i];
            }


        }
        System.out.println("first max is   "+max);
        System.out.println("second max is  "+max1);
    }
}
