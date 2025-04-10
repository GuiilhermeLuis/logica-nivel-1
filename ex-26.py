vetor = []
# Aqui, criamos uma lista vazia chamada vetor. Ele guarda os 5 ou + numeros digitados pelo usuario
for i in range(5):
# O laço for vai repetir 5 vezes(de i = 0 até i = 4)
    numero = int(input("Digite o {i+1} numero: "))
# O {i+1} é só para mostrar a contagem de forma amigável (de 1 a 5)
    vetor.append(numero) 
# Adiciona o número digitado no final da lista vetor
print("Os numeros informados foram:")
for numero in vetor:
# Pecorre a lista vetor elemento por elemento
    print(numero)
