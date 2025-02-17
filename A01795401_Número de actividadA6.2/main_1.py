"""
Prueba 1: Flujo normal del sistema de reservas.
- Crear hoteles y clientes
- Realizar reservas
- Mostrar datos guardados
"""

from hotel_system import Hotel, Customer, Reservation

print("\n📌 Creando hoteles en Perú...")
Hotel.create_hotel(1, "JW Marriott", "Lima", 20)
Hotel.create_hotel(2, "Belmond Miraflores Park", "Lima", 15)

print("\n📌 Creando clientes peruanos...")
Customer.create_customer(101, "Luis Rodríguez", "luis.rodriguez@email.com")
Customer.create_customer(102, "María Pérez", "maria.perez@email.com")

print("\n📌 Realizando reservas...")
if Hotel.reserve_room(1, 2):
    Reservation.create_reservation(2001, 101, 1)
if Hotel.reserve_room(2, 3):
    Reservation.create_reservation(2002, 102, 2)

print("\n🔹 Lista de Hoteles después de reservas:")
Hotel.display_hotels()

print("\n🔹 Lista de Clientes:")
Customer.display_customers()

print("\n🔹 Lista de Reservas:")
Reservation.display_reservations()
