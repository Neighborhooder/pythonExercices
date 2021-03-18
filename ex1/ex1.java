public class Oddity {
  public static boolean isOdd(int i) {
    // the objective of this function is to validate the oddity of a number, 
    // the right way to do this is: divide the number by 2 and verify if the rest of the division
    // is zero, if that's the case then the number is even, otherwise odd
    //
    // initial -> return i % 2 == 1;
    return i % 2 != 0;
  }
}
