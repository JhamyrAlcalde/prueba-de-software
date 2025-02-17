"""
Prueba 2: Modificar y eliminar hoteles y clientes.
"""

from hotel_system import Hotel, Customer, Reservation

print("\n📌 Creando hoteles en Perú...")
Hotel.create_hotel(3, "Casa Andina Premium", "Arequipa", 25)
Hotel.create_hotel(4, "Hotel Libertador", "Cusco", 30)

print("\n📌 Creando clientes peruanos...")
Customer.create_customer(103, "Carlos Gómez", "carlos.gomez@email.com")
Customer.create_customer(104, "Andrea Torres", "andrea.torres@email.com")

print("\n📌 Modificando el hotel 'Casa Andina Premium' en Arequipa...")
Hotel.modify_hotel(3, "Casa Andina Arequipa", "Centro Histórico, Arequipa", 20)

print("\n📌 Eliminando hotel 'Hotel Libertador' en Cusco...")
Hotel.delete_hotel(4)

print("\n📌 Eliminando cliente Andrea Torres...")
Customer.create_customer(104, "Andrea Torres", "andrea.torres@email.com")
Customer.display_customers()
Customer.create_customer(103, "Carlos Gómez", "carlos.gomez@email.com")
Customer.display_customers()

print("\n🔹 Lista de Hoteles después de eliminación:")
Hotel.display_hotels()

print("\n🔹 Lista de Clientes después de eliminación:")
Customer.display_customers()
