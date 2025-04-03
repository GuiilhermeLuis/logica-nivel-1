numero1 = int(input("informe o primeiro numero:"))
numero2 = int(input("Informe o segundo numero:"))
numero3 = int(input("Informe o terceiro numero:"))

if numero1 > numero2 and numero1 > numero3:
   print("O primeiro numero é maior")
elif numero2 > numero1 and numero2 > numero3:
    print("O segundo numero é maior")
else:
    print("O terceiro numero é maior")
