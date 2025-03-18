# Padrão Strategy Aplicado ao Código

O **padrão Strategy** é um padrão de design comportamental que permite definir uma família de algoritmos, encapsulá-los em classes separadas e torná-los intercambiáveis. Esse padrão promove a substituição de algoritmos sem modificar o código que os usa.

---

## Como o Padrão Strategy é Aplicado no Código?

No código, o padrão Strategy é usado para organizar e executar diferentes algoritmos de ordenação de forma flexível. A ideia principal é que cada algoritmo de ordenação implementa uma interface comum (`SortingStrategy`), permitindo que sejam utilizados de maneira intercambiável sem precisar modificar o código principal.

---

## Componentes do Padrão Strategy no Código

### 1. Interface/Classe Base (`SortingStrategy`)

- Essa classe define um método comum para os algoritmos de ordenação, geralmente chamado `sort()`.
- Todos os algoritmos concretos de ordenação (como `BubbleSort`, `QuickSort`, `MergeSort`, etc.) implementam essa interface.

### 2. Algoritmos Concretos

- Cada classe de ordenação (`BubbleSort`, `QuickSort`, `MergeSort`, etc.) implementa a interface `SortingStrategy` e fornece sua própria implementação do método `sort()`.
- Isso permite que todos os algoritmos sejam usados de forma intercambiável.

### 3. Contexto (Código Principal)

- O código principal não precisa saber os detalhes de implementação de cada algoritmo de ordenação. Ele simplesmente recebe um objeto que segue a interface `SortingStrategy` e chama seu método `sort()`.
- A função `executar_algoritmo()` recebe uma instância de `SortingStrategy`, executa o algoritmo correspondente e mede seu desempenho.

---

## Benefícios do Padrão Strategy neste Caso

✅ **Código mais flexível e extensível** – É fácil adicionar novos algoritmos de ordenação sem modificar o código principal.  
✅ **Princípio Aberto/Fechado** – O código está aberto para extensão (novos algoritmos), mas fechado para modificação.  
✅ **Facilidade de manutenção** – Se um algoritmo precisar ser alterado ou otimizado, essa mudança não impacta os outros algoritmos nem o código que os utiliza.  
✅ **Desacoplamento** – O código que usa os algoritmos (como `executar_algoritmo()`) não precisa conhecer a implementação específica de cada método de ordenação.

---

## Fluxo de Execução

1. O código carrega os dados do arquivo (`carregar_dados()`).
2. Cria uma lista com diferentes algoritmos de ordenação (`algoritmos`).
3. Para cada algoritmo na lista, ele executa `executar_algoritmo()`, que:
   - Mede o tempo de execução.
   - Registra métricas com Prometheus.
   - Garante que erros sejam capturados e contados separadamente.

---

## Exemplo Simples do Padrão Strategy

Se tivermos um sistema de ordenação sem o Strategy, precisaríamos de muitos `if-else`, o que dificultaria a manutenção:

```python
class Ordenador:
    def ordenar(self, dados, metodo):
        if metodo == "bubble":
            return self.bubble_sort(dados)
        elif metodo == "quick":
            return self.quick_sort(dados)
        # E assim por diante...

    def bubble_sort(self, dados):
        # Implementação do Bubble Sort
        pass

    def quick_sort(self, dados):
        # Implementação do Quick Sort
        pass
```

O problema é que cada vez que quisermos adicionar um novo algoritmo, precisaríamos modificar essa classe.

Usando Strategy, cada algoritmo é separado:

```python
from abc import ABC, abstractmethod

# Interface comum
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, dados):
        pass

# Implementação de Bubble Sort
class BubbleSort(SortingStrategy):
    def sort(self, dados):
        print("Ordenando com Bubble Sort")
        return sorted(dados)  # Implementação real seria diferente

# Implementação de Quick Sort
class QuickSort(SortingStrategy):
    def sort(self, dados):
        print("Ordenando com Quick Sort")
        return sorted(dados)  # Implementação real seria diferente

# Contexto que usa a estratégia
class Ordenador:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def ordenar(self, dados):
        return self.strategy.sort(dados)

# Uso
ordenador = Ordenador(BubbleSort())  # Pode mudar para QuickSort() sem alterar o código principal
ordenador.ordenar([5, 3, 8, 1])
```

---

## Conclusão

O seu código implementa o **padrão Strategy** para permitir que diferentes algoritmos de ordenação sejam usados de forma flexível e independente. Isso melhora a organização, a extensibilidade e a manutenção do sistema, tornando mais fácil testar, adicionar ou modificar algoritmos sem impactar outras partes do código. 🚀
