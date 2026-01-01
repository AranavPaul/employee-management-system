import utility

utility.print_logo()
while True:
    utility.print_menu()
    user_input = int(input("Enter your choice:"))

    if user_input == 1:
        utility.check_employee()

    elif user_input == 2:
        utility.adding_employee()

    elif user_input == 3:
        utility.deleting_employee()

    elif user_input == 4:
        utility.get_all_employee()

    elif user_input == 5:
        utility.clear_screen()

    elif user_input == 6:
        exit()
    else:
        print("Wrong Input!")