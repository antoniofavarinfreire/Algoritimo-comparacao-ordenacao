import os
import matplotlib.pyplot as plt

def create_plot(benchmark_data, dados):
    """
    Generates a bar chart comparing the execution times of different sorting algorithms
    and saves it as an image file named with the length of `dados`.

    :param benchmark_data: Dictionary with algorithm names as keys and execution times (ms) as values.
    :param dados: The dataset used for sorting (to determine filename length).
    """
    if not benchmark_data:
        print("No benchmark data available to generate a graph.")
        return

    if not dados:
        print("Dataset is empty. Cannot determine filename.")
        return

    dataset_length = len(dados)

    # Create folder benchmarks one level up if it doesn't exist
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    benchmarks_dir = os.path.join(parent_dir, "benchmarks")
    if not os.path.exists(benchmarks_dir):
        os.makedirs(benchmarks_dir)

    filename = os.path.join(benchmarks_dir, f"{dataset_length}.png")  # Create filename based on dataset length

    # Sort data for better visualization
    sorted_benchmark = dict(sorted(benchmark_data.items(), key=lambda x: x[1]))

    # Generate bar chart
    plt.figure(figsize=(12, 6))
    bars = plt.barh(list(sorted_benchmark.keys()), list(sorted_benchmark.values()))
    plt.xlabel("Execution Time (ms)")
    plt.ylabel("Sorting Algorithm")
    plt.title(f"Sorting Algorithm Benchmark - {dataset_length} elements")
    plt.grid(axis="x", linestyle="--", alpha=0.7)

    # Add execution time as legend
    for bar, (algorithm, time) in zip(bars, sorted_benchmark.items()):
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{time:.2f} ms', va='center')

    # Save plot as a file
    plt.savefig(filename)
    plt.close()  # Close the plot to prevent it from displaying in GUI mode

    print(f"Benchmark graph saved as {filename}")
