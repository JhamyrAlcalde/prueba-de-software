# 🏨 Sistema de Reservas de Hotel (Python)

Este es un sistema de reservas de hotel desarrollado en Python, que permite la gestión de **hoteles, clientes y reservas**.  
Incluye pruebas unitarias y medición de cobertura con `unittest` y `coverage`.

** Información importante ** :

Archivo	                    Descripción
hotel_system.py	        Código principal con la implementación del sistema de reservas.
main_1.py	            Prueba el flujo normal (crear hoteles, clientes y reservas).
main_2.py	            Prueba la modificación y eliminación de datos.
main_3.py	            Prueba validaciones de errores (hoteles inexistentes, JSON corrupto).
main_4.py	            Prueba reservas masivas y cancelaciones.
test_hotel_system.py	Pruebas unitarias del sistema con unittest.

### Clonar el repositorio y realizar los siguientes pasos:

1. Instalar coverage:

pip install coverage

2. Ejecutar el programa:

python3 main_1.py
python3 main_2.py
python3 main_3.py
python3 main_4.py


3. Ejecutar pruebas unitarias:

python3 -m unittest test_hotel_system.py


4. Ejecutar coverage:

python3 -m coverage run --source=hotel_system -m unittest test_hotel_system.py

5. Visualizamos resultados:

python3 -m coverage report -m