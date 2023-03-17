/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] height = new int[9];
		int sum = 0;
		int a=0, b=0;
		
		for(int i=0;i<9;i++){
			height[i] = Integer.parseInt(br.readLine());
			sum += height[i];
		}
		Arrays.sort(height);
		
		for(int i=0;i<9;i++){
			for(int j=i+1;j<9;j++) {
				if(sum - height[i] - height[j] == 100) {
					a = i;
					b = j;
					break;
				}
			}
		}
		
		for (int i=0;i<9; i++) {
			if(i == a || i == b) continue;
			System.out.println(height[i]);
		}
	}
}