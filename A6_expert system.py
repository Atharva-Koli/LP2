# Assignment No. 6
# Name: Atharva Koli
# Roll No: C33301
# Assignment 6: ES Info Management (with user input)

class InformationManagementExpertSystem:
    def __init__(self):
        self.data = {}

    def add_information(self, key, value):
        self.data[key] = value
        print(f"Information '{key}' added successfully.")

    def get_information(self, key):
        if key in self.data:
            print(f"{key}: {self.data[key]}")
        else:
            print(f"Information '{key}' not found.")

    def remove_information(self, key):
        if key in self.data:
            del self.data[key]
            print(f"Information '{key}' removed successfully.")
        else:
            print(f"Information '{key}' not found.")

    def display_all_information(self):
        if self.data:
            print("All information:")
            for key, value in self.data.items():
                print(f"{key}: {value}")
        else:
            print("No information available.")

# Main Program
expert_system = InformationManagementExpertSystem()

while True:
    print("\n--- Expert System Menu ---")
    print("1. Add Information")
    print("2. Get Information")
    print("3. Remove Information")
    print("4. Display All Information")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        expert_system.add_information(key, value)
    elif choice == '2':
        key = input("Enter the key to retrieve: ")
        expert_system.get_information(key)
    elif choice == '3':
        key = input("Enter the key to remove: ")
        expert_system.remove_information(key)
    elif choice == '4':
        expert_system.display_all_information()
    elif choice == '5':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
