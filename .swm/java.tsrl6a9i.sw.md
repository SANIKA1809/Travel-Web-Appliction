---
title: java
---
public class FactorialCalculator {

&nbsp;&nbsp;&nbsp;&nbsp;public static void main(String\[\] args) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;int number = 5; // Change this to calculate factorial for a different number

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;long factorial = calculateFactorial(numberr);

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System.out.println("Factorial of " + number + " is: " + factorial);

&nbsp;&nbsp;&nbsp;&nbsp;}

&nbsp;&nbsp;&nbsp;&nbsp;public static long calculateFactorial(int n) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (n == 0 || n == 1) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return 1;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} else {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return n \* calculateFactorial(n - 1);

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}

&nbsp;&nbsp;&nbsp;&nbsp;}

}

&nbsp;

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBVHJhdmVsLVdlYi1BcHBsaWN0aW9uJTNBJTNBU0FOSUtBMTgwOQ==" repo-name="Travel-Web-Appliction"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
