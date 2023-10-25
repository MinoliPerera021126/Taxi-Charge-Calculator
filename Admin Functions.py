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


add_data()
change_data()
delete_data()