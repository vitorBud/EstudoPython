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
# lista = []

# while True:
#     comando = input('Selecione uma opção: [I]nserir  [A]pagar  [L]istar  [S]air: ').strip().lower()



#     if comando == 'i':
#         item = input('Digite o item a ser inserido: ')
#         lista.append(item)



#     elif comando == 'a':
        
#         if lista:
#             try:
#                 indice = int(input('Digite o número do item para apagar: ')) - 1  
#                 if 0 <= indice < len(lista):
#                     lista.pop(indice)
#                 else:
#                     print("Número inválido.")
#             except ValueError:
#                 print("Digite um número válido.")
#         else:
#             print("Nada para apagar.")



#     elif comando == "l":
#         if lista:
#             print("\nLista de itens:")
#             for i, item in enumerate(lista, start=1):  
#                 print(f"{i}. {item}")
#         else:
#             print("A lista está vazia.")



#     elif comando == "s":
#         print("Saindo...")
#         break  



#     else:
#         print("Comando inválido. Digite I, A, L ou S.")

#     print(lista)  


#---------------------------------------------------------------------------

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
# lista = []

# while True:
#     comando = input('Selecione uma opção: [I]nserir  [A]pagar  [L]istar  [S]air: ').strip().lower()



#     if comando == 'i':
#         item = input('Digite o item a ser inserido: ')
#         lista.append(item)



#     elif comando == 'a':
        
#         if lista:
#             try:
#                 indice = int(input('Digite o número do item para apagar: ')) - 1  
#                 if 0 <= indice < len(lista):
#                     lista.pop(indice)
#                 else:
#                     print("Número inválido.")
#             except ValueError:
#                 print("Digite um número válido.")
#         else:
#             print("Nada para apagar.")



#     elif comando == "l":
#         if lista:
#             print("\nLista de itens:")
#             for i, item in enumerate(lista, start=1):  
#                 print(f"{i}. {item}")
#         else:
#             print("A lista está vazia.")



#     elif comando == "s":
#         print("Saindo...")
#         break  



#     else:
#         print("Comando inválido. Digite I, A, L ou S.")

#     print(lista)  

#-----------------------------------------------------------------------

# cpf_enviado_usuario = '74682489070'

# nove_digitos = cpf_enviado_usuario[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0

# for digito in nove_digitos:
#     resultado_digito_1 += int(digito) * contador_regressivo_1
#     contador_regressivo_1 -= 1

# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# dez_digitos = nove_digitos + str(digito_1)
# contador_regressivo_2 = 11

# resultado_digito_2 = 0
# for digito in dez_digitos:
#     resultado_digito_2 += (int(digito) * contador_regressivo_2)
#     contador_regressivo_2 -= 1

# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_1 <= 9 else  0

# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
#     print(f'{cpf_gerado_pelo_calculo} é valido')

# else:
#     print("invalido")

#------------------------------------------------------------------------


# def imprimir(a, b, c):
#     print(a, b, c)
   
# imprimir(1,2,3)
# imprimir(4,5,6)

#---------------------------------------

# def saudacao(nome = 'estranho'):
#     print(f'ola {nome}!')

# saudacao("vitor")
# saudacao("maria")
# saudacao()



#---------------------------------------

# def multiplo_de(numero, multiplo):
#     resultado = numero % multiplo == 0
#     print(f'{numero} é múltiplo de {multiplo}?', end=' ')
#     print(resultado)
 
 
# multiplo_de(16, 8)
# multiplo_de(15, 3)
# multiplo_de(10, 2)

#------------------------------------------------



# valor1 = int(input('digite um valor: '))
# valor2 = int(input('digite outro valor: '))

# if valor1 > valor2:
#     print(f'{valor1} é maior que {valor2}') 
# else:
#     print(f'{valor2} é maior que {valor1}')


#------------------------------------------------


# def seloko():
#     x = 1
#     def seloko2():
#         x=10
#         y=20
#         print(x,y)
#     print(x)
#     seloko2()

# seloko()

#------------------------------------------------

# def soma (x,y):
#     return x + y

# soma1 = soma(1,1)
# soma2 = soma(2,2)

# print(soma1 + soma2)


#------------------------------------------------

# def multiplicar(*args):
#     total = 1
#     for numero in args:
#         total*= numero
#     return total

# multiplicacao = multiplicar(1,2,3,4,5)
# print(multiplicacao)

#------------------------------------------------

# def verificar(numero):

#     if numero % 2 == 0:
#         return "par"
#     else:
#         return "impar"
    
# cont_par = 0
# cont_impar = 0

# while True:
#     numero = int(input("Digite um numero(digite 0 para sair): "))
#     if numero == 0:
#         break

#     resultado = verificar(numero)
#     print("Resultado:", resultado)

#     if resultado == "par":
#         cont_par += 1
#     else:
#         cont_impar += 1

# print("\nQuantidade de pares:", cont_par)
# print("Quantidade de ímpares:", cont_impar)
    
    
#------------------------------------------------

# def verificar(numero):

#     if numero % 2 == 0:
#         return "par"
#     else:
#         return "impar"

# while True:
#     numero = int(input("Digite um numero(digite 0 para sair): "))
#     if numero == 0:
#         break
#     print("resultado:", verificar(numero))


#------------------------------------------------

# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}'
#     return saudar

# s1 = criar_saudacao ('Bom dia')
# s2 = criar_saudacao ('Boa noite')

# print(s1("vitor"))
# print(s2("maria"))
 

#------------------------------------------------

# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar

# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# print(duplicar(4))
# print(triplicar(5))


#------------------------------------------------

# pessoa = {}

# pessoa['nome'] = 'vitor'
# print(pessoa)

#------------------------------------------------



# perguntas = [
#     {
#         'pergunta': 'quanto é 2+2?',
#         'Opçoes': ['1', '3', '4', '5'],
#         'resposta_certa': "4"
#     },
#     {
#         'pergunta': 'quanto é 5*5?',
#         'Opçoes': ['25', '10', '45', '50'],
#         'resposta_certa': "25"
#     },
#     {
#         'pergunta': 'Quanto e 10/2?',
#         'Opçoes': ['10', '0', '2', '5'],
#         'resposta_certa': "5"
#     }
# ]


# for pergunta in perguntas:
#     print('Pergunta:',pergunta['pergunta'])
#     print()


#     opcoes = pergunta['Opçoes']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)

#     print()

#     resposta = input('escolha uma opção: ')

#     acertou = False
#     resposta_int = None
#     qtd_opcoes = len(opcoes)

#     if resposta.isdigit():
#         resposta_int = int(resposta)

#     if resposta_int is not None:
#         if resposta_int >= 0 and resposta_int < qtd_opcoes:
#             if opcoes[resposta_int] == pergunta['resposta_certa']:
#                 acertou = True

#     if acertou:
#         print('Você acertou!')
#     else:
#         print('Você errou!')

#     print()

#     print('----------------------------------')
#     print()

#-------------------------------------------------------

# s1 = set()
# s1.add('Vitor')
# s1.add(1)
# print(s1)


#-------------------------------------------------------

# letras = set()
# while True:
#     letra = input('Digite uma letra: ')
#     letras.add(letra)

#     if 'l' in letras:
#         print("saiu")
#         break

#     print(letras)


#-------------------------------------------------------


# lista_de_listas_de_inteiros = [
#     [1, 2, 3,4,5,6],
#     [4, 5, 4, 7, 5, 9],
#     [7, 8, 9, 7, 12, 15],
#     [10, 11, 12, 12, 12],
#     [13, 14, 15, 10, 9],
#     [16, 17, 18, 16, 17],
# ]

# def encontrar_primeiro_duplicado(lista_de_inteiros):
#     numeros_checados = set()
#     primeiro_duplicado = -1

#     for numero in lista_de_inteiros:
#         if numero in numeros_checados:
#            primeiro_duplicado = numero
#            break

#         numeros_checados.add(numero)


#     return primeiro_duplicado


# for lista in lista_de_listas_de_inteiros:
#     print(lista, encontrar_primeiro_duplicado(lista))
#     print('----------------------------------')



#-------------------------------------------------------

# pessoa = {
#     'nome': 'vitor',
#     'sobrenome': 'gomes',
# }
# a, b = pessoa.values()
# print(a, b)


#-------------------------------------------------------

# lista = [numero * 2 for numero in range(10)]
# print(lista)

#-------------------------------------------------------

# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))
# lista = [

#     (x, y)
#     for x in range(3)
#     for y in range(3)
# ]
# lista = [
#     [letra for letra in 'vitor']
#     for x in range(3)
# ]

# print(lista)



#-------------------------------------------------------

# import copy

# produtos = [
#     {'nome': 'produto1', 'preco': 10.20},
#     {'nome': 'produto2', 'preco': 9.00},
#     {'nome': 'produto3', 'preco': 102.00},
#     {'nome': 'produto4', 'preco': 14.00},
#     {'nome': 'produto5', 'preco': 11.00},
# ]

# novos_produtos = [

#     {**p, 'preco': round(p['preco'] *1.1 )}
#     for p in copy.deepcopy(produtos)
# ]

# print(*produtos, sep='\n')
# print('----------------------------------')
# print(*novos_produtos, sep='\n')
# print('----------------------------------')


#-------------------------------------------------------


# # Funções básicas de operação
# def soma(x, y=0):
#     return x + y

# def multiplica(x, y=1):
#     return x * y

# # Função para executar qualquer função com múltiplos argumentos
# def criar_funcao(funcao, *args):
#     return funcao(*args)

# # Testando as funções
# soma_com_cinco = criar_funcao(soma, 5, 10)  # 5 + 10 = 15
# multiplica_por_dez = criar_funcao(multiplica, 10, 2)  # 10 * 2 = 20

# print(f"Resultado da soma: {soma_com_cinco}")
# print(f"Resultado da multiplicação: {multiplica_por_dez}")



#-------------------------------------------------------

# def zipper(lista1, lista2):

#     tamanho_menor_lista = min(len(lista1), len(lista2))

#     resultado = []

#     for i in range(tamanho_menor_lista):
#         par = (lista1[i], lista2[i])
#         resultado.append(par)
    
#     return resultado

# lista1 = ['Brasilia', 'Bahia', 'Brasil']
# lista2 = ['Bsb', 'Ba', 'BR']

# print(zipper(lista1, lista2))
# print('----------------------------------')

#-------------------------------------------------------

# def zipper(lista1, lista2):
#     # Usando zip para unir os elementos das listas
#     return list(zip(lista1, lista2))

# lista1 = ['Brasilia', 'Bahia', 'Brasil']
# lista2 = ['Bsb', 'Ba', 'BR']

# print(zipper(lista1, lista2))
# print('----------------------------------')


#-------------------------------------------------------

# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]

# tamanho_menor_lista = min(len(lista_a), len(lista_b))

# lista_soma = []

# for i in range(tamanho_menor_lista):
#     soma = lista_a[i] + lista_b[i]
#     lista_soma.append(soma)

# print(lista_soma)



#-------------------------------------------------------


# class Carro:
#     def __init__(self, nome):
#         self.nome = nome
        
#     def acelerar(self):
#         print(f'{self.nome} está acelerando!')

# fusca = Carro("Fusca")
# print(fusca.nome)
# fusca.acelerar()

# celta = Carro("Celta")
# print(celta.nome)
# celta.acelerar()


#-------------------------------------------------------


# class Animal:
#     def __init__(self, nome):
#         self.nome = nome

#     variavel = 'valor'
#     print(variavel)

#     def comendo(self, alimento):
#         print(f'{self.nome} está comendo {alimento}')

# leao = Animal('Leão')
# print(leao.nome)
# leao.comendo('carne')


#-------------------------------------------------------

# class Pessoa:
#     ano_atual = 2025

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def get_ano_nascimento(self):
#         return Pessoa.ano_atual - self.idade
    
# p1 = Pessoa('Vitor', 20)
# p2 = Pessoa('Maria', 30)
# print(f'{p1.nome} nasceu em {p1.get_ano_nascimento()}')


#-------------------------------------------------------

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protegido = 'isso é protegido'

    def metodo_publico(self):
        self._metodo_protegido()
        print(self._protegido)
        return 'metodo público'
    
    def _metodo_protegido(self):
        print('metodo_protegido')
        return 'metodo_protegido'

f = Foo()

print(f.metodo_publico())


#-------------------------------------------------------











