```python
def gerar_dados(quantidade, arquivo='dados.txt', valor_maximo=1000000):
    with open(arquivo, 'w') as file:
        for _ in range(quantidade):
            numero = random.randint(0, valor_maximo)
            file.write(f"{numero}\n")
```

# Geração de dados

Para a geração de dados fora criada uma função tal que recebe os seguintes parâmetros

1. quantidade - sendo a quantidade de números que serão gerados
2. arquivo - nome do arquivo gerado
3. valor_maximo - valor maximo de cada numero gerado aleatoriamente

O metodo open abre um arquivo e garante que ele é fechado após seu uso
Então em um loop que roda "quantidade" vezes escrevemos um numero aleatorio no arquivo que vai de 0 a "valor_maximo" e pula linha a cada iteração
