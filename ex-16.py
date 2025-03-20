quantidade = float(input("QUANTIDADE DE MAÇÃS COMPRADAS?:"))
if quantidade <= 12:
    preco_por_maca = 1.30
else:
    preco_por_maca = 1.00
total = quantidade * preco_por_maca
print("O CUSTO TOTAL É R$", total)
