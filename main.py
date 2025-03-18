import time
from algorithms.sorting_strategy import SortingStrategy
from algorithms.bubble_sort import BubbleSort
from algorithms.quick_sort import QuickSort

# Função para carregar dados do arquivo
def carregar_dados(caminho):
    with open(caminho, 'r') as file:
        return [int(line.strip()) for line in file]

# Função para executar e medir desempenho de algoritmos
def executar_algoritmo(algoritmo: SortingStrategy, dados: list):
    inicio = time.time()
    algoritmo.sort(dados.copy())
    fim = time.time()

    tempo_execucao = (fim - inicio) * 1000  # milissegundos

    print(f"{algoritmo.__class__.__name__}: Tempo de execução = {tempo_execucao:.2f} ms")

# Carregando os dados
dados = []
with open('data-generator/dados.txt', 'r') as file:
    dados = [int(linha.strip()) for linha in file.readlines()]

# Exemplo com Bubble Sort
from algorithms.bubble_sort import BubbleSort
bubble = BubbleSort()
executar_algoritmo(bubble, dados)

# Exemplo com Quick Sort
from algorithms.quick_sort import QuickSort
quick = QuickSort()
executar_algoritmo(quick, dados)

#Exemplo com Insertion Sort
from algorithms.insertion_sort import InsertionSort
insertion = InsertionSort()
executar_algoritmo(insertion, dados)

#Exemplo com Selection Sort
from algorithms.selection_sort import SelectionSort
selection = SelectionSort()
executar_algoritmo(selection, dados)

#Exemplo com Insertion Sort
from algorithms.insertion_sort import InsertionSort
insertion = InsertionSort()
executar_algoritmo(insertion, dados)