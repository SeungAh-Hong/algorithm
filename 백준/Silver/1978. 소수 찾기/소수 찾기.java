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
		int num = Integer.parseInt(br.readLine());
		int cnt = 0;
		String str = br.readLine();
		StringTokenizer st = new StringTokenizer(str, " ");
		for(int i=0;i<num;i++) {
			int k = Integer.parseInt(st.nextToken());
			boolean isPrime = true;
			
			if(k==1)
				continue;
			for(int j=2; j<=Math.sqrt(k); j++) {
				if (k % j ==0) {
					isPrime = false;
				}
			}
			if(isPrime){
				cnt++;
			}
		}
		
		System.out.println(cnt);
	}
}