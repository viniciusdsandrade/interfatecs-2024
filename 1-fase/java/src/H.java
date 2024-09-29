import java.util.Arrays;

public class H {
    /*
        Problema H
        Quem é o pivô?

        Zequinha está estudando métodos de ordenação na escola e ficou muito empolgado com o Quick Sort,
    devido à sua rapidez. Fez até uma implementação em sua linguagem de programação favorita. Pesquisando
    um pouco mais sobre os detalhes de implementação, ficou sabendo que a escolha do valor de referência
    utilizado para processar uma partição dos dados, o famoso pivô, é um aspecto crítico para o desempenho.
    Se uma implementação descuidada do metodo tiver o azar de encontrar sequências particularmente ruins de
    pivôs em uma ordenação, o desempenho será degradado a ponto de, no limite, o Quick Sort se comparar
    com o Bubble Sort. Claro que isso seria um caso extremo para alguém muito azarado, mas esse alerta foi
    suficiente para que Zequinha resolvesse melhorar sua escolha de pivôs. Dentre várias abordagens possíveis,
    ele se interessou pela que escolhe três valores contidos na partição a ser processada e seleciona como pivô
    aquele valor que não seja sozinho nem o menor, nem o maior dos três. Por exemplo, entre os valores 23, 42
    e 37, o pivô a ser escolhido por esse metodo seria o 37; para os valores 15, 30 e 15, o escolhido teria que
    ser o 15 mesmo, dada a repetição. Sua tarefa é ajudar seu amigo Zequinha a determinar o valor do pivô com
    base em 3 valores inteiros fornecidos para análise.

    Entrada
    A entrada é composta por 3 inteiros separados por espaço em branco. Cada valor encontra-se na faixa que
    vai de -2000000000 até + 2000000000.

    Saída
    Imprimir o valor selecionado como pivô pelo critério exposto anteriormente.

    Entrada1  23 42 37
    Saída1   37

    Entrada2  15 30 15
    Saída2    15

    Entrada3  10 20 30
    Saída3    20
     */

    public static void main(String[] args) {
        testPivor(23, 42, 37);
        testPivor(15, 30, 15);
        testPivor(10, 20, 30);
    }

    public static int pivor(int a, int b, int c) {
        if (a > b && a < c || a < b && a > c) return a;
        else if (b > a && b < c || b < a && b > c) return b;
        else return c;
    }

    public static int pivor2(int a, int b, int c) {
        if ((a <= b && b <= c) || (c <= b && b <= a)) return b;
        else if ((b <= a && a <= c) || (c <= a && a <= b)) return a;
        else return c;
    }

    public static int pivor3(int a, int b, int c) {
        return Math.max(Math.min(a, b), Math.min(Math.max(a, b), c));
    }

    public static int pivor4(int a, int b, int c) {
        int[] array = {a, b, c};
        Arrays.sort(array);
        return array[1];
    }

    public static void testPivor(int a, int b, int c) {
        System.out.println("Input: " + a + " " + b + " " + c);

        double totalTime1 = 0, totalTime2 = 0, totalTime3 = 0, totalTime4 = 0;
        int result = 0, result2 = 0, result3 = 0, result4 = 0;
        double start, end, start2, end2, start3, end3, start4, end4;

        final long repeat = 10000000;

        for (int i = 0; i < repeat; i++) {
            start = System.nanoTime();
            result = pivor(a, b, c);
            end = System.nanoTime();

            start2 = System.nanoTime();
            result2 = pivor2(a, b, c);
            end2 = System.nanoTime();

            start3 = System.nanoTime();
            result3 = pivor3(a, b, c);
            end3 = System.nanoTime();

            start4 = System.nanoTime();
            result4 = pivor4(a, b, c);
            end4 = System.nanoTime();

            totalTime1 += (end - start);
            totalTime2 += (end2 - start2);
            totalTime3 += (end3 - start3);
            totalTime4 += (end4 - start4);
        }

        double averageTime1 = totalTime1 / repeat;
        double averageTime2 = totalTime2 / repeat;
        double averageTime3 = totalTime3 / repeat;
        double averageTime4 = totalTime4 / repeat;

        System.out.println("Output1:  " + result);
        System.out.println("Output2:  " + result2);
        System.out.println("Output3:  " + result3);
        System.out.println("Output4:  " + result4);
        System.out.printf("Average Time1: %.2f ns\n", averageTime1);
        System.out.printf("Average Time2: %.2f ns\n", averageTime2);
        System.out.printf("Average Time3: %.2f ns\n", averageTime3);
        System.out.printf("Average Time4: %.2f ns\n\n", averageTime4);
    }
}
