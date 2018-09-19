import java.io.*;
import java.util.*;

public class PalindromePermutation14{

  public static void main(String[] args){
    String s = "HI HO, HI HO";
    checkPalindromability(s);


  }

  public static boolean checkPalindromability(String input){

    Integer[] occurances = new Integer[255];

    Arrays.fill(occurances, 0);

    for (int i = 0; i < input.length(); i ++){
      char curChar = input.charAt(i);

      if (curChar == ' '){
        System.out.println("Skip space");
      }
      else{
        curChar = Character.toLowerCase(curChar);
        System.out.println("curChar " + curChar);
        occurances[curChar] ++;
      }
    }

    boolean foundOdd = false;

    for (int i = 0; i < occurances.length; i++){

      if (occurances[i] % 2 == 1){
        if (foundOdd){

          return false;
        }else{
          System.out.println("I found an odd one! at " + i);
          foundOdd = true;
        }

      }

      System.out.print(occurances[i]);
    }
    return true;
  }



}
