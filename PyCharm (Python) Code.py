class Reservation:
    """This class represents a hotel room reservation."""

    def __init__(self, reservation_id, guest_name, room_number, check_in_date, check_out_date):
        # Initializing the attributes related to a reservation
        self.__reservation_id = reservation_id  # Unique ID for the reservation
        self.__guest_name = guest_name  # Storing the guest's name
        self.__room_number = room_number  # Tracking the assigned room number
        self.__check_in_date = check_in_date  # Setting the check-in date
        self.__check_out_date = check_out_date  # Setting the check-out date

    def get_reservation_id(self):
        return self.__reservation_id  # Returning the reservation ID

    def modify_reservation(self, new_room_number):
        # Updating the room number for the reservation
        self.__room_number = new_room_number

    def display_details(self):
        # Formatting and returning a string with all relevant reservation details
        return "Reservation ID: " + str(self.__reservation_id) + ", Guest: " + self.__guest_name + \
            ", Room: " + str(self.__room_number) + ", Check-in: " + self.__check_in_date + \
            ", Check-out: " + self.__check_out_date


class Room:
    """This class represents a hotel room."""

    def __init__(self, room_number, room_type, price_per_night, availability, description):
        # Initializing the attributes related to a room
        self.__room_number = room_number  # Unique room number
        self.__room_type = room_type  # Type of room (e.g., single, double)
        self.__price_per_night = price_per_night  # Price per night
        self.__availability = availability  # Availability status
        self.__description = description  # Description of the room

    def check_availability(self):
        # Returning the availability status of the room
        return self.__availability

    def book_room(self):
        # Booking the room if it’s available
        if self.__availability:
            self.__availability = False  # Marking the room as booked
            return True  # Indicating successful booking
        return False  # Indicating the room was not available


class Payment:
    """This class represents a payment made for a reservation."""

    def __init__(self, payment_id, amount, payment_method, reservation_id, payment_date):
        # Initializing the attributes related to a payment
        self.__payment_id = payment_id  # Unique ID for the payment
        self.__amount = amount  # Total amount paid
        self.__payment_method = payment_method  # Payment method used (e.g., credit card)
        self.__reservation_id = reservation_id  # Link to the reservation
        self.__payment_date = payment_date  # Date when the payment was made

    def process_payment(self):
        # Logic to process the payment would go here
        pass

    def refund_payment(self):
        # Logic to refund the payment would go here
        pass


class Customer:
    """This class represents a hotel customer."""

    def __init__(self, customer_id, name, email, phone_number):
        # Initializing the attributes related to a customer
        self.__customer_id = customer_id  # Unique ID for the customer
        self.__name = name  # Customer's name
        self.__email = email  # Customer's email address
        self.__phone_number = phone_number  # Customer's phone number
        self.__reservation_list = []  # Initializing an empty list for reservations

    def add_reservation(self, reservation):
        # Adding a reservation object to the customer's reservation list
        self.__reservation_list.append(reservation)

    def get_reservation_list(self):
        # Returning the list of reservations made by the customer
        return self.__reservation_list


# Example of using the classes
# Creating a Room object
room1 = Room(101, "Double", 150.00, True, "A room with two double beds.")

# Creating a Reservation object
reservation1 = Reservation(12345, "Ted Vera", room1._Room__room_number, "2024-09-23", "2024-09-25")

# Creating a Payment object
payment1 = Payment(1, 150.00, "Mastercard", reservation1.get_reservation_id(), "2024-09-20")

# Creating a Customer object
customer1 = Customer(1, "Ted Vera", "tedvera@mac.com", "505-661-1110")

# Populating the customer's reservation list
customer1.add_reservation(reservation1)

# Displaying reservation information
print(reservation1.display_details())  # Printing the details of the reservation
