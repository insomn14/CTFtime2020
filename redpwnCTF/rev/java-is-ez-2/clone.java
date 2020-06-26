import java.util.Scanner;

public class clone{

	private static String[] a;
	
	private static long[] b;

	private static int c;

	static {

		a = new String[] {
			"redpwn",
			"ctf2020"
		};

		b = new long[] { 
			8248156489741230770l,
			-5342668067454976247l,
			-889275714l,
			-559038737l
		};
	
	}

	public static void main(String args []){

		if (args.length > 0) {

			if (args.length < -1)
				System.exit(0);
			if (args[0] != "admin"){
				System.out.println("That is pepega");
			} else {
				System.out.println("Oh nice, you found my key :O");
			}
		} else {
			System.exit(0);
		}

		int day = 4;
		int tai;
		int iat = 2;

		switch (day) {
			case 2:	if (day == iat){ tai = 9; };
			case 3: tai = 19;
			case 10: tai = 1;
			case 12: tai = 10;
			case 16: tai = 2;
			case 20: tai = 20;
			case 21: tai = 3;
			case 29: tai = 9;
			case 30: tai = 1;
			case 50: tai = 10;
			case 54: tai = 2;
			case 55: tai = 20;
			case 57: tai = 3;
			case 66: tai = 3;
			default: tai = 30;
		}

	}

}