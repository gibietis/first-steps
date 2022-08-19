import math
#nbase é a quantidade de números que serão somados
print("""Insira quantos números você deseja somar. 
Pressione 'enter' para cada número adicionado. 
Adicione "0" para encerrar a inserção de novos números
""")
base = ["1", "3"]
baseconv = [int(x) for x in base]

while True:
    data = input()
    base.append(data)
    if data == "Sair":
        break
    

res = sum(baseconv)
print(res)

#for 
#if nbase < 2:
#    print("Você deve somar pelo menos dois números")
#    elif nbase => 2:

#n1 = int(input("Insira primeiro número a ser somado: "))
#def add2():
