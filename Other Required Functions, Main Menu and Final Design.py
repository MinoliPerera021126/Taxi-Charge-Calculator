# This Section is Allocated to Develop Functions needed for the system.
def main_menu():
    print("\nSelect Your Role:\n1 - Customer\n2 - Driver\n3 - Admin\n")


def admin_sub_menu():
    print("\n1 - Add Data\n2 - Change Data\n3 - Delete Data")


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


def add_data():
    global vehicle_type
    global vehicle_charge

    # Getting user input for the update
    update_vehicle_type = input("\nEnter the vehicle type want be added to the table: ")
    update_vehicle_charge = int(input("Enter the charge for the vehicle: "))

    # process
    vehicle_type.append(update_vehicle_type)
    vehicle_charge.append(update_vehicle_charge)


def change_data():
    global vehicle_charge

    # Getting user input for the update
    search_by_serial_no = int(input("\nEnter the Serial No. of the Record: "))
    while not ((search_by_serial_no - 1) in range(len(vehicle_charge))):
        print("Invalid Serial No. Try Again.")
        search_by_serial_no = int(input("\nEnter the Serial No. of the Record: "))

    index_of_the_record = vehicle_charge.index(vehicle_charge[search_by_serial_no - 1])

    new_data = input("Enter the vehicle charge: ")
    vehicle_charge[index_of_the_record] = new_data


def delete_data():
    search_by_serial_no = int(input("\nEnter the Serial No. of the Record: "))
    while not ((search_by_serial_no - 1) in range(len(vehicle_type))):
        print("\nInvalid Serial No. Try Again.")
        search_by_serial_no = int(input("\nEnter the Serial No. of the Record: "))

    # Preview of the record and asking for confirmation.
    print("|---------------|-----------------------|-------------------------------|")
    print("|  Serial No.\t|\tVehicle Type\t|\tCharges per Km (Rs.)\t|")
    print("|---------------|-----------------------|-------------------------------|")
    print(
        f"|\t{search_by_serial_no}\t|\t{vehicle_type[search_by_serial_no - 1]}\t\t|\t\t{vehicle_charge[search_by_serial_no - 1]}.00\t\t|")
    print("|---------------|-----------------------|-------------------------------|")

    confirmation = int(input("\nConfirm Deletion\n(Press 0 for No and 1 for Yes): "))
    while not (confirmation == 0 or confirmation == 1):
        print("\nInvalid Input. Try Again.")
        confirmation = int(input("\nConfirm Deletion\n(Press 0 for No and 1 for Yes): "))
        if (confirmation == 0):
            print("\nYou will be directed to the Admin menu.")
            while not (operation_user_input == 1 or operation_user_input == 2 or operation_user_input == 3):
                print("Invalid Input. Try Again.")
                operation_user_input = int(input("\nEnter the number of the operation: "))
        else:
            # Process
            vehicle_type.remove(vehicle_type[search_by_serial_no - 1])
            vehicle_charge.remove(vehicle_charge[search_by_serial_no - 1])


def asking_for_repeatition_of_the_operation():
    global ask
    while not (ask == 0 or ask == 1):
        print("\nInvalid Input. Try Again.")
        ask = int(input("\nYou want to repeat the operation?\n(Press 0 for No and 1 for Yes): "))


def response():
    print("\nDatabase Updated Successfully.\n")
    print_table()


# End of the function development


# User Interface
print("Welcome to TripTally!")

main_menu()
role_user_input = int(input("Enter Role Number Here: "))

while not (role_user_input == 1 or role_user_input == 2 or role_user_input == 3):
    print("Invalid Input. Try Again.\n")
    main_menu()
    role_user_input = int(input("Enter Role Number Here: "))

else:
    while (role_user_input == 1 or role_user_input == 2):
        print("\nTaxi Charge Calculator")
        proceed_confirmation = int(input("\nDo You Want to Proceed?\n(Press 0 for No and 1 for Yes): "))
        while (proceed_confirmation == 0):
            print("\nYou will be directed to the main menu.")
            main_menu()
            role_user_input = int(input("Enter Role Number Here: "))
            print("\nTaxi Charge Calculator")
            proceed_confirmation = int(input("\nDo You Want to Proceed?\n(Press 0 for No and 1 for Yes): "))

        if (proceed_confirmation == 1):
            taxi_charge_calculator()

        ask = int(input("\nYou want to repeat the operation?\n(Press 0 for No and 1 for Yes): "))
        asking_for_repeatition_of_the_operation()
        while (ask == 1):
            taxi_charge_calculator()
            ask = int(input("\nYou want to repeat the operation?\n(Press 0 for No and 1 for Yes): "))
            asking_for_repeatition_of_the_operation()
        else:
            print("\nYou will be directed to the main menu.")
            main_menu()
            role_user_input = int(input("Enter Role Number Here: "))

    else:
        print("\nUpdate Database")
        proceed_confirmation = int(input("\nDo You Want to Proceed?\n(Press 0 for No and 1 for Yes): "))
        while (proceed_confirmation == 0):
            print("\nYou will be directed to the main menu.")
            main_menu()
            role_user_input = int(input("Enter Role Number Here: "))
            while not (role_user_input == 1 or role_user_input == 2 or role_user_input == 3):
                print("Invalid Input. Try Again.\n")
                role_user_input = int(input("Enter Role Number Here: "))
            else:
                print("\nUpdate Database")
                proceed_confirmation = int(input("\nDo You Want to Proceed?\n(Press 0 for No and 1 for Yes): "))

        else:
            print_table()
            admin_sub_menu()
            operation_user_input = int(input("\nEnter the number of the operation: "))
            while not (operation_user_input == 1 or operation_user_input == 2 or operation_user_input == 3):
                print("\nInvalid Input. Try Again.\n")
                admin_sub_menu()
                operation_user_input = int(input("\nEnter the number of the operation: "))

            while (operation_user_input == 1):
                add_data()
                ask = int(input("\nYou want to repeat the operation?\n(Press 0 for No and 1 for Yes): "))
                asking_for_repeatition_of_the_operation()
                while (ask == 1):
                    add_data()
                    ask = int(input("\nYou want to repeat the operation?\n(Press 0 for No and 1 for Yes): "))
                    asking_for_repeatition_of_the_operation()
                else:
                    response()
                    print("\n\nYou will be directed to the Admin menu")
                    admin_sub_menu()
                    operation_user_input = int(input("\nEnter the number of the operation: "))

            else:
                while (operation_user_input == 2):
                    print("\nVehicle Charge Table")
                    proceed_confirmation = int(input("\nDo You Want to Proceed?\n(Press 0 for No and 1 for Yes): "))
                    while (proceed_confirmation == 0):
                        print("\nYou will be directed to the Admin menu.")
                        admin_sub_menu()
                        operation_user_input = int(input("\nEnter the number of the operation: "))
                        while not (operation_user_input == 1 or operation_user_input == 2 or operation_user_input == 3):
                            print("Invalid Input. Try Again.\n")
                            operation_user_input = int(input("\nEnter the number of the operation: "))
                    else:
                        change_data()
                        ask = int(input("\nYou want to repeat the operation?\n(Press 0 for No and 1 for Yes): "))
                        asking_for_repeatition_of_the_operation()
                        while (ask == 1):
                            change_data()
                            ask = int(input("\nYou want to repeat the operation?\n(Press 0 for No and 1 for Yes): "))
                            asking_for_repeatition_of_the_operation()
                        else:
                            response()
                            print("\nYou will be directed to the Admin menu")
                            admin_sub_menu()
                            operation_user_input = int(input("\nEnter the number of the operation: "))

                else:
                    delete_data()
                    ask = int(input("\nYou want to repeat the operation?\n(Press 0 for No and 1 for Yes): "))
                    asking_for_repeatition_of_the_operation()
                    while (ask == 1):
                        delete_data()
                        ask = int(input("\nYou want to repeat the operation?\n(Press 0 for No and 1 for Yes): "))
                        asking_for_repeatition_of_the_operation()
                    else:
                        response()
                        print("\nYou will be directed to the Admin menu")
                        admin_sub_menu()
                        operation_user_input = int(input("\nEnter the number of the operation: "))