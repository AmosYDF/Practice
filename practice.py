class Route:
    def __init__(self, start_state, end_state):
        self.start_state = start_state
        self.end_state = end_state

    def __str__(self):
        return f"{self.start_state} to {self.end_state}"

class Vehicle:
    def __init__(self, name, price, vehicle_type, routes):
        self.name = name
        self.price = price
        self.vehicle_type = vehicle_type
        self.routes = routes

    def __str__(self):
        return f"{self.name} - {self.price:,.0f} Naira ({self.vehicle_type} Bus)"

class BusBoardingSystem:
    def __init__(self):
        self.routes = [
            Route("Lagos", "Abuja"),
            Route("Lagos", "Ibandan"),
            Route("Lagos", "Ilorin"),
            Route("Lagos", "Oshogbo"),
        ]

        self.vehicles = [
            Vehicle("Luxury Car", 15000, "Day", self.routes),
            Vehicle("Standard Car", 10000, "Day", self.routes),
            Vehicle("Luxury Bus", 8000, "Night", self.routes),
            Vehicle("Standard Bus", 17000, "Night", self.routes),
        ]
    
    def display_vehicles(self,vehicle_type):
        print(f"Available Vehicle for {vehicle_type} service:")
        for index, vehicle in enumerate(self.vehicles, start=1):
            if vehicle.vehicle_type == vehicle_type:
                print(f"{index}. {vehicle}")
    
    def display_routes(self):
        print("Available Routes:")
        for index, route in enumerate(self.routes, start=1):
            print(f"{index}. {route}")

    def book_vehicle(self, vehicle, route):
        print(f"You have successfully booked the {vehicle.name} from {route} for {vehicle.price:,.0f} Naira.")

def main():
    system = BusBoardingSystem()
    system.display_routes()

    try:
        route_choice = int(input("Please select a route by number (0 to exit): "))
        if route_choice == 0:
            print("Exiting the system. Thank you!")
            return
        
        selected_route = system.routes[route_choice - 1]
        Time_of_Day = input("Would you like a 'Day or 'Night' service?").strip().capitalize()

        if Time_of_Day not in ["Day", "Night"]:
            print("Invalid time of day. Please enter 'Day' or 'Night'.")
            return

        system.display_vehicles(Time_of_Day)
        vehicle_choice = int(input("Please slect a vehicle by number: "))
        vehicle = system.vehicles[vehicle_choice - 1]

        if vehicle.vehicle_type != Time_of_Day:
            print(f"The selected vehicle is not available for {Time_of_Day} service.")
            return

        system.book_vehicle(vehicle, selected_route)

    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Invalid choice. Please select a valid vehicle or route number. ")

if __name__ == "__main__":
    main()
