"""
Este script convierte números decimales (positivos y negativos) 
a sus representaciones en binario y hexadecimal,
siguiendo el formato específico de salida en columnas.
"""

import sys
import time

def decimal_to_binary(n):
    """Convierte un número decimal a binario, manejando números negativos en complemento a dos."""
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(n)
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2

    if is_negative:
        binary = "-" + binary  # Para indicar que el número es negativo
    return binary

def decimal_to_hexadecimal(n):
    """Convierte un número decimal a hexadecimal, incluyendo negativos."""
    if n == 0:
        return "0"

    is_negative = n < 0
    n = abs(n)

    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        remainder = n % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        n //= 16

    if is_negative:
        hexadecimal = "-" + hexadecimal  # Agregar el signo negativo
    return hexadecimal

def read_numbers(filename):
    """Lee números enteros desde un archivo, ignorando valores no numéricos."""
    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            try:
                number = int(line.strip())  # Convertir a entero
                numbers.append(number)
            except ValueError:
                print(f"Error: '{line.strip()}' no es un número válido y será ignorado.")
    return numbers

def main():
    """Función principal que ejecuta la conversión de números a binario y hexadecimal."""
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Uso: python convert_numbers.py fileWithData.txt")
        return
    filename = sys.argv[1]
    try:
        numbers = read_numbers(filename)
        # Formato de salida con cabecera
        header = f"{'ITEM':<5} {'TC1':<10} {'BIN':<20} {'HEX':<10}"
        results = [header]
        for index, number in enumerate(numbers, start=1):
            binary = decimal_to_binary(number)
            hexadecimal = decimal_to_hexadecimal(number)
            formatted_line = f"{index:<5} {number:<10} {binary:<20} {hexadecimal:<10}"
            results.append(formatted_line)
        output = "\n".join(results)
        print(output)
        with open("ConversionResults.txt", "w", encoding="utf-8") as file:
            file.write(output)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe.")
    elapsed_time = time.time() - start_time
    print(f"\nTiempo de ejecución: {elapsed_time:.2f} segundos")
if __name__ == "__main__":
    main()
