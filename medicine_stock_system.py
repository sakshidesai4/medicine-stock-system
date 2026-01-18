import datetime
import os

FILE_NAME = "medicines.txt"

# ---------------- Helper Functions ----------------

def load_medicines():
    medicines = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, qty, exp = line.strip().split(",")
                medicines.append({
                    "name": name,
                    "quantity": int(qty),
                    "expiry": exp
                })
    return medicines


def save_medicines(medicines):
    with open(FILE_NAME, "w") as file:
        for med in medicines:
            file.write(f"{med['name']},{med['quantity']},{med['expiry']}\n")


# ---------------- Core Functions ----------------

def add_medicine(medicines):
    name = input("Enter Medicine Name: ")
    quantity = int(input("Enter Quantity: "))
    expiry = input("Enter Expiry Date (DD-MM-YYYY): ")

    medicines.append({
        "name": name,
        "quantity": quantity,
        "expiry": expiry
    })

    save_medicines(medicines)
    print("Medicine Added Successfully!")


def view_medicines(medicines):
    if not medicines:
        print("No medicines available.")
        return

    print("\nAvailable Medicines:")
    for med in medicines:
        print(f"Name: {med['name']} | Quantity: {med['quantity']} | Expiry: {med['expiry']}")


def update_medicine(medicines):
    name = input("Enter Medicine Name to Update: ")
    for med in medicines:
        if med["name"].lower() == name.lower():
            med["quantity"] = int(input("Enter New Quantity: "))
            med["expiry"] = input("Enter New Expiry Date (DD-MM-YYYY): ")
            save_medicines(medicines)
            print("Medicine Updated Successfully!")
            return
    print("Medicine not found.")


def delete_medicine(medicines):
    name = input("Enter Medicine Name to Delete: ")
    for med in medicines:
        if med["name"].lower() == name.lower():
            medicines.remove(med)
            save_medicines(medicines)
            print("Medicine Deleted Successfully!")
            return
    print("Medicine not found.")


def check_expiry_alerts(medicines):
    today = datetime.date.today()
    print("\nExpiry Alerts (Within 30 Days):")

    found = False
    for med in medicines:
        exp_date = datetime.datetime.strptime(med["expiry"], "%d-%m-%Y").date()
        days_left = (exp_date - today).days

        if days_left <= 30:
            print(f"ALERT: {med['name']} expires on {med['expiry']}")
            found = True

    if not found:
        print("No medicines nearing expiry.")


# ---------------- Main Menu ----------------

def main():
    medicines = load_medicines()

    while True:
        print("\n===== Medicine Stock System =====")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Update Medicine")
        print("4. Delete Medicine")
        print("5. Check Expiry Alerts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_medicine(medicines)
        elif choice == "2":
            view_medicines(medicines)
        elif choice == "3":
            update_medicine(medicines)
        elif choice == "4":
            delete_medicine(medicines)
        elif choice == "5":
            check_expiry_alerts(medicines)
        elif choice == "6":
            print("Exiting Medicine Stock System...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()