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

# notas=[]

# contador = 1

# while contador <= 3:
#     codigo_aluno = input('Rm: ')
#     nota = float(input('Nota: '))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)

#     contador=contador + 1

#     print("quantidade de notas: ", len(notas))


#----------------------------------------------------------


# valor1 = int(input('digite um valor: '))
# valor2 = int(input('digite outro valor: '))

# if valor1 > valor2:
#     print(f'{valor1} é maior que {valor2}') 
# else:
#     print(f'{valor2} é maior que {valor1}')




#----------------------------------------------------------





# nome = input("Digite seu nome: ")
# encontrar = input("Digite o que deseja encontrar: ")

# if encontrar in nome:
#     print(f'{encontrar} esta em {nome}')
# else:
#     print(f'{encontrar} nao esta em {nome}')


#--------------------------------------------------------------

# nome = 'vitor'
# preco = 1000.454775
# variavel ='%s, o preco é R$%.2f ' %(nome, preco)
# print(variavel)
# print("o hexadecimal de %d é %x" %(100,100))
    



#--------------------------------------------------------------



# nome=input("Digite seu nome: ")
# idade=input("digite sua idade: ")

# if nome and idade:
#     print(f'seu nome é: {nome}')
#     print(f'sua idade é: {idade}')
#     print(f'seu nome invertido é :{nome[::-1]}')
        
#     if ' ' in nome:
#         print("seu nome contem espacos")
#     else:
#         print("seu nome nao contem espacos")
        

#     print(f'a primeira letra do seu nome é: {nome[0]}')
#     print(f'a ultima letra do seu nome é: {nome[-1]}')
#     print(f'seu nome tem {len(nome)} letras')
# else:
#     print("nada foi digitado")



#--------------------------------------------------------------


# numero_str = input('vou dobrar o numero que voce digitar: ')

# try:
#      print('STR: ', numero_str)
#      numero_float = float(numero_str)
#      print("FLOAT: ", numero_float)
#      print(f'o dobro de {numero_str} é {numero_float * 2}')
# except:
#      print("isso nao é um numero")



#--------------------------------------------------------------




# velocidade = 61  # velocidade atual do carro
# local_carro = 100  # local em que o carro está na estrada
 
# RADAR_1 = 60  # velocidade máxima do radar 1
# LOCAL_1 = 100  # local onde o radar 1 está
# RADAR_RANGE = 1  # A distância onde o radar pega
 


# vel_carro_pass_radar_1 = velocidade > RADAR_1

# carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

# carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1


 
# if vel_carro_pass_radar_1:
#     print('Velocidade carro passou do radar 1')

# if carro_passou_radar_1:
#     print('Carro passou radar 1')
 
# if carro_multado_radar_1:
#     print('carro multado em radar 1')



#----------------------------------------------------------------------------------



# entrada = input('Digite um numero inteiro: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)

#     if entrada_int %2 == 0:
#         print("o numero é par")

#     elif entrada_int %2 == 1:
#         print("o numero é impar")

# else:
#     print("voce nao digitou um numero inteiro")



#----------------------------------------------------------

# nome = input('Escreva seu primeiro nome: ')

# if  len(nome) <= 4:
#     print("Seu nome é curto")
# elif len(nome) == 5 or len(nome) == 6:
#     print("seu nome é normal")
# elif len(nome) > 6:
#     print("seu nome é muito grande") 


#----------------------------------------------------------

# entrada = input("digite a hora em numero float: ")

# try:
#     hora = float(entrada)

#     if hora >= 0 and hora <=11:
#         print("bom dia")

#     elif hora >=12 and hora <=17:
#         print("boa tarde")

#     elif hora >=18 and hora <=23:
#         print("boa noite")
#     else:
#         print("nao conheço essa hora")
# except:
#     print("voce nao digitou um numero float")    


#----------------------------------------------------------

# condicao = True

# while condicao:
#     nome = input('Escreva seu nome: ')
#     print(f'Seu nome é {nome}')

#     if nome == 'sair' or nome == 'Sair' or nome == 'SAIR':
#         print("acabou")

#         break


#------------------------------------------------------------------

# contador = 0

# while contador < 10:
#     # contador = contador + 1
#     contador  += 1

#     print(contador)

# print('acabou')


#------------------------------------------------------------------


# contador = 0

# while contador < 100:
#     contador  += 1

#     if contador ==6:
#         continue

#     if contador >=10 and contador <=27:
#         continue


#     print(contador)



#     if contador == 40:
#         break

# print('acabou')



#------------------------------------------------------------------

# qtd_linhas = 5
# qtd_colunas = 5

# linha =1
# while linha <= qtd_linhas:
#     coluna =1

#     while coluna <= qtd_colunas:
#         print(f'{linha=}{coluna=}')
#         coluna +=1

#     linha +=1

# print("acabou")


#------------------------------------------------------------------

# nome = 'Vitor Gomes'

# indice = 0 
# novo_nome = ''

# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice +=1


# print(novo_nome)



#----------------------------------------------------------------------






# while True:

#     numero1 = input('Digite o primeiro numero: ')
#     numero2 = input('Digite o segundo numero: ')
#     operador = input('Digite o operador (+-/*): ')

#     numeros_validos = False
   
#     try:
#         numero1_float = float(numero1)
#         numero2_float = float(numero2)
#         numeros_validos = True

#     except ValueError:
#         print("Um ou ambos os numeros sao invalidos")
#         continue

#     operadores_permitidos = '+-/*'

#     if operador not in operadores_permitidos:
#         print("operador invalido")
#         continue

#     if len(operador) > 1:
#         print("digite apenas 1 operador")
#         continue




#     if operador == '+':
#         resposta = numero1_float + numero2_float

#     elif operador == '-':
#         resposta = numero1_float - numero2_float

#     elif operador == '/':
#         resposta = numero1_float / numero2_float

#     elif operador == '*':
#         resposta = numero1_float * numero2_float

#     print(f'{numero1_float} {operador} {numero2_float} = {resposta}')            




#     sair = input('Quer sair? [s]im: ').lower().startswith('s')

#     if sair is True:
#         print('saiu')
#         break



#----------------------------------------------------------------------



# frase = 'o python é uma linguagem de programaçao. O python foi criado por um cara'

# indice = 0
# maior_frequencia = 0
# letra_mais_frequente = ''

# while indice < len(frase):
#     letra_atual = frase[indice]

#     if letra_atual == ' ':
#         indice += 1
#         continue

#     frequencia_atual = frase.count(letra_atual)

#     if maior_frequencia < frequencia_atual:
#         maior_frequencia = frequencia_atual
#         letra_mais_frequente = letra_atual

#     indice += 1

# print(f'A letra que apareceu mais vezes foi "{letra_mais_frequente}" que apareceu {maior_frequencia}x')


#------------------------------------------------------------

# texto = 'vitor'
# nv_txt = ''

# for letra in texto:
#     nv_txt += f'*{letra}'
# print(nv_txt)



#---------------------------------------

# numeros =  range(0, 100, 5)

# for numero in numeros:
#     print(numero)



#---------------------------------------


# for i in range(10):
#     if i == 2:
#         print('i é 2, pulando...')
#         continue

#     if i == 8:
#         print('i é 8, seu else nao executara')
#         break

#     for j in range(1, 3):
#         print(i, j)

# else:
#     print("For completo com sucesso")


#---------------------------------------


# palavra_secreta = 'vitor'
# letras_acertadas = ''
# tentativa = 0

# while True:

#     letra_digitada = input('Digite uma letra: ')
#     tentativa += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas 1 letra')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas = letras_acertadas + letra_digitada


#     palavra_formada = ''
        
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada = palavra_formada + letra_secreta
#         else:
#             palavra_formada = palavra_formada + '*'

#     print('palavra_formada: ', palavra_formada)

#     if palavra_formada == palavra_secreta:

#         print("parabens voce acertou")       
#         print(f'a palavra era:', palavra_secreta) 
#         print(f'tentativas: ', tentativa)

        
#         letras_acertadas = ''
#         tentativa = 0

#-----------------------------------------------------------------


#----------------------------------------------

# # Criando uma lista inicial
# lista = [1, 2, 3]

# # append - Adiciona um item ao final
# lista.append(4)
# print(lista)  # [1, 2, 3, 4]

# # insert - Adiciona um item no índice escolhido
# lista.insert(1, 9)
# print(lista)  # [1, 9, 2, 3, 4]

# # pop - Remove do final ou do índice escolhido
# lista.pop()
# print(lista)  # [1, 9, 2, 3]

# lista.pop(1)  # Remove o item no índice 1
# print(lista)  # [1, 2, 3]

# # del - Apaga um índice
# del lista[1]
# print(lista)  # [1, 3]

# # clear - Limpa a lista
# lista.clear()
# print(lista)  # []

# # extend - Estende a lista
# lista.extend([5, 6, 7])
# print(lista)  # [5, 6, 7]


#----------------------------------------------

# lista = ['maria', 'vitor' , 'pedro']
# for nome in lista:
#     print(nome, type(nome))

#----------------------------------------------

# lista = ['maria', 'vitor' , 'pedro']
# indices = range(len(lista))

# for indice in indices:
#     print(indice, lista[indice])


#----------------------------------------------

# numeros = [10, 15, 22, 33, 40, 55, 60, 77, 90]


# for numero in numeros:
#     if numero % 2 ==0:
#         print(f'o numero {numero}  é par')
    
#     else: 
#         print(f'o numero {numero} é impar')

#----------------------------------------------

# lista = ['Maria', 'vitor', 'pedro']
# lista.append('joao')


# for indice, nome in enumerate(lista, start=1):
#     print(indice, nome)



#----------------------------------------------
lista = []

while True:
    comando = input('Selecione uma opção: [I]nserir  [A]pagar  [L]istar  [S]air: ').strip().lower()



    if comando == 'i':
        item = input('Digite o item a ser inserido: ')
        lista.append(item)



    elif comando == 'a':
        
        if lista:
            try:
                indice = int(input('Digite o número do item para apagar: ')) - 1  
                if 0 <= indice < len(lista):
                    lista.pop(indice)
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite um número válido.")
        else:
            print("Nada para apagar.")



    elif comando == "l":
        if lista:
            print("\nLista de itens:")
            for i, item in enumerate(lista, start=1):  
                print(f"{i}. {item}")
        else:
            print("A lista está vazia.")



    elif comando == "s":
        print("Saindo...")
        break  



    else:
        print("Comando inválido. Digite I, A, L ou S.")

    print(lista)  


