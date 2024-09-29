public class D {
    /*
    Problema D
    Rotação

    A empresa GeoFatec trabalha com Geoprocessamento e necessita de um programa que seja capaz de rotacionar
    uma figura. Ou seja, dado um conjunto de pontos no plano cartesiano, o programa seja capaz de
    rotacionar a figura conforme o grau dado. Sabemos que para rotacionar uma figura necessitamos de
    uma matriz de rotação dada por:
    Onde θ é dado em graus
    Dado um conjunto de pontos encontre as novas coordenadas dos pontos. Considerar pi=3,1415

    Entrada
    Uma linha contendo um número inteiro N (1 ≤ N ≤ 100) e um ângulo θ (0 ≤ θ ≤ 180) em graus que
    representam o número de pontos da figura e o quanto se quer rotacionar a figura e a seguir as N coordenadas
    da figura (x, y) (−1000 ≤ x, y ≤ 1000)
    Saída
    Imprima as novas coordenadas (x, y) da figura rotacionada com duas casas decimais

    Exemplo de Entrada1
    5 40
    20 50
    10 50
    35 75
    -5 -7
    -2 4
    Exemplo de Saída 1
    -16.82 51.16
    -24.48 44.73
    -21.40 79.95
    0.67 -8.58
    -4.10 1.78

    Exemplo de Entrada2
    3 100
    20 250
    35 4
    66 50
    Exemplo de Saída2
    -249.68 -23.70
    -10.02 33.77
    -60.70 56.32

    Exemplo de Entrada3
    2 30
    100 5
    55 35
    Exemplo de Saída3
    84.10 54.33
    30.13 57.81
     */

    public static void main(String[] args) {
        int n = 5;
        int angulo = 40;
        int[][] pontos = {{20, 50}, {10, 50}, {35, 75}, {-5, -7}, {-2, 4}};
        testRotacionaFigura(n, angulo, pontos);

        int n2 = 3;
        int angulo2 = 100;
        int[][] pontos2 = {{20, 250}, {35, 4}, {66, 50}};
        testRotacionaFigura(n2, angulo2, pontos2);

        int n3 = 2;
        int angulo3 = 30;
        int[][] pontos3 = {{100, 5}, {55, 35}};
        testRotacionaFigura(n3, angulo3, pontos3);
    }

    public static String rotacionaFigura(int n, int angulo, int[][] pontos) {
        StringBuilder resultado = new StringBuilder();
        final double PI = 3.1415;
        double anguloRadianos = angulo * PI / 180;

        for (int i = 0; i < n; i++) {
            double novoX = pontos[i][0] * Math.cos(anguloRadianos) - pontos[i][1] * Math.sin(anguloRadianos);
            double novoY = pontos[i][0] * Math.sin(anguloRadianos) + pontos[i][1] * Math.cos(anguloRadianos);

            // Adiciona as novas coordenadas formatadas ao resultado
            resultado.append(String.format("%.2f %.2f\n", novoX, novoY));
        }

        return resultado.toString();
    }

    public static void testRotacionaFigura(int n, int angulo, int[][] pontos) {
        System.out.println("Input:");
        System.out.println(n);
        System.out.println(angulo);

        for (int i = 0; i < n; i++)
            System.out.println(pontos[i][0] + " " + pontos[i][1]);

        long startTime = System.nanoTime();
        String result = rotacionaFigura(n, angulo, pontos);
        long endTime = System.nanoTime();

        System.out.println("Output: ");
        System.out.println(result);
        System.out.println("Time: " + (endTime - startTime) + " ns\n");
    }
}
