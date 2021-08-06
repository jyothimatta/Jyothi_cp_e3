// Write the method vowelCount(s), that takes a string s, 
// and returns the number of vowels in s, ignoring case, 
// so "A" and "a" are both vowels. The vowels are "a", "e", "i", "o", and "u". 
// So, for example, ("Abc def!!! a? yzyzyz!") returns 3 (two a's and one e).


import java.io.*;
  
public class MyString {
    public static void main(String[] args)
        throws IOException
    {
        String str = "GeeksForGeeks";
  
            str = str.toLowerCase();
  
        // toCharArray() is used to convert 
        // string to char array
        // char[] chars = str.toCharArray();
  
        int count = 0;
  
        for (int i = 0; i < str.length(); i++)
        {
            // check if char[i] is vowel
            if (str.charAt(i) == 'a' || str.charAt(i) == 'e'
                || str.charAt(i) == 'i'
                || str.charAt(i) == 'o'
                || str.charAt(i) == 'u')
            {
                // count increments if there is vowel in
                // char[i]
                count++;
            }
        }
  
        // display total count of vowels in string
        System.out.println("Total no of vowels in string are: " + count);
    }
}