public class K {
    /*

    Problema K
    Mentirinha

        Thiago gosta muito de matemática, tanto que até inventa suas próprias definições sobre números! Por
    exemplo, Thiago é fascinado pelos números primos e já sabe diversas características sobre eles, em uma
    tarde chuvosa pensou que poderia criar uma definição chamada "primos de mentirinha".
    Como sabemos, números naturais primos têm apenas dois divisores naturais, isto é, são divisíveis por 1 e
    por eles mesmos. Já os "primos de mentirinha"de Thiago têm apenas um divisor a mais, ou seja, têm três
    divisores naturais.

    Sua missão é criar um programa que possa ajudar Thiago a descobrir se um dado número natural pode ser
    considerado um "primo de mentirinha".

    Entrada
    A entrada contém um único número natural N (1 < N < 1000000) que é o número que Thiago quer saber
    se é um "primo de mentirinha".

    Saída
    A saída será a palavra ’sim’ ou a palavra ’nao’ (sem apóstrofos, sem acentuação e em minúsculo), que
    indicará se N é um "primo de mentirinha"segundo a definição de Thiago.

   Entrada1  7
   Saída 1   nao

   Entrada2  4
   Saída 2   sim

   Entrada3  9
   Saída3    sim

   Entrada4  994009
   Saída 4   sim

   Entrada5  999983
   Saída 5   nao
     */

    public static void main(String[] args) {
        testIsFakePrime(7);
        testIsFakePrime(4);
        testIsFakePrime(9);
        testIsFakePrime(994009);
        testIsFakePrime(999983);
    }

    public static String isFakePrime(int n) {
        if (n <= 2) return "nao";

        for (int i = 2; i * i <= n; i++)
            if (n % i == 0)
                return "nao";

        return "sim";
    }

    public static void testIsFakePrime(int n) {
        System.out.println("Input: " + n);

        double totalTime = 0;
        String result = "";
        for (int i = 0; i < 10_000; i++) {
            long start = System.nanoTime();
            result = isFakePrime(n);
            long end = System.nanoTime();
            totalTime += (end - start);
        }

        double averageTime = totalTime / 10_000;

        System.out.println("Output: " + result);
        System.out.println("Average Time: " + averageTime + " ns\n");
    }
}
