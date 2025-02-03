"""
Este script calcula estadísticas como media, mediana, moda,
varianza y desviación estándar a partir de un archivo de entrada.
Guarda los resultados en un archivo y muestra el tiempo de ejecución.
"""

import sys
import time
import math

def read_numbers(filename):
    """Lee números de un archivo, ignora valores inválidos y devuelve una lista de números."""
    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print(f"Error: '{line.strip()}' no es un número válido.")
    return numbers

def compute_statistics(numbers):
    """Calcula la media, mediana, moda, varianza y desviación estándar de una lista de números."""
    n = len(numbers)
    if n == 0:
        return None

    mean = sum(numbers) / n
    sorted_numbers = sorted(numbers)
    median = sorted_numbers[n // 2] if n % 2 != 0 else (
        sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]
    ) / 2
    mode = max(set(numbers), key=numbers.count) if numbers else None
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = math.sqrt(variance)

    return mean, median, mode, variance, std_dev

def main():
    """Función principal que ejecuta el programa."""
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Uso: python compute_statistics.py fileWithData.txt")
        return
    filename = sys.argv[1]
    try:
        numbers = read_numbers(filename)
        stats = compute_statistics(numbers)
        if stats:
            mean, median, mode, variance, std_dev = stats
            output = (
                f"Media: {mean}\n"
                f"Mediana: {median}\n"
                f"Moda: {mode}\n"
                f"Varianza: {variance}\n"
                f"Desviación estándar: {std_dev}"
            )
            print(output)

            with open("StatisticsResults.txt", "w", encoding="utf-8") as file:
                file.write(output)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe.")
    elapsed_time = time.time() - start_time
    print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    main()
