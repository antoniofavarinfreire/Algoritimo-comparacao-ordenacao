import time
import logging
from prometheus_client import start_http_server, Counter, Summary
from algorithms.sorting_strategy import SortingStrategy
from algorithms.bubble_sort import BubbleSort
from algorithms.quick_sort import QuickSort
from algorithms.insertion_sort import InsertionSort
from algorithms.selection_sort import SelectionSort
from algorithms.tim_sort import TimSort
from algorithms.shell_sort import ShellSort
from algorithms.merge_sort import MergeSort
from algorithms.heap_sort import HeapSort
from algorithms.counting_sort import CountingSort
from algorithms.radix_sort import RadixSort
from algorithms.bubble_sort_optimized import BubbleSortOptimized

# Initialize logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Prometheus Metrics
SORT_EXECUTION_TIME = Summary('sorting_execution_time', 'Time taken by sorting algorithms', ['algorithm'])
SORTING_ERRORS = Counter('sorting_errors', 'Count of sorting algorithm errors', ['algorithm'])
SORTING_SUCCESS = Counter('sorting_success', 'Count of successful sorting executions', ['algorithm'])

# Start Prometheus HTTP server
start_http_server(8000)  # Exposes metrics at http://localhost:8000

# Function to load data
def carregar_dados(caminho):
    try:
        with open(caminho, 'r') as file:
            data = [int(line.strip()) for line in file]
        logging.info("Successfully loaded data from %s", caminho)
        return data
    except Exception as e:
        logging.error("Error loading data: %s", str(e))
        SORTING_ERRORS.labels("data_load").inc()
        return []

# Function to execute sorting algorithms and collect metrics
def executar_algoritmo(algoritmo: SortingStrategy, dados: list, repeticoes=1):
    for _ in range(repeticoes):
        try:
            dados_copia = dados.copy()
            inicio = time.time()
            resultado = algoritmo.sort(dados_copia)
            fim = time.time()

            exec_time = (fim - inicio) * 1000  # Convert to milliseconds
            SORT_EXECUTION_TIME.labels(algoritmo.__class__.__name__).observe(exec_time)
            SORTING_SUCCESS.labels(algoritmo.__class__.__name__).inc()

            logging.info(f"{algoritmo.__class__.__name__}: Execution Time = {exec_time:.2f} ms")
        except Exception as e:
            logging.error("Error executing %s: %s", algoritmo.__class__.__name__, str(e))
            SORTING_ERRORS.labels(algoritmo.__class__.__name__).inc()

# Load dataset
dados = carregar_dados('data-generator/dados.txt')

# List of sorting algorithms
algoritmos = [
    BubbleSort(),
    BubbleSortOptimized(),
    QuickSort(),
    InsertionSort(),
    SelectionSort(),
    TimSort(),
    ShellSort(),
    MergeSort(),
    HeapSort(),
    CountingSort(),
    RadixSort()
]

# Execute each algorithm
for algoritmo in algoritmos:
    executar_algoritmo(algoritmo, dados)

# Keep the server running
while True:
    time.sleep(1)
