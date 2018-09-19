import java.io.*;
import java.util.*;


public class CheckPermutation12{

  public static void main(String[] args){

    int number_of_args = args.length;

    System.out.println("This is the args length!!!! " + number_of_args);

    for (String s:args){
      System.out.println(s);
    }

    String word1 = "ABCDEFG";
    String word2 = "DEABCFG";
    System.out.println("x " + word1 + "y " + word2 + " results " + is_permutation(word1, word2));

  }

  public static boolean is_permutation(String word1, String word2){

    if (word1.length() != word2.length()){
      return false;
    }

    HashMap<Character, Integer> count = new HashMap<Character, Integer>();

    for(int i = 0; i < word1.length(); i++){
      char char1 = word1.charAt(i);
      char char2 = word2.charAt(i);
      if (!count.containsKey(char1)){
        count.put(char1, 0);
      }
      if (!count.containsKey(char2)){
        count.put(char2, 0);
      }

      count.put(char1, count.get(char1) + 1);
      count.put(char2, count.get(char2) - 1);
    }
    System.out.println("count " + count.toString() + count.values().getClass().getTypeParameters());

    Iterator vals = count.values().iterator();

    while (vals.hasNext()){
      int cur = (Integer)vals.next();
      if(cur != 0){
        return false;
      }
    }


    return true;

  }

}
