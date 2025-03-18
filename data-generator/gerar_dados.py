import random

def gerar_dados(quantidade, arquivo='dados.txt', valor_maximo=1000000):
    with open(arquivo, 'w') as file:
        for _ in range(quantidade):
            numero = random.randint(0, valor_maximo)
            file.write(f"{numero}\n")

# Exemplo de uso:
if __name__ == '__main__':
    tamanho = 10000  # pode alterar conforme necessidade
    gerar_dados(tamanho)
