#Desafio
#Dada a letra N do alfabeto, nos diga qual a sua posição.

#Entrada
#Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).

#Saída
#Um único inteiro, que representa a posição da letra no alfabeto.


#|Exemplo de entrada:|      |Entrada de Saída:|
#|        C          |      |          3      |
#|        J          |      |         10      |
#|        Z          |      |         26      |
#|        A          |      |          1      |

letra = str(input()).upper()
valor = ord(letra)

print(valor-64)

# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto