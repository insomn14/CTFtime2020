import java.util.Random;

public class seed {
    public static void main(String[] arrstring) {
 		Random random = new Random();
        random.setSeed(431289);
        for (int i = 0; i < 22; ++i) {
            System.out.print(random.nextInt(i + 1) + ", ");
        }
    }
}
