public class multi_dimension_array {
    public static void main(String[] args) {
        int a[][]={ {1,2},{3,4}};
        int b[][]={{5,6},{7,8}};
        for(int i=0;i<a.length;i++){
            for(int j=0;j<a.length;j++){
                System.out.println((a[i][j]*b[j][j])+(a[j][j]*b[j][i]));
            }
        }
    }
}
