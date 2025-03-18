import time
from algorithms.sorting_strategy import SortingStrategy
from algorithms.bubble_sort import BubbleSort
from algorithms.quick_sort import QuickSort
from algorithms.insertion_sort import InsertionSort
from algorithms.selection_sort import SelectionSort

# Função para carregar dados do arquivo
def carregar_dados(caminho):
    with open(caminho, 'r') as file:
        return [int(line.strip()) for line in file]

# Função para executar e medir desempenho de algoritmos
def executar_algoritmo(algoritmo: SortingStrategy, dados: list):
    inicio = time.time()
    algoritmo.sort(dados.copy())  # Evita modificar os dados originais
    fim = time.time()

    tempo_execucao = (fim - inicio) * 1000  # milissegundos
    print(f"{algoritmo.__class__.__name__}: Tempo de execução = {tempo_execucao:.2f} ms")

# Carregar os dados
dados = carregar_dados('data-generator/dados.txt')

# Lista de algoritmos a serem testados
algoritmos = [
    BubbleSort(),
    QuickSort(),
    InsertionSort(),
    SelectionSort()
]

# Executar cada algoritmo
for algoritmo in algoritmos:
    executar_algoritmo(algoritmo, dados)
