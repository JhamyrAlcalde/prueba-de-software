"""
Este script cuenta la frecuencia de palabras en un archivo de texto y 
formatea la salida para que coincida con el formato esperado.
"""

import sys
import time

def clean_word(word):
    """Elimina caracteres no alfabéticos y convierte a minúsculas."""
    cleaned = ""
    for char in word:
        if char.isalpha():
            cleaned += char.lower()
    return cleaned

def read_words(filename):
    """Lee palabras desde un archivo, limpiándolas manualmente."""
    words = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                current_word = ""
                for char in line:
                    if char.isalpha():
                        current_word += char.lower()
                    elif current_word:
                        words.append(current_word)
                        current_word = ""
                if current_word:
                    words.append(current_word)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe.")
        return []
    return words

def count_word_frequencies(words):
    """Cuenta la frecuencia de cada palabra usando listas en lugar de diccionarios."""
    word_list = []
    word_count = []
    for word in words:
        found = False
        for index, existing_word in enumerate(word_list):
            if existing_word == word:
                word_count[index] += 1
                found = True
                break
        if not found:
            word_list.append(word)
            word_count.append(1)

    return word_list, word_count

def bubble_sort(words, counts):
    """Ordena las palabras alfabéticamente junto con sus conteos usando Bubble Sort."""
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]
                counts[j], counts[j + 1] = counts[j + 1], counts[j]

def main():
    """Función principal que ejecuta el programa."""
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return
    filename = sys.argv[1]
    words = read_words(filename)
    if not words:
        return

    word_list, word_counts = count_word_frequencies(words)
    bubble_sort(word_list, word_counts)

    # Formatear la salida como la imagen
    output_lines = ["Row Labels     Count of TC2"]
    for word, count in zip(word_list, word_counts):
        output_lines.append(f"{word:<15} {count:>5}")

    output_text = "\n".join(output_lines)
    print(output_text)

    # Guardar los resultados en el archivo
    with open("WordCountResults.txt", "w", encoding="utf-8") as file:
        file.write(output_text)

    elapsed_time = time.time() - start_time
    print(f"\nTiempo de ejecución: {elapsed_time:.2f} segundos")

    # Guardar el tiempo de ejecución en el archivo de resultados
    with open("WordCountResults.txt", "a", encoding="utf-8") as file:
        file.write(f"\nTiempo de ejecución: {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    main()
