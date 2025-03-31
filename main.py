# print("calculo de IMC")

# print("==================")
# print("")
# nome = input('escreva seu nome: ')
# peso = input('fale seu peso: ')
# altura = input('fale sua altura: ')
# idade = input("digite sua idade: ")

# imc = float(peso) / float(altura)**2

# print("===================")
# print("")
# print("sua nome e",nome)
# print("seu peso e",peso)
# print("sua altura e",altura)
# print("sua idade e",idade)

# print(f'seu imc é {imc:.2f}')

# if imc < 18.5:
#     print("baixo peso")

# elif imc >= 18.5 and imc < 24.99:
#     print("normal")

# elif imc >= 25 and imc <=29.99:
#     print("sobrepeso")

# elif imc >30:
#     print("obesidade")  





#----------------------------------------------------------



# ingressos = 50
# compradores = 250

# tem_ingresso_suficiente = (ingressos >=compradores)
# print(tem_ingresso_suficiente)


#----------------------------------------------------------

# lista_numeros = [1, 2, 3]

# print(lista_numeros[0])
# print(lista_numeros[1])
# print(lista_numeros[2])
 

#----------------------------------------------------------

notas=[]

contador = 1

while contador <= 3:
    codigo_aluno = input('Rm: ')
    nota = float(input('Nota: '))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    contador=contador + 1

    print("quantidade de notas: ", len(notas))