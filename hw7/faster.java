import java.math.BigInteger;

class faster{
    public static int emod(int a, BigInteger b, int c) {
        if (b.equals(new BigInteger("0"))) {
            return 1;
        } else if (b.mod(new BigInteger("2")).equals(new BigInteger("0"))) {
            int d = emod(a,b.divide(new BigInteger("2")),c);
            return (d*d) %c;
        } else {
            return ((a%c)*emod(a,b.subtract(new BigInteger("1")),c))%c;
        }
    }
    
    public static void main(String[] args) {
        System.out.println(emod(10, new BigInteger("600000000000000000000000000000000000000002"), 13));
        System.out.println(emod(17, new BigInteger("80000000000000000000000000000000001"), 100));
    }
}
