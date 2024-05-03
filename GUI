import tkinter as tk
from tkinter import messagebox
import pickle
from sen import *

class EventsCompanyApp(tk.Tk):
    global system
    system = EventsCompanySystem.load_from_binary("event_system.pkl")
    def __init__(self):
        super().__init__()
        self.title("The Best Events Company Management System")

        # Basic frame for navigation
        self.nav_frame = tk.Frame(self)
        self.nav_frame.pack()

        self.nav_buttons = {
            "Add Employee": self.add_employee,
            "Delete Employee": self.del_employee,
            "Modify Employee": self.select_employee_to_modify,
            "Display Employee": self.display_employee,
            "Add Event": self.add_event,
#            "Delete Event": self.del_event,
#            "Modify Event": self.modify_event,
            "Display Event": self.display_event,
            "Add Client": self.add_client,
#            "Delete Client": self.del_client,
#            "Modify Client": self.modify_client,
            "Display Client": self.display_client,
#            "Add Guest": self.add_guest,
##            "Delete Guest": self.del_guest,
##            "Modify Guest": self.modify_guest,
#            "Display Guest": self.display_guest,
#            "Add Supplier": self.add_supplier,
##            "Delete Supplier": self.del_supplier,
##            "Modify Supplier": self.modify_supplier,
#            "Display Supplier": self.display_supplier,
            "Display All": self.display_system,
            "Save": self.save_system,
            "Exit": self.quit
        }

        for button_text, command in self.nav_buttons.items():
            btn = tk.Button(self.nav_frame, text=button_text, command=command)
            btn.pack(side=tk.LEFT)

    def add_employee(self):
        # GUI to add an employee
        add_employee_window = tk.Toplevel(self)
        add_employee_window.title("Add Employee")

        # Employee ID
        lbl_emp_id = tk.Label(add_employee_window, text="Employee ID:")
        lbl_emp_id.pack()
        txt_emp_id = tk.Entry(add_employee_window)
        txt_emp_id.pack()

        # Employee Name
        lbl_emp_name = tk.Label(add_employee_window, text="Employee Name:")
        lbl_emp_name.pack()
        txt_emp_name = tk.Entry(add_employee_window)
        txt_emp_name.pack()

        # Department
        lbl_department = tk.Label(add_employee_window, text="Department:")
        lbl_department.pack()
        txt_department = tk.Entry(add_employee_window)
        txt_department.pack()

        # Job Title
        lbl_job_title = tk.Label(add_employee_window, text="Job Title:")
        lbl_job_title.pack()
        txt_job_title = tk.Entry(add_employee_window)
        txt_job_title.pack()

        # Basic Salary
        lbl_basic_salary = tk.Label(add_employee_window, text="Basic Salary:")
        lbl_basic_salary.pack()
        txt_basic_salary = tk.Entry(add_employee_window)
        txt_basic_salary.pack()

        # Age
        lbl_age = tk.Label(add_employee_window, text="Age:")
        lbl_age.pack()
        txt_age = tk.Entry(add_employee_window)
        txt_age.pack()

        # Date of Birth
        lbl_dob = tk.Label(add_employee_window, text="Date of Birth:")
        lbl_dob.pack()
        txt_dob = tk.Entry(add_employee_window)
        txt_dob.pack()

        # Passport Details
        lbl_passport_details = tk.Label(add_employee_window, text="Passport Details:")
        lbl_passport_details.pack()
        txt_passport_details = tk.Entry(add_employee_window)
        txt_passport_details.pack()

        # Button to add the employee
        btn_add_emp = tk.Button(add_employee_window, text="Add", command=lambda: self.save_employee(
            1, txt_emp_id.get(),
            txt_emp_name.get(),
            txt_department.get(),
            txt_job_title.get(),
            txt_basic_salary.get(),
            txt_age.get(),
            txt_dob.get(),
            txt_passport_details.get()
        ))
        btn_add_emp.pack()

    def select_employee_to_modify(self):
        # GUI to modify an employee based on ID
        modify_employee_window = tk.Toplevel(self)
        modify_employee_window.title("Modify Employee")

        # Employee ID
        lbl_emp_id = tk.Label(modify_employee_window, text="Employee ID:")
        lbl_emp_id.pack()
        txt_emp_id = tk.Entry(modify_employee_window)
        txt_emp_id.pack()

        btn_modify_emp = tk.Button(modify_employee_window, text="Modify", command=lambda: self.modify_employee(txt_emp_id.get()))
        btn_modify_emp.pack()

    def modify_employee(self, emp_id):
        emp_id = int(emp_id)
        emp = system.display_employee(emp_id)
        self.del_emp(emp_id)
        # GUI to modify an employee
        modify_employee_window = tk.Toplevel(self)
        modify_employee_window.title("Modify Employee")

        # Employee ID
        lbl_emp_id = tk.Label(modify_employee_window, text="Employee ID:")
        lbl_emp_id.pack()
        txt_emp_id = tk.Entry(modify_employee_window)
        txt_emp_id.insert(0, emp.employee_id)
        txt_emp_id.pack()

        # Employee Name
        lbl_emp_name = tk.Label(modify_employee_window, text="Employee Name:")
        lbl_emp_name.pack()
        txt_emp_name = tk.Entry(modify_employee_window)
        txt_emp_name.insert(0, emp.name)
        txt_emp_name.pack()

        # Department
        lbl_department = tk.Label(modify_employee_window, text="Department:")
        lbl_department.pack()
        txt_department = tk.Entry(modify_employee_window)
        txt_department.insert(0, emp.department)
        txt_department.pack()

        # Job Title
        lbl_job_title = tk.Label(modify_employee_window, text="Job Title:")
        lbl_job_title.pack()
        txt_job_title = tk.Entry(modify_employee_window)
        txt_job_title.insert(0, emp.job_title)
        txt_job_title.pack()

        # Basic Salary
        lbl_basic_salary = tk.Label(modify_employee_window, text="Basic Salary:")
        lbl_basic_salary.pack()
        txt_basic_salary = tk.Entry(modify_employee_window)
        txt_basic_salary.insert(0, emp.basic_salary)
        txt_basic_salary.pack()

        # Age
        lbl_age = tk.Label(modify_employee_window, text="Age:")
        lbl_age.pack()
        txt_age = tk.Entry(modify_employee_window)
        txt_age.insert(0, emp.age)
        txt_age.pack()

        # Date of Birth
        lbl_dob = tk.Label(modify_employee_window, text="Date of Birth:")
        lbl_dob.pack()
        txt_dob = tk.Entry(modify_employee_window)
        txt_dob.insert(0, emp.dob)
        txt_dob.pack()

        # Passport Details
        lbl_passport_details = tk.Label(modify_employee_window, text="Passport Details:")
        lbl_passport_details.pack()
        txt_passport_details = tk.Entry(modify_employee_window)
        txt_passport_details.insert(0, emp.passport_details)
        txt_passport_details.pack()

        # Button to add the employee
        btn_add_emp = tk.Button(modify_employee_window, text="Modify", command=lambda: self.save_employee(
            2, txt_emp_id.get(),
            txt_emp_name.get(),
            txt_department.get(),
            txt_job_title.get(),
            txt_basic_salary.get(),
            txt_age.get(),
            txt_dob.get(),
            txt_passport_details.get()
        ))
        btn_add_emp.pack()

    def save_employee(self, stat, emp_id, emp_name, department, job_title, basic_salary, age, dob, passport_details):
        try:
            emp_id = int(emp_id)
            basic_salary = float(basic_salary)
            age = int(age)

            employee = Employee(emp_id, emp_name, department, job_title, basic_salary, age, dob, passport_details)
            system.add_employee(employee)
            if(stat == 1):
                messagebox.showinfo("Success", "Employee added successfully.")
            else:
                messagebox.showinfo("Success", "Employee modify successfully.")                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add employee: {e}")

    def del_employee(self):
        # GUI to delete an employee based on ID
        del_employee_window = tk.Toplevel(self)
        del_employee_window.title("Delete Employee")

        # Employee ID
        lbl_emp_id = tk.Label(del_employee_window, text="Employee ID:")
        lbl_emp_id.pack()
        txt_emp_id = tk.Entry(del_employee_window)
        txt_emp_id.pack()

        btn_del_emp = tk.Button(del_employee_window, text="Delete", command=lambda: self.del_emp(txt_emp_id.get()))
        btn_del_emp.pack()

    def del_emp(self, emp_id):
        try:
            emp_id = int(emp_id)
            system.remove_employee(system.display_employee(emp_id))
            messagebox.showinfo("Employee Deleted", f"Employee {emp_id} Deleted")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete employee: {e}")
        
    def display_employee(self):
        # GUI to display an employee based on ID
        display_employee_window = tk.Toplevel(self)
        display_employee_window.title("Display Employee")

        # Employee ID
        lbl_emp_id = tk.Label(display_employee_window, text="Employee ID:")
        lbl_emp_id.pack()
        txt_emp_id = tk.Entry(display_employee_window)
        txt_emp_id.pack()

        btn_display_emp = tk.Button(display_employee_window, text="Display", command=lambda: self.show_employee(
            txt_emp_id.get()
        ))
        btn_display_emp.pack()
        
    def show_employee(self, emp_id):
        try:
            emp_id = int(emp_id)
            employee = system.display_employee(emp_id)
            if employee:
                messagebox.showinfo("Employee Details", f"{employee}")
            else:
                messagebox.showerror("Error", "Employee not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display employee: {e}")

    def add_client(self):
        # GUI to add a client
        add_client_window = tk.Toplevel(self)
        add_client_window.title("Add Client")

        # Client ID
        lbl_client_id = tk.Label(add_client_window, text="Client ID:")
        lbl_client_id.pack()
        txt_client_id = tk.Entry(add_client_window)
        txt_client_id.pack()

        # Client Name
        lbl_client_name = tk.Label(add_client_window, text="Client Name:")
        lbl_client_name.pack()
        txt_client_name = tk.Entry(add_client_window)
        txt_client_name.pack()

        # Address
        lbl_address = tk.Label(add_client_window, text="Address:")
        lbl_address.pack()
        txt_address = tk.Entry(add_client_window)
        txt_address.pack()

        # Contact Details
        lbl_contact_details = tk.Label(add_client_window, text="Contact Details:")
        lbl_contact_details.pack()
        txt_contact_details = tk.Entry(add_client_window)
        txt_contact_details.pack()

        # Budget
        lbl_budget = tk.Label(add_client_window, text="Budget:")
        lbl_budget.pack()
        txt_budget = tk.Entry(add_client_window)
        txt_budget.pack()

        # Button to add the client
        btn_add_client = tk.Button(add_client_window, text="Add", command=lambda: self.save_client(
            txt_client_id.get(),
            txt_client_name.get(),
            txt_address.get(),
            txt_contact_details.get(),
            txt_budget.get()
        ))
        btn_add_client.pack()

    def save_client(self, client_id, client_name, address, contact_details, budget):
        try:
            client_id = int(client_id)
            budget = float(budget)

            client = Client(client_id, client_name, address, contact_details, budget)
            system.add_client(client)
            messagebox.showinfo("Success", "Client added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add client: {e}")

    def display_client(self):
        # GUI to display a client based on ID
        display_client_window = tk.Toplevel(self)
        display_client_window.title("Display Client")

        # Client ID
        lbl_client_id = tk.Label(display_client_window, text="Client ID:")
        lbl_client_id.pack()
        txt_client_id = tk.Entry(display_client_window)
        txt_client_id.pack()

        btn_display_client = tk.Button(display_client_window, text="Display", command=lambda: self.show_client(
            txt_client_id.get()
        ))
        btn_display_client.pack()

    def show_client(self, client_id):
        try:
            client_id = int(client_id)
            client = system.display_client(client_id)
            if client:
                messagebox.showinfo("Client Details", f"{client}")
            else:
                messagebox.showerror("Error", "Client not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display client: {e}")

    def add_event(self):
        # GUI to add an event
        add_event_window = tk.Toplevel(self)
        add_event_window.title("Add Event")

        # Event ID
        lbl_event_id = tk.Label(add_event_window, text="Event ID:")
        lbl_event_id.pack()
        txt_event_id = tk.Entry(add_event_window)
        txt_event_id.pack()

        # Event Type
        lbl_event_type = tk.Label(add_event_window, text="Event Type:")
        lbl_event_type.pack()
        txt_event_type = tk.Entry(add_event_window)
        txt_event_type.pack()

        # Theme
        lbl_theme = tk.Label(add_event_window, text="Theme:")
        lbl_theme.pack()
        txt_theme = tk.Entry(add_event_window)
        txt_theme.pack()

        # Date
        lbl_date = tk.Label(add_event_window, text="Date:")
        lbl_date.pack()
        txt_date = tk.Entry(add_event_window)
        txt_date.pack()

        # Time
        lbl_time = tk.Label(add_event_window, text="Time:")
        lbl_time.pack()
        txt_time = tk.Entry(add_event_window)
        txt_time.pack()

        # Duration
        lbl_duration = tk.Label(add_event_window, text="Duration:")
        lbl_duration.pack()
        txt_duration = tk.Entry(add_event_window)
        txt_duration.pack()

        # Venue Address
        lbl_venue_address = tk.Label(add_event_window, text="Venue Address:")
        lbl_venue_address.pack()
        txt_venue_address = tk.Entry(add_event_window)
        txt_venue_address.pack()

        # Client ID
        lbl_client_id = tk.Label(add_event_window, text="Client ID:")
        lbl_client_id.pack()
        txt_client_id = tk.Entry(add_event_window)
        txt_client_id.pack()

        # Catering Company
        lbl_catering_company = tk.Label(add_event_window, text="Catering Company:")
        lbl_catering_company.pack()
        txt_catering_company = tk.Entry(add_event_window)
        txt_catering_company.pack()

        # Button to add the event
        btn_add_event = tk.Button(add_event_window, text="Add", command=lambda: self.save_event(
            txt_event_id.get(),
            txt_event_type.get(),
            txt_theme.get(),
            txt_date.get(),
            txt_time.get(),
            txt_duration.get(),
            txt_venue_address.get(),
            txt_client_id.get(),
            txt_catering_company.get()
        ))
        btn_add_event.pack()

    def save_event(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, catering_company):
        try:
            event_id = int(event_id)

            event = Event(
                event_id,
                event_type,
                theme,
                date,
                time,
                duration,
                venue_address,
                client_id,
                catering_company,
            )
            system.add_event(event)
            messagebox.showinfo("Success", "Event added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add event: {e}")

    def display_event(self):
        # GUI to display an event based on ID
        display_event_window = tk.Toplevel(self)
        display_event_window.title("Display Event")

        # Event ID
        lbl_event_id = tk.Label(display_event_window, text="Event ID:")
        lbl_event_id.pack()
        txt_event_id = tk.Entry(display_event_window)
        txt_event_id.pack()

        btn_display_event = tk.Button(display_event_window, text="Display", command=lambda: self.show_event(
            txt_event_id.get()
        ))
        btn_display_event.pack()

    def show_event(self, event_id):
        try:
            event_id = int(event_id)
            event = system.display_event(event_id)
            if event:
                messagebox.showinfo("Event Details", f"{event}")
            else:
                messagebox.showerror("Error", "Event not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display event: {e}")

    def display_system(self):
        str = "\nThe Employees:"
        for employee in system.employees:
            str += "\n" + employee.get()
        str += "\n\nThe Clients:"
        for client in system.clients:
            str += "\n" + client.get()
        str += "\n\nThe Events:"
        for event in system.events:
            str += "\n" + event.get()
        str += "\n\nThe Suppliers:"
        for supplier in system.suppliers:
            str += "\n" + supplier.get()
        str += "\n\nThe Venues:"
        for venue in system.venues:
            str += "\n" + venue.get()
        str += "\n\nThe Guests:"
        for guest in system.guests:
            str += "\n" + guest.get()
        str += "\n\nThe Caterers:"
        for caterer in system.caterers:
            str += "\n" + caterer.get()
        messagebox.showinfo("System Data", str)

    def save_system(self):
        try:
            system.save_to_binary("event_system.pkl")
            messagebox.showinfo("Success", "System saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the system: {e}")

# Run the application
if __name__ == "__main__":
    app = EventsCompanyApp()
    app.mainloop()
