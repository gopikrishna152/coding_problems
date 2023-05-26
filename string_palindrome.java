import java.util.Scanner;

public class string_palindrome {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String reverseStr="";
        System.out.println("only give small lettered string otherwise just get out of here ");
        String word=sc.nextLine();
        int strLength=word.length();

        for (int i = (strLength - 1); i >=0; --i) {
            reverseStr = reverseStr + word.charAt(i);

        }
        if(word.equals(reverseStr)){
            System.out.println("palindrome");

        }
        else{
            System.out.println("not a palindrome");
        }



    }
}

