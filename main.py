def gerar_senha(tamanho=8, incluir_numeros=True, incluir_simbolos=True):
    import random
    import string

    caracteres = string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha: "))
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
    print("Sua senha gerada é:", gerar_senha(tamanho, incluir_numeros, incluir_simbolos))
