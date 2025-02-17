"""
Prueba 4: Realizar reservas y luego cancelarlas en masa.
"""

from hotel_system import Hotel, Customer, Reservation

print("\n📌 Creando hoteles en Perú...")
Hotel.create_hotel(6, "Inkaterra Machu Picchu", "Machu Picchu", 10)

print("\n📌 Creando clientes peruanos...")
Customer.create_customer(105, "Rosa Castillo", "rosa.castillo@email.com")
Customer.create_customer(106, "José Ramos", "jose.ramos@email.com")

print("\n📌 Realizando reservas en Inkaterra Machu Picchu...")
if Hotel.reserve_room(6, 3):
    Reservation.create_reservation(4001, 105, 6)
if Hotel.reserve_room(6, 4):
    Reservation.create_reservation(4002, 106, 6)

print("\n🔹 Lista de Reservas antes de la cancelación:")
Reservation.display_reservations()

print("\n📌 Cancelando la reserva 4001 y 4002...")
Reservation.cancel_reservation(4001)
Reservation.cancel_reservation(4002)

print("\n🔹 Lista de Reservas después de la cancelación:")
Reservation.display_reservations()

print("\n🔹 Lista de Hoteles después de cancelaciones (verificar habitaciones disponibles):")
Hotel.display_hotels()
