#algoritmo -> sequencia de passos para execultar uma tarefa 


#3 estruturas possiveis no algoritmo

#1 - estrutural(sequncia de passos continuos)
#2 - condicional (decisão - vou execultar um script se X e outro se Y)
#3 - repetição - permite execultar varias vezes o mesmo codigo

# variaveis
# espaços de memoria qu pode armazenar dados para execulção de um processo

#int, (1 (valor)float, string e booleam
#int : armazem valores inteiros (10, 14, 999, 362)
#float : numeros decimais (1.2, 1.7, 3.98... valores quebrados)
#String: ("" ou '') cadeia de caracteres: "rua dos bobos n 0"são valotes literais, ou seja não fazem calculos. Ex, bruno, gustavo, kelvin, kaio, luiz, fernanda, nico
#"rua nome da rua , n0"
#regras-> uma string deve estar entre "",'',"house's Fer"
#boolean: (true ou false) é o poligrafo ele aceita dois valores true (verdadeiro) e false(falso)
#o paython tem a tipagem dinamica, ou seja ele entende
#apartir do valor o tipo variavel

#VARIAVEL
#curso = 15.00
#a varialvel "curso" recebe o valor "Manufatura Digital"

#print(type(curso))


#exibir -> comando print
#print("Olá eu sou seu .py")

#para conversar com o usuário uso o input
#altura = float(input("digite sua altura"))
#a variavel altura recebe o valor

#rint(f"sua altura é {altura}")
#exibir para mim a "FORMATAÇÃO"  do texto com o valor variavel

#nome = input("digite seu nome")
#sobrenome = input("digite seu sobrenome")
#print(nome + sobrenome)

# print("cadastro de uma pessoa")
# nome = input("digite seu nome")
# # idade = input("digite sua idade")
# endereco = input("digite seu endereco")
# cpf = input("digite seu cpf")
# distancia = input("digite a distancia percorrida no dia")
# anoNacimento = int(input("digite o ano do seu nacimento"))
# idade = 2024 - anoNacimento
# print(idade, cpf, nome, distancia, endereco)

#estrutura de algoritmo CONDICIONAL
#execulto alguma instrução de acordo com os dados que tenho. Por exemplo, só posso me alistar no exercito
# se for maior de idade
#Para usar IF ou Else, eu tenho que saber quais opções que tenho!

# if(idade>= 18):
# # se a idade for maior ou igual a 18. ENTÃo exiba a mensagem
#     print("você já pode se alistar")
# else:
# #se a idade não for maior ou igual a 18 ENTÃO(:) exiba a mensagem
#     print("você é menor de idade")    

nota = float(input("Nota 1"))

if(nota > 5):
    print("Você está aprovado")
elif(nota == 5):
    print("Chama os pais , porque vc está no conselho")
else:
    print("Você está reprovado")

