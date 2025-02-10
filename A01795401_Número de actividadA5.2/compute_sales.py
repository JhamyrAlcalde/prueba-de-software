"""
Este script calcula el total de ventas basado en un catálogo de productos
y un registro de ventas. Genera un reporte con el total de ventas
y los productos inválidos.
"""

import sys
import time
import json


def load_json(filename):
    """
    Carga un archivo JSON y maneja errores de
    archivo no encontrado o formato inválido.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
        return None
    except json.JSONDecodeError:
        print(
            f"Error: El archivo '{filename}' no contiene "
            f"un JSON válido."
        )
        return None


def build_price_catalogue(product_list):
    """Crea un diccionario de precios basado en el catálogo de productos."""
    return {
        product["title"]: product["price"]
        for product in product_list
    }


def compute_total_sales(price_catalogue, sales_record):
    """
    Calcula el total de ventas basado en el catálogo de precios
    y las ventas registradas. Ignora valores inválidos y los reporta.
    """
    total_sales = 0.0
    invalid_sales = []
    results = ["Resumen de Ventas", "-----------------"]

    for sale in sales_record:
        product = sale.get("Product")
        quantity = sale.get("Quantity")

        if product not in price_catalogue:
            error_msg = f"Producto '{product}' no encontrado en el catálogo."
            print(f"Advertencia: {error_msg}")
            invalid_sales.append(error_msg)
            continue

        if not isinstance(quantity, (int, float)) or quantity <= 0:
            error_msg = f"Cantidad inválida ({quantity}) para '{product}'."
            print(f"Advertencia: {error_msg}")
            invalid_sales.append(error_msg)
            continue

        price = price_catalogue[product]
        subtotal = price * quantity
        total_sales += subtotal

        results.append(
            f"{product}: {quantity} x ${price:.2f} = ${subtotal:.2f}"
        )

    results.append("-----------------")
    results.append(f"Total de ventas: ${total_sales:.2f}")

    # 🔹 Reportar registros inválidos ignorados
    results.append(f"Registros inválidos ignorados: {len(invalid_sales)}")
    if invalid_sales:
        results.append("Detalles de registros inválidos:")
        results.extend(invalid_sales)

    return total_sales, results


def main():
    """Función principal que ejecuta el cálculo de ventas."""
    start_time = time.time()

    if len(sys.argv) != 3:
        print(
            "Uso: python compute_sales.py "
            "price_catalogue.json sales_record.json"
        )
        return

    price_file, sales_file = sys.argv[1], sys.argv[2]

    # Cargar datos
    product_list = load_json(price_file)
    sales_record = load_json(sales_file)

    if product_list is None or sales_record is None:
        return

    # Construir catálogo de precios
    price_catalogue = build_price_catalogue(product_list)

    # Calcular ventas
    _, sales_results = compute_total_sales(price_catalogue, sales_record)

    # Mostrar resultados
    output = "\n".join(sales_results)
    print(output)

    # Guardar resultados en archivo
    with open("SalesResults.txt", "w", encoding="utf-8") as file:
        file.write(output)

    elapsed_time = time.time() - start_time
    print(f"\nTiempo de ejecución: {elapsed_time:.2f} segundos")

    # Guardar tiempo de ejecución en el archivo de resultados
    with open("SalesResults.txt", "a", encoding="utf-8") as file:
        file.write(f"\nTiempo de ejecución: {elapsed_time:.2f} segundos")


if __name__ == "__main__":
    main()
