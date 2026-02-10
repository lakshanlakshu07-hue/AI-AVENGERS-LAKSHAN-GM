# Parking Availability App (Console Based)

class ParkingLot:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.slots = [None] * total_slots

    def show_status(self):
        print("\nParking Status:")
        for i in range(self.total_slots):
            if self.slots[i] is None:
                print(f"Slot {i + 1}: Available")
            else:
                print(f"Slot {i + 1}: Occupied by {self.slots[i]}")

    def park_vehicle(self, vehicle_number):
        for i in range(self.total_slots):
            if self.slots[i] is None:
                self.slots[i] = vehicle_number
                print(f"Vehicle {vehicle_number} parked at slot {i + 1}")
                return
        print("Sorry! Parking lot is full.")

    def remove_vehicle(self, vehicle_number):
        for i in range(self.total_slots):
            if self.slots[i] == vehicle_number:
                self.slots[i] = None
                print(f"Vehicle {vehicle_number} removed from slot {i + 1}")
                return
        print("Vehicle not found.")


# Main Program
parking = ParkingLot(5)

while True:
    print("\n--- Parking Availability App ---")
    print("1. View Parking Status")
    print("2. Park Vehicle")
    print("3. Remove Vehicle")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        parking.show_status()
    elif choice == "2":
        vehicle_no = input("Enter vehicle number: ")
        parking.park_vehicle(vehicle_no)
    elif choice == "3":
        vehicle_no = input("Enter vehicle number: ")
        parking.remove_vehicle(vehicle_no)
    elif choice == "4":
        print("Thank you for using the Parking App!")
        break
    else:
        print("Invalid choice. Try again.")
