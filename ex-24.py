senha_correta = 4002  # Definindo a senha correta
senha = int(input("Digite a senha: "))  # Solicita a senha ao usuário

while senha != senha_correta:
    print("A senha está incorreta. Repita por favor.")
    senha = int(input("Digite a senha: "))  # Solicita novamente a senha

print("Senha correta!")
