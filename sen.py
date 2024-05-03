import pickle
import os
from datetime import date


# Base Employee Class
## name, employee ID, department, job title, basic salary, age, date of birth, and passport details
class Employee:
    def __init__(self, employee_id, name, department, job_title, basic_salary, age, dob, passport_details):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details

    def display(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Department: {self.department}")

    def get(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Department: {self.department}"

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Department: {self.department}"


# Manager Class inheriting from Employee
class Manager(Employee):
    def __init__(self, employee_id, name, department, job_title, basic_salary, age, dob, passport_details):
        super().__init__(employee_id, name, department, job_title, basic_salary, age, dob, passport_details)
        self.managed_employees = []

    def add_employee(self, employee):
        self.managed_employees.append(employee)

    def remove_employee(self, employee):
        self.managed_employees.remove(employee)

# Client Class
## Client ID, Name, Address, Contact details, and Budget
class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    def display(self):
        print(f"Client ID: {self.client_id}, Name: {self.name}, Contact: {self.contact_details}")

    def get(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Contact: {self.contact_details}"

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Contact: {self.contact_details}"

# Event Class
## weddings, birthdays, themed parties, and graduations
### Event ID, Type, Theme, Date, Time, Duration, Venue address, Client ID, Guest list, Catering company, Cleaning company, Decorations company, Entertainment company, Furniture supply company and Invoice
class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                 catering_company, cleaning_company, decoration_company, entertainment_company, furniture_company,
                 invoice):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decoration_company = decoration_company
        self.entertainment_company = entertainment_company
        self.furniture_company = furniture_company
        self.invoice = invoice

    def display(self):
        print(f"Event ID: {self.event_id}, Type: {self.event_type}, Client ID: {self.client_id}")

    def get(self):
        return f"Event ID: {self.event_id}, Type: {self.event_type}, Client ID: {self.client_id}"

    def __str__(self):
        return f"Event ID: {self.event_id}, Type: {self.event_type}, Client ID: {self.client_id}"

# Guest Class
## Guest ID, Name, Address, Contact details
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def display(self):
        print(f"Guest ID: {self.guest_id}, Name: {self.name}, Contact: {self.contact_details}")

    def get(self):
        return f"Guest ID: {self.guest_id}, Name: {self.name}, Contact: {self.contact_details}"

    def __str__(self):
        return f"Guest ID: {self.guest_id}, Name: {self.name}, Contact: {self.contact_details}"


# Supplier Class
## catering, cleaning, supplying furniture and decorations
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details, service_type, min_guests, max_guests):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.service_type = service_type
        self.min_guests = min_guests
        self.max_guests = max_guests

    def display(self):
        print(f"Supplier ID: {self.supplier_id}, Name: {self.name}, Contact: {self.contact_details}")

    def get(self):
        return f"Supplier ID: {self.supplier_id}, Name: {self.name}, Contact: {self.contact_details}"

    def __str__(self):
        return f"Supplier ID: {self.supplier_id}, Name: {self.name}, Contact: {self.contact_details}"

# Venue Class
## Venue ID, Name, Address, Contact, Minimum number of guests, and Maximum number of guests
class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    def display(self):
        print(f"Venue ID: {self.venue_id}, Name: {self.name}, Contact: {self.contact}")

    def get(self):
        return f"Venue ID: {self.venue_id}, Name: {self.name}, Contact: {self.contact}"

    def __str__(self):
        return f"Venue ID: {self.venue_id}, Name: {self.name}, Contact: {self.contact}"

# Caterer Class
## Caterer ID, Name, Address, Contact details, Menu, Minimum number of guests, and Maximum number of guests
class Caterer:
    def __init__(self, caterer_id, name, address, contact, menu, min_guests, max_guests):
        self.caterer_id = caterer_id
        self.name = name
        self.address = address
        self.contact = contact
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

    def display(self):
        print(f"Caterer ID: {self.caterer_id}, Name: {self.name}, Contact: {self.contact}")

    def get(self):
        return f"Caterer ID: {self.caterer_id}, Name: {self.name}, Contact: {self.contact}"

    def __str__(self):
        return f"Caterer ID: {self.caterer_id}, Name: {self.name}, Contact: {self.contact}"

# Events Company System to Manage All Entities
class EventsCompanySystem:
    def __init__(self):
        self.employees = []
        self.clients = []
        self.events = []
        self.suppliers = []
        self.guests = []
        self.venues = []
        self.caterers = []

    # Adding Entities
    def add_employee(self, employee):
        self.employees.append(employee)

    def add_client(self, client):
        self.clients.append(client)

    def add_event(self, event):
        self.events.append(event)

    def add_guest(self, guest):
        self.guests.append(guest)

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def add_venue(self, venue):
        self.venues.append(venue)

    def add_caterer(self, caterer):
        self.caterers.append(caterer)

    # Deleting Entities
    def remove_employee(self, employee):
        self.employees.remove(employee)

    def remove_client(self, client):
        self.clients.remove(client)

    def remove_event(self, event):
        self.events.remove(event)

    def remove_guest(self, guest):
        self.guests.remove(guest)

    def remove_supplier(self, supplier):
        self.suppliers.remove(supplier)

    def remove_venue(self, venue):
        self.venues.remove(venue)

    def remove_caterer(self, caterer):
        self.caterers.remove(caterer)

    # Displaying Details Based on ID
    def display_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee

    def display_client(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client

    def display_event(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                return event

    def display_supplier(self, supplier_id):
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                return supplier

    def display_venue(self, venue_id):
        for venue in self.venues:
            if venue.venue_id == venue_id:
                return venue

    def display_guest(self, guest_id):
        for guest in self.guests:
            if guest.guest_id == guest_id:
                return guest

    def display_caterer(self, caterer_id):
        for caterer in self.caterers:
            if caterer.caterer_id == caterer_id:
                return caterer

    # Displaying All Details
    def display_All(self):
        print("\nThe Employees:")
        for employee in self.employees:
            employee.display()
        print("\nThe Clients:")
        for client in self.clients:
            client.display()
        print("\nThe Events:")
        for event in self.events:
            event.display()
        print("\nThe Suppliers:")
        for supplier in self.suppliers:
            supplier.display()
        print("\nThe Venues:")
        for venue in self.venues:
            venue.display()
        print("\nThe Guests:")
        for guest in self.guests:
            guest.display()
        print("\nThe Caterers:")
        for caterer in self.caterers:
            caterer.display()

    # Serialization and Deserialization with Pickle
    def save_to_binary(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_binary(filename):
        if os.path.isfile(filename):
            with open(filename, 'rb') as file:
                return pickle.load(file)
        else:
            return None

# Test Cases for the System
def test_system():
    # Create the system
    system = EventsCompanySystem()

    # Create Employees
    employee1 = Employee(1, "Shyam Sundar", "Sales", "Salesperson", 35000, 30, "1993-08-20", "ABC123")
    employee2 = Employee(2, "Mariam Khalid", "Sales", "Salesperson", 20000, 29, "1994-07-19", "QWE987")
    employee3 = Employee(3, "Salma J Sam", "Sales", "Salesperson", 35000, 28, "1995-01-25", "DEF456")
    
    # Create a Manager and add managed employees
    manager1 = Manager(4, "Susan Meyers", "Sales", "Sales Manager", 50000, 35, "1988-06-15", "XYZ123")
    manager1.add_employee(employee1)
    manager1.add_employee(employee3)

    manager2 = Manager(5, "Joy Rogers", "Sales", "Sales Manager", 55000, 40, "1983-12-12", "LMN789")
    manager2.add_employee(employee2)

    # Add employees to the system
    system.add_employee(employee1)
    system.add_employee(employee2)
    system.add_employee(employee3)
    system.add_employee(manager1)
    system.add_employee(manager2)

    # Create Clients
    client1 = Client(1, "John Doe", "123 Main St", "555-1234", 5000)
    client2 = Client(2, "Jane Smith", "456 Oak Ave", "555-5678", 7000)
    system.add_client(client1)
    system.add_client(client2)

    # Create Suppliers
    supplier1 = Supplier(1, "ABC Catering", "789 Elm Rd", "555-7890", "Catering", 50, 300)
    supplier2 = Supplier(2, "XYZ Cleaning", "123 Cedar St", "555-0123", "Cleaning", 10, 200)
    system.add_supplier(supplier1)
    system.add_supplier(supplier2)

    # Create a Venue
    venue1 = Venue(1, "Grand Hall", "321 Birch Rd", "555-3456", 100, 500)
    system.add_venue(venue1)

    # Create a Caterer
    caterer1 = Caterer(1, "Caterer 1", "111 Nour Rd", "555-1234", "some dashes", 150, 600)
    system.add_caterer(caterer1)

    # Create Events
    event1 = Event(1, "Wedding", "Traditional", "2024-05-20", "18:00", 6, "Grand Hall", 1, [], 1, 2, 3, 4, 5, 5000)
    system.add_event(event1)

    # Save the system to binary
    system.save_to_binary("event_system.pkl")

#    # Load the system from binary
#    loaded_system = EventsCompanySystem.load_from_binary("event_system.pkl")
#    if loaded_system:
#        print("System loaded successfully from binary.")
#        loaded_system.display_All()
#    else:
#        print("Failed to load the system from binary.")

# Run the test
test_system()
