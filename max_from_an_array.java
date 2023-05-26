public class max_from_an_array {
    public static void main(String[] args) {
        int a[]={ 1,2,3,4,56,6,7,9,23};
        int max=a[0];
        int max1=a[0];
       // here the time complexity is o(a.length)


        for(int i=0;i<a.length;i++){
            if (a[i]>max){
                max=a[i];

            }



        }
        System.out.println(max);

    }
}
