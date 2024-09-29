/*
Problema M

Eleição

As eleições municipais estão chegando e o prefeito de Fatecalandia quer construir postinhos de saúde pela
cidade para conseguir se eleger! Ele pede para o secretário da Saúde da cidade para organizar isto. Temos
várias localidades onde podem ser instalados os postinhos de saúde, cada localidade tem um custo de construção
e a quantidade de pessoas atendidas. No entanto, a verba disponível para isto é escassa e o prefeito
quer que sejam construídos os postinhos de saúde que atendam o maior número de pessoas, mas que respeitem
a verba dada!

Entrada
Um número inteiro V (1 ≤ V ≤ 10000) que representa a verba disponível, um número N (1 ≤ N ≤ 100)
que representa a quantidade de localidades e três números que representam o local (1 ≤ L ≤ 100), o custo
de construção (1 ≤ C ≤ 1000) e o número de pessoas atendidas (1 ≤ P ≤ 10000).

Saída
A quantidade máxima de pessoas que poderão ser atendidas com a construção dos postos de saúde, considerando,
é claro, a melhor combinação conforme o limite de verba.

Exemplo de Entrada 1
    100
    10
    1 40 5
    2 30 45
    3 10 67
    4 23 12
    5 26 11
    6 11 23
    7 14 23
    8 50 33
    9 2 3
    10 1 100

Exemplo de Saída 1
    273
*/

import static java.lang.Math.max;
import static java.lang.System.in;
import static java.lang.System.out;

// Função para calcular a máxima quantidade de pessoas atendidas com a verba disponível
public static int maxPessoasAtendidas(int verba, int n, int[] custo, int[] pessoasAtendidas) {
    int[] dp = new int[verba + 1];

    // Resolvendo o problema da mochila
    for (int i = 1; i <= n; i++) {
        for (int j = verba; j >= custo[i]; j--) {
            dp[j] = max(dp[j], dp[j - custo[i]] + pessoasAtendidas[i]);
        }
    }

    return dp[verba]; // Retorna a máxima quantidade de pessoas atendidas com a verba disponível
}

// Função para realizar a leitura dos dados de entrada
public static int[] lerDados(Scanner entrada, int n) {
    int[] dados = new int[n * 2 + 1]; // Armazena custo e pessoasAtendidas consecutivamente

    // Leitura das localidades, seus custos e pessoas atendidas
    for (int i = 1; i <= n; i++) {
        entrada.nextInt();// Ignorado, pois não é utilizado
        dados[i * 2 - 1] = entrada.nextInt();  // Custo de construção do postinho
        dados[i * 2] = entrada.nextInt();      // Quantidade de pessoas atendidas
    }

    return dados;
}

public static void main(String[] ignoredArgs) {
    Scanner sc = new Scanner(in);

    int[] dados, custo, pessoasAtendidas;
    int verba, n;

    // Leitura da verba disponível e do número de localidades
    verba = sc.nextInt();
    n = sc.nextInt();

    // Leitura dos dados de entrada
    dados = lerDados(sc, n);

    // Separando os arrays de custo e pessoas atendidas
    custo = new int[n + 1];
    pessoasAtendidas = new int[n + 1];

    for (int i = 1; i <= n; i++) {
        custo[i] = dados[i * 2 - 1];
        pessoasAtendidas[i] = dados[i * 2];
    }

    // Chama a função e imprime a quantidade máxima de pessoas atendidas
    out.println(maxPessoasAtendidas(verba, n, custo, pessoasAtendidas));

    sc.close();
}
