# Database for further functions
vehicle_type = ["Car", "Van", "Lorry", "3-Wheel", "Bike"]
vehicle_charge = [80, 70, 100, 60, 40]
vehicle_condition = ["Non-AC", "AC"]  # This array is created only for the purpose of output
additional_charge = 80


def print_table():
    print("|---------------|-----------------------|-------------------------------|")
    print("|  Serial No.\t|\tVehicle Type\t|\tCharges per Km (Rs.)\t|")
    print("|---------------|-----------------------|-------------------------------|")

    for i in range(len(vehicle_type)):
        print(f"|\t{i + 1}\t|\t{vehicle_type[i]}\t\t|\t\t{vehicle_charge[i]}.00\t\t|")

    print("|---------------|-----------------------|-------------------------------|")


def taxi_charge_calculator():
    # Charge Table
    global vehicle_type
    global vehicle_charge
    global vehicle_condition
    print_table()
    print(f"Please note that additional Rs.{additional_charge}.00 will be added for AC vehicles.\n")

    # Getting user inputs to calculate the charge
    vehicle_type_user_input = int(
        input("\nVehicle Type\n(Enter the Serial No. of the preferred Vehicle Type): "))  # Vehicle Type
    while not ((vehicle_type_user_input - 1) in range(len(vehicle_type))):
        print("\nInvalid Input. Please Try Again.")
        vehicle_type_user_input = int(input("\nVehicle Type\n(Enter the Serial No. of the preferred Vehicle Type): "))

    if (vehicle_type_user_input == 4 or vehicle_type_user_input == 5):  # Vehicle Condition
        vehicle_condition_user_input = 0
    else:
        vehicle_condition_user_input = int(input("\nVehicle Condition\n(Press 0 for Non-AC and 1 for AC): "))
        while not (vehicle_condition_user_input == 0 or vehicle_condition_user_input == 1):
            print("\nInvalid Input. Please Try Again.")
            vehicle_condition_user_input = int(input("\nVehicle Condition\n(Press 0 for Non-AC and 1 for AC): "))

    total_distance_travelled_user_input = int(
        input("\nTotal Distance Travelled (Km.)\n(Enter the total distance): "))  # Total Distance Travelled
    while not (total_distance_travelled_user_input > 0):
        print("\nInvalid Input. Please Try Again.")
        total_distance_travelled_user_input = int(
            input("\nTotal Distance Travelled (Km.)\n(Enter the total distance): "))

    # Calculation
    for i in range(len(vehicle_type)):
        if (vehicle_type_user_input == i + 1):
            if (vehicle_condition_user_input == 0):
                total_charge = vehicle_charge[i] * total_distance_travelled_user_input

            elif (vehicle_condition_user_input == 1):
                total_charge = (vehicle_charge[i] + 80) * total_distance_travelled_user_input

    # output
    print(
        f"\nPreferred Vehicle Type: {vehicle_type[vehicle_type_user_input - 1]}\nPreferred Vehicle Condition: {vehicle_condition[vehicle_condition_user_input]}")
    if (vehicle_condition_user_input == 0):
        print(f"Charge Per 1KM: Rs.{vehicle_charge[vehicle_type_user_input - 1]}.00")
    elif (vehicle_condition_user_input == 1):
        print(f"Charge Per 1KM: Rs.{vehicle_charge[vehicle_type_user_input - 1] + 80}.00")
    print(f"Total Distance Travelled: {total_distance_travelled_user_input} KM\nTotal Charge: Rs.{total_charge}.00")


taxi_charge_calculator()