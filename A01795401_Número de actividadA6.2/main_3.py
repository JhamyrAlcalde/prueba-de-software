"""
Prueba 3: Manejo de errores y validaciones.
- Intentar reservar en un hotel que no existe.
- Intentar reservar más habitaciones de las disponibles.
- Intentar reservar sin clientes registrados.
"""

from hotel_system import Hotel, Customer, Reservation

print("\n📌 Creando hoteles en Perú...")
Hotel.create_hotel(5, "Tambo del Inka", "Urubamba", 5)

print("\n📌 Intentando reservar más habitaciones de las disponibles...")
if not Hotel.reserve_room(5, 10):  # Solo hay 5 habitaciones disponibles
    print("✅ Correcto: No se permitió la reserva.")

print("\n📌 Intentando reservar en un hotel que no existe...")
if not Hotel.reserve_room(99, 2):  # No existe hotel 99
    print("✅ Correcto: No se permitió la reserva.")

print("\n📌 Intentando reservar sin clientes registrados...")
Reservation.create_reservation(3001, 999, 5)  # Cliente 999 no existe

print("\n🔹 Lista de Hoteles:")
Hotel.display_hotels()

print("\n🔹 Lista de Reservas:")
Reservation.display_reservations()
