#Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu carro faz 12 KM/L.\n
#Como ele não sabe fazer um programa que o auxilie nessa missão, ele te pede ajuda. Para efetuar o cálculo, deve-se fornecer o tempo gasto em horas na viagem e a velocidade média durante a mesma em km/h.\n
#Assim, você conseguirá passar para Rubens qual a distância percorrida e, em seguida, calcular quantos litros serão necessários para a viagem que ele quer fazer. Mostre o valor com 3 casas decimais após o ponto.

#Entrada
#O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem em horas e o segundo é a velocidade média durante a mesma em km/h.

#Saída
#Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal.


#|Exemplo de entrada:|      |Entrada de Saída:|
#|     10 85         |      |      70.833     |
#|     22 67         |      |      122.833    |


valores = input().split()

# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal

tempo = int(valores[0])
velocidade = int(valores[1])

litros = velocidade / 12

resultado = tempo * litros

print(f"{resultado:.3f}")
