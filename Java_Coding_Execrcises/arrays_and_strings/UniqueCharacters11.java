import java.io.*;
import java.util.*;



public class UniqueCharacters11 {

  public static void main(String[] args) {
    System.out.println("You hear that princess, those are the shrieking eels!");

    System.out.printf("%s\n", "shriek!");

    String no_duplicates = "single quot";

    System.out.println("INPUT " +no_duplicates+" gave result of: " + uniqueness_checker(no_duplicates));

    String some_duplicates = "eel1: Shriek!, eel2: Shriek!";

    System.out.println("INPUT " +some_duplicates+" gave result of: " + uniqueness_checker(some_duplicates));
  }

  public static  boolean uniqueness_checker(String input) {

    HashSet<Character> my_lazy_set = new HashSet<Character>();

    for (int i = 0; i < input.length(); i++){

      char cur = input.charAt(i);

      if (my_lazy_set.contains(cur)){
        return false;
      }

      my_lazy_set.add(cur);
    }

    return true;

  }
}
