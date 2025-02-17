"""
Sistema de reservas de hotel con clientes y reservas.
Maneja la persistencia en archivos y permite operaciones CRUD.
"""

import json
import os


class Hotel:
    """Clase que representa un hotel y maneja su información."""

    FILE_PATH = "hotels.json"

    def __init__(self, hotel_id, name, location, rooms_available):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available

    def to_dict(self):
        """Convierte el hotel en un diccionario."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms_available": self.rooms_available
        }

    @classmethod
    def save_hotels(cls, hotels):
        """Guarda la lista de hoteles en un archivo JSON."""
        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([hotel.to_dict() for hotel in hotels], file, indent=4)

    @classmethod
    def load_hotels(cls):
        """Carga la lista de hoteles desde el archivo JSON y maneja archivos vacíos."""
        if not os.path.exists(cls.FILE_PATH) or os.stat(cls.FILE_PATH).st_size == 0:
            return []
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return [cls(**hotel) for hotel in json.load(file)]
        except json.JSONDecodeError:
            return []

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms_available):
        """Crea un nuevo hotel y lo guarda en la lista."""
        hotels = cls.load_hotels()
        hotels.append(cls(hotel_id, name, location, rooms_available))
        cls.save_hotels(hotels)

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Elimina un hotel de la lista."""
        hotels = cls.load_hotels()
        hotels = [hotel for hotel in hotels if hotel.hotel_id != hotel_id]
        cls.save_hotels(hotels)

    @classmethod
    def modify_hotel(cls, hotel_id, new_name, new_location, new_rooms_available):
        """Modifica la información de un hotel."""
        hotels = cls.load_hotels()
        for hotel in hotels:
            if hotel.hotel_id == hotel_id:
                hotel.name = new_name
                hotel.location = new_location
                hotel.rooms_available = new_rooms_available
        cls.save_hotels(hotels)

    @classmethod
    def reserve_room(cls, hotel_id, rooms_requested):
        """Reserva habitaciones en un hotel si hay disponibilidad, 
        o lanza un ValueError si el hotel no existe."""
        hotels = cls.load_hotels()
        for hotel in hotels:
            if hotel.hotel_id == hotel_id:
                if hotel.rooms_available >= rooms_requested:
                    hotel.rooms_available -= rooms_requested
                    cls.save_hotels(hotels)
                    return True
                print("Error: No hay suficientes habitaciones disponibles.")
                return False

        raise ValueError(f"Error: Hotel con ID {hotel_id} no encontrado.")
    @classmethod
    def display_hotels(cls):
        """Muestra todos los hoteles guardados."""
        hotels = cls.load_hotels()
        for hotel in hotels:
            print(f"{hotel.hotel_id}: {hotel.name} - {hotel.location} \
                  ({hotel.rooms_available} habitaciones)")


class Customer:
    """Clase que representa un cliente del sistema de reservas."""

    FILE_PATH = "customers.json"

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convierte un cliente en diccionario."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }

    @classmethod
    def save_customers(cls, customers):
        """Guarda los clientes en un archivo JSON."""
        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([customer.to_dict() for customer in customers], file, indent=4)

    @classmethod
    def load_customers(cls):
        """Carga los clientes desde el archivo JSON y maneja archivos vacíos."""
        if not os.path.exists(cls.FILE_PATH) or os.stat(cls.FILE_PATH).st_size == 0:
            return []
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return [cls(**customer) for customer in json.load(file)]
        except json.JSONDecodeError:
            return []

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Crea un nuevo cliente."""
        customers = cls.load_customers()
        customers.append(cls(customer_id, name, email))
        cls.save_customers(customers)

    @classmethod
    def modify_customer(cls, customer_id, new_name, new_email):
        """Modifica la información de un cliente."""
        customers = cls.load_customers()
        for customer in customers:
            if customer.customer_id == customer_id:
                customer.name = new_name
                customer.email = new_email
        cls.save_customers(customers)

    @classmethod
    def display_customers(cls):
        """Muestra todos los clientes guardados."""
        customers = cls.load_customers()
        for customer in customers:
            print(f"{customer.customer_id}: {customer.name} - {customer.email}")


class Reservation:
    """Clase que maneja las reservas de hotel."""

    FILE_PATH = "reservations.json"

    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Convierte una reserva en diccionario."""
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id
        }

    @classmethod
    def save_reservations(cls, reservations):
        """Guarda las reservas en un archivo JSON."""
        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([res.to_dict() for res in reservations], file, indent=4)

    @classmethod
    def load_reservations(cls):
        """Carga las reservas desde el archivo JSON y maneja archivos vacíos."""
        if not os.path.exists(cls.FILE_PATH) or os.stat(cls.FILE_PATH).st_size == 0:
            return []
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return [cls(**res) for res in json.load(file)]
        except json.JSONDecodeError:
            return []

    @classmethod
    def create_reservation(cls, reservation_id, customer_id, hotel_id):
        """Crea una nueva reserva.
        
        Intenta reservar 1 habitación en el hotel. Si se reserva correctamente,
        se crea y guarda la reserva. De lo contrario, se muestra un mensaje de error.
        """
        if Hotel.reserve_room(hotel_id, 1):
            reservations = cls.load_reservations()
            reservations.append(cls(reservation_id, customer_id, hotel_id))
            cls.save_reservations(reservations)
        else:
            print("No se pudo reservar la habitación.")

    @classmethod
    def cancel_reservation(cls, reservation_id):
        """Cancela una reserva y devuelve exactamente la 
        cantidad correcta de habitaciones al hotel."""
        reservations = cls.load_reservations()
        new_reservations = []
        canceled = False

        for res in reservations:
            if res.reservation_id == reservation_id:
                canceled = True
                hotels = Hotel.load_hotels()
                for hotel in hotels:
                    if hotel.hotel_id == res.hotel_id:
                        hotel.rooms_available += 1  # Restaurar solo 1 habitación
                        break
                Hotel.save_hotels(hotels)
            else:
                new_reservations.append(res)

        if canceled:
            cls.save_reservations(new_reservations)
            print(f"✅ Reserva {reservation_id} cancelada correctamente. \
                  Habitaciones restauradas: 1")
        else:
            print(f"⚠️ No se encontró la reserva {reservation_id}.")

    @classmethod
    def display_reservations(cls):
        """Muestra todas las reservas guardadas."""
        reservations = cls.load_reservations()
        for res in reservations:
            print(f"Reserva {res.reservation_id}: Cliente {res.customer_id} - Hotel {res.hotel_id}")
