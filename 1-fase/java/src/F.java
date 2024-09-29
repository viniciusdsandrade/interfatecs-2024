import java.util.regex.Pattern;

public class F {
    /*
        Problema F
        Valida Placas

        Josélio foi contratado como estagiário em uma empresa que presta serviços para um órgão público que
    cuida, entre outras coisas, do tráfego de veículos nas vias de trânsito de seu estado. E nosso amigo Josélio
    é um tipo meio orgulhoso, que gosta de contar vantagem sobre seus colegas de turma na faculdade. Depois
    que conseguiu esse estágio então, o cara está impossível, parece que é o salvador da pátria lá no setor dele
    e que sem ele nada lá funciona. Recentemente ele veio contando sobre um programa que teve que fazer
    para validar placas de automóveis captadas por sensores óticos. Quando seu grupo de amigos falou que ele
    estava sendo muito chato, ele desafiou os colegas a fazerem um programa como o que ele fez. Falou que se
    alguém conseguisse produzir um validador que funcionasse, ele pagaria lanche para a turma inteira. Você,
    obviamente, se viu na situação de calar a boca desse infeliz e, ainda por cima, fazer uma merenda nas costas
    dele. Então vamos aos detalhes. O Brasil teve, ao longo do tempo, várias especificações para as placas de
    veículos automotores e, neste problema, estamos interessados apenas nas placas de automóveis.

     1 - O primeiro modelo de algum interesse vigorou entre 1915 e 1941 e determinava que as placas teriam
        uma letra inicial seguida de uma sequência de 1 a 5 algarismos numéricos. A letra inicial poderia ser “A”, para automóveis
        de “aluguel” tais como táxis, caminhões e ônibus, ou então deveria ser “P”, indicando que se tratava de um veículo “particular”.
        Exemplo: “A234” ou “P12345”
        Contra-Exemplo: “123X45” ou “ABCD1” ou, ainda, “B234”.

    2 - Em um segundo momento, no período entre 1941 e 1969, as placas passaram a ser compostas apenas por uma
        sequência de até 7 dígitos numéricos.
        Exemplo: “533” ou “3949573”.

    3 - Uma posterior reformulação nas regras de trânsito implantou o modelo de placa veicular composta por
        duas letras seguidas de quatro dígitos numéricos, vigorando entre 1970 e 1990.
        Exemplo: “RX3429” e “CM9382”.

    4 - Entre 1990 e 2018 o formato de placas mudou novamente, passando a ser composto por
        três caracteres alfabéticos seguidos de quatro dígitos numéricos.
        Exemplo: “BTP3465” e “PWS9521”.

     5 - Finalmente passamos a utilizar a chamada “placa Mercosul”, que possui uma
        sequência inicial de três letras, seguidas por um dígito numérico, depois mais uma letra e finaliza com uma sequência de dois dígitos numéricos.

   O programa a ser desenvolvido por você para calar a boca do Josélio vai receber uma leitura do sensor na forma de uma string com até 50 caracteres
        de comprimento, contendo apenas letras em maiúsculas e dígitos numéricos. Nenhum outro tipo de caracter
        será encontrado nessa string, pois a coleta de dados já faz uma limpeza no conteúdo, removendo espaços
        em branco e eventuais pontuações presentes no registro.

        O programa deverá, para cada placa lida, indicar se ela é uma “Placa muito antiga” por atender ao formato vigente entre 1915 e 1941, ou se é uma “Placa
        numérica”, caso se enquadre no formato que vigorou entre 1941 e 1969, ou, se trata de uma “Placa AA-9999” que teve validade entre 1970 e 1990 ou, ainda, se for uma “Placa AAA-9999” que foi exigida entre
        1990 e 2018 ou, finalmente, se é uma “Placa Mercosul”.
        Se a placa lida não for nenhuma dessas, o programa deverá informar que se trata de uma “Placa invalida”.

    Entrada
    A entrada possui apenas uma string de até 50 caracteres úteis, composta por alguma combinação de letras
    maiúsculas e dígitos numéricos.

    Saída
    Para a placa lida o programa deverá imprimir uma das respostas previstas, conforme ilustram os casos de
    teste. As saídas não utilizam nenhum tipo de acentuação e devem ser impressas exatamente como constam

       Entrada1 A1234
       Saída1   Placa muito antiga

       Entrada2 12345
       Saída2   Placa numerica

       Entrada3 AB1234
       Saída3   Placa AA-9999

       Entrada4 ABC1234
       Saída4   Placa AAA-9999

       Entrada5 ABC1D34
       Saída5   Placa Mercosul

       Entrada6 X0S0X0X0009
       Saída6   Placa invalida
     */

    public static void main(String[] args) {
        testValidaPlaca("A1234");
        testValidaPlaca("12345");
        testValidaPlaca("AB1234");
        testValidaPlaca("ABC1234");
        testValidaPlaca("ABC1D34");
        testValidaPlaca("X0S0X0X0009");
    }

    private static final Pattern PLACA_MUITO_ANTIGA = Pattern.compile("[A|P][0-9]{1,5}");
    private static final Pattern PLACA_NUMERICA = Pattern.compile("[0-9]{1,7}");
    private static final Pattern PLACA_AA_9999 = Pattern.compile("[A-Z]{2}[0-9]{4}");
    private static final Pattern PLACA_AAA_9999 = Pattern.compile("[A-Z]{3}[0-9]{4}");
    private static final Pattern PLACA_MERCOSUL = Pattern.compile("[A-Z]{3}[0-9][A-Z][0-9]{2}");

    public static String validaPlaca(String placa) {
        if (PLACA_MUITO_ANTIGA.matcher(placa).matches()) return "Placa muito antiga";
        else if (PLACA_NUMERICA.matcher(placa).matches()) return "Placa numerica";
        else if (PLACA_AA_9999.matcher(placa).matches()) return "Placa AA-9999";
        else if (PLACA_AAA_9999.matcher(placa).matches()) return "Placa AAA-9999";
        else if (PLACA_MERCOSUL.matcher(placa).matches()) return "Placa Mercosul";
        else return "Placa invalida";
    }

    public static void testValidaPlaca(String placa) {
        System.out.println("Input: " + placa);

        long startTime = System.nanoTime();
        String result = validaPlaca(placa);
        long endTime = System.nanoTime();

        System.out.println("Output: " + result);
        System.out.println("Runtime: " + (endTime - startTime) + " ns\n");
    }
}
