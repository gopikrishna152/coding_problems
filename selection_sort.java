public class selection_sort {
    public static void main(String[] args) {
        int a[]={1,8,7,5,3,4,6,9};
    int size=a.length;
        for(int i=0;i<size;i++){
int minind=i;
for(int j=i+1;j<size;j++){
if (a[j]<a[minind]){
minind=j;
}
}
int temp=0;
a[i]=temp;
a[i]=a[minind];
a[minind]=temp;
}
for(int k=0;k<size;k++){
System.out.print(a[k]+" ");
}
}
}