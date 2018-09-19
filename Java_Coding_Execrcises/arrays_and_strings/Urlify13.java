import java.io.*;
import java.util.*;


public class Urlify13{

  public static void main(String[] args){

    char[] roadHogQuote = "I'm a one man apocalypse".toCharArray();
    System.out.println(roadHogQuote);

    char[] urlSafe = makeUrlSafe(roadHogQuote);


  }

  public static char[] makeUrlSafe(char[] input){
    int numSpaces = 0;
    int inputLength = input.length;

    for (char c:input){
      if (c == ' '){
        numSpaces ++;
      }

    }

    if (numSpaces == 0){
      return input;
    }

    int outputLength = inputLength + 2 * numSpaces;

    char[] output = new char[outputLength];
    System.out.println("Initalized output is: " + output + " with a length of " + output.length);

    int outIndex = 0;
    for (char c:input){
      System.out.println("current char is: " + c);

      if (c == ' '){
        output[outIndex] = '%';
        output[outIndex + 1] = '2';
        output[outIndex + 2] = '0';
        outIndex += 3;
      }else{
        output[outIndex] = c;
        outIndex ++;

      }

    }

    for (char o:output){
      System.out.println(o);
    }

    System.out.println("output is: " + output);
    StringBuilder sb = new StringBuilder();
    for(char c: output) {
      sb.append(c);
    }

    System.out.println("Appended string is:" + sb.toString());

    return output;

  }

}
