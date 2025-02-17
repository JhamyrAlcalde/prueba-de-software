"""
Pruebas unitarias para el sistema de reservas de hotel.
Usamos unittest para validar el comportamiento de las funciones principales.
"""

import unittest
import os
import json
from hotel_system import Hotel, Customer, Reservation


class TestHotelSystem(unittest.TestCase):
    """Pruebas unitarias para hoteles, clientes y reservas."""

    def setUp(self):
        """Se ejecuta antes de cada prueba para limpiar los datos."""
        open(Hotel.FILE_PATH, "w").close()  # Limpiar archivo de hoteles
        open(Customer.FILE_PATH, "w").close()  # Limpiar archivo de clientes
        open(Reservation.FILE_PATH, "w").close()  # Limpiar archivo de reservas

    def test_create_hotel(self):
        """Prueba la creación de un hotel."""
        Hotel.create_hotel(1, "JW Marriott", "Lima", 20)
        hotels = Hotel.load_hotels()
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0].name, "JW Marriott")

    def test_delete_hotel(self):
        """Prueba la eliminación de un hotel."""
        Hotel.create_hotel(2, "Belmond Miraflores Park", "Lima", 15)
        Hotel.delete_hotel(2)
        hotels = Hotel.load_hotels()
        self.assertEqual(len(hotels), 0)

    def test_modify_hotel(self):
        """Prueba la modificación de un hotel."""
        Hotel.create_hotel(3, "Casa Andina", "Arequipa", 10)
        Hotel.modify_hotel(3, "Casa Andina Premium", "Centro Histórico", 20)
        hotels = Hotel.load_hotels()
        self.assertEqual(hotels[0].name, "Casa Andina Premium")
        self.assertEqual(hotels[0].rooms_available, 20)

    def test_reserve_room(self):
        """Prueba la reserva de habitaciones en un hotel."""
        Hotel.create_hotel(4, "Hotel Libertador", "Cusco", 5)
        self.assertTrue(Hotel.reserve_room(4, 3))  # Reservar 3 habitaciones
        hotels = Hotel.load_hotels()
        self.assertEqual(hotels[0].rooms_available, 2)  # Deben quedar 2 habitaciones

    def test_reserve_nonexistent_hotel(self):
        """Prueba de error al intentar reservar en un hotel que no existe."""
        with self.assertRaises(ValueError):
            Hotel.reserve_room(999, 2)  # Hotel con ID 999 no existe

    def test_create_customer(self):
        """Prueba la creación de un cliente."""
        Customer.create_customer(101, "Luis Rodríguez", "luis@email.com")
        customers = Customer.load_customers()
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0].name, "Luis Rodríguez")

    def test_modify_customer(self):
        """Prueba la modificación de un cliente."""
        Customer.create_customer(102, "María Pérez", "maria@email.com")
        Customer.modify_customer(102, "María García", "maria.new@email.com")
        customers = Customer.load_customers()
        self.assertEqual(customers[0].name, "María García")

    def test_create_reservation(self):
        """Prueba la creación de una reserva."""
        Hotel.create_hotel(5, "Tambo del Inka", "Urubamba", 10)
        Customer.create_customer(103, "Carlos Gómez", "carlos@email.com")
        Reservation.create_reservation(2001, 103, 5)
        reservations = Reservation.load_reservations()
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0].customer_id, 103)

    def test_cancel_reservation(self):
        """Prueba la cancelación de una reserva."""
        Hotel.create_hotel(6, "Inkaterra Machu Picchu", "Machu Picchu", 10)
        Customer.create_customer(104, "Andrea Torres", "andrea@email.com")
        Reservation.create_reservation(3001, 104, 6)
        reservations_before = Reservation.load_reservations()
        self.assertEqual(len(reservations_before), 1)

        Reservation.cancel_reservation(3001)  # Cancelar la reserva

        reservations_after = Reservation.load_reservations()
        self.assertEqual(len(reservations_after), 0)  # Debe estar vacía

        hotels = Hotel.load_hotels()
        self.assertEqual(hotels[0].rooms_available, 10)  # Las habitaciones deben restaurarse

    def test_load_invalid_json(self):
        """Prueba cargar un JSON corrupto."""
        with open(Hotel.FILE_PATH, "w", encoding="utf-8") as file:
            file.write("{ invalid json }")  # JSON mal escrito

        hotels = Hotel.load_hotels()
        self.assertEqual(len(hotels), 0)  # Debe cargar como lista vacía

    def tearDown(self):
        """Se ejecuta después de cada prueba para eliminar los archivos de prueba."""
        if os.path.exists(Hotel.FILE_PATH):
            os.remove(Hotel.FILE_PATH)
        if os.path.exists(Customer.FILE_PATH):
            os.remove(Customer.FILE_PATH)
        if os.path.exists(Reservation.FILE_PATH):
            os.remove(Reservation.FILE_PATH)


if __name__ == "__main__":
    unittest.main()
