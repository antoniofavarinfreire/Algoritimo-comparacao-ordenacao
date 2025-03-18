import time
import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
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
from benchmark_script.create_plot import create_plot
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource

resource = Resource.create({"service.name": "sorting_algorithms_benchmark"})

# ✅ Configure OpenTelemetry Tracing
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# ✅ Use OTLP Exporter Instead of JaegerExporter
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
provider.add_span_processor(BatchSpanProcessor(otlp_exporter))

# ✅ Instrument logging to include trace context
LoggingInstrumentor().instrument()

# ✅ Initialize logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Function to Load Data with Tracing
def carregar_dados(caminho):
    with tracer.start_as_current_span("carregar_dados") as span:
        try:
            with open(caminho, 'r') as file:
                data = [int(line.strip()) for line in file]
            logging.info("Successfully loaded data from %s", caminho)

            # ✅ Add metadata to the span
            span.set_attribute("file.path", caminho)
            span.set_attribute("data.size", len(data))

            return data
        except Exception as e:
            logging.error("Error loading data: %s", str(e))
            SORTING_ERRORS.labels("data_load").inc()
            span.record_exception(e)
            return []

# ✅ Dictionary to Store Execution Times
benchmark_data = {}

# ✅ Function to Execute Sorting Algorithms with Tracing
def executar_algoritmo(algoritmo: SortingStrategy, dados: list, repeticoes=1):
    global benchmark_data
    with tracer.start_as_current_span(f"executar_{algoritmo.__class__.__name__}") as span:
        for _ in range(repeticoes):
            try:
                dados_copia = dados.copy()
                inicio = time.time()
                algoritmo.sort(dados_copia)
                fim = time.time()

                exec_time = (fim - inicio) * 1000  # Convert to milliseconds

                logging.info(f"{algoritmo.__class__.__name__}: Execution Time = {exec_time:.2f} ms")

                # ✅ Store benchmark data
                benchmark_data[algoritmo.__class__.__name__] = exec_time

                # ✅ Add metadata to the trace
                span.set_attribute("dataset.size", len(dados))
                span.set_attribute("algorithm.name", algoritmo.__class__.__name__)
                span.set_attribute("execution.time_ms", exec_time)

            except Exception as e:
                logging.error("Error executing %s: %s", algoritmo.__class__.__name__, str(e))
                span.record_exception(e)

# ✅ Load Dataset
dados = carregar_dados('dados.txt')

# ✅ List of Sorting Algorithms
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

# ✅ Execute Each Algorithm
for algoritmo in algoritmos:
    executar_algoritmo(algoritmo, dados)

# ✅ Generate and Display the Benchmark Graph
create_plot(benchmark_data, dados)
