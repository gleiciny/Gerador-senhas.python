import random
import string

# Função para gerar a senha
def gerar_senha(tamanho=8, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_letters  # Começa com letras maiúsculas e minúsculas
    if incluir_numeros:  # Adiciona números se solicitado
        caracteres += string.digits
    if incluir_simbolos:  # Adiciona símbolos se solicitado
        caracteres += string.punctuation

    # Gera a senha aleatória com o tamanho desejado
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Bloco principal do programa
if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha: "))  # Solicita o tamanho da senha
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'  # Pergunta sobre números
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'  # Pergunta sobre símbolos
    
    # Chama a função e exibe a senha gerada
    print("Sua senha gerada é:", gerar_senha(tamanho, incluir_numeros, incluir_simbolos))
