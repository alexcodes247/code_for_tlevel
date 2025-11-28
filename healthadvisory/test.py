import os
import time
password="password1"
wristband_variable_cost=20
senior_price=11
adult_price=20
child_price=12

def run(): 
    guests=0
    parking_needed = False
    import datetime
    current_time = datetime.datetime.now()
    


    # Introduction
    print("Welcome to Copington Theme Park!")
    print(f"Senior: £{senior_price}, Adult: £{adult_price}, Child: £{child_price}")
    
    # Input number of adults, children, and seniors with input validation
    while True:
        try:
            num_adults = int(input("How many adult tickets are needed: "))
            if num_adults >= 0:
                break
            else:
                print("cant be a minus")
        except:
            print("Invalid input")
    while True:
        try:
            num_children = int(input("How many child tickets are needed: "))
            if num_children >= 0:
                break
            else:
                print("cant be a minus")
        except:
            print("Invalid input")
    while True:
        try:
            num_seniors = int(input("How many senior tickets are needed: "))
            if num_seniors >= 0:
                break
            else:
                print("cant be a minus")
        except:
            print("Invalid input")
    os.system("cls")
    guests=guests+num_adults+num_children+num_seniors
    if guests>500:
        print("we cant let your group in the park its too large")
        run()

# adding the costs of all the tickets and returning it 
    def calculate_entrance_cost(child_count, adult_count, senior_count):
        total_cost = adult_count * adult_price + senior_count * senior_price + child_count * child_price
        return total_cost

#asks for the amount of wristbands and calculates the cost
    def purchase_wristbands():
        while True:
            try:
                wristband_count = int(input(f"Enter number of wristbands £{wristband_variable_cost} each: "))
                if wristband_count>0:
                    break
                else:
                    print("cant be 0 or below")
            except:
                print("Invalid input")
        wristband_cost = wristband_count * wristband_variable_cost
        return wristband_cost

#asks and returns a surname
    def get_surname():
        surname_input = str(input("Enter your surname for ticket: "))
        return surname_input

#seeing if the person needs parking and taking the reg number 
    def handle_parking():
        global parking_needed
        registration_number = input("Press enter for no parking, or enter your registration number for parking: ")
        return registration_number if registration_number else None

#takes the money by them inputing 1 or 2 for 10 and 20 with input validation
    def process_payment(total_cost):
        amount_owed = total_cost
        print(f"Your total cost is: £{amount_owed}")
        print("This machine only accepts £10 or £20 notes.")
        while True:
            while True:
                try:
                    note_choice = int(input("Enter 1 for £10 or 2 for £20: "))
                    break
                except:
                    print("Invalid input")
            if note_choice == 1:
                note_value = 10
            elif note_choice == 2:
                note_value = 20
            else:
                print("Invalid input")
                note_value = 0
            #taking the note away from owed and calulating change 
            amount_owed -= note_value
            os.system("cls")
            if amount_owed>0:
                print(f"You still owe: £{amount_owed}")
            if amount_owed <= 0:
                break
        change_due = abs(amount_owed)
        return change_due

    #printing all the paramaters on the ticket
    def print_ticket():
        print(f"Your ticket for {surname_input}:")
        print(f"Printed on: {current_time}")
        print(f"You have {num_seniors} senior tickets costing: £{num_seniors * senior_price}")
        print(f"You have {num_adults} adult tickets costing: £{num_adults * adult_price}")
        print(f"You have {num_children} child tickets costing: £{num_children * child_price}")
        print(f"You have bought {int(wristband_cost / wristband_variable_cost)} wristbands costing: £{wristband_cost}")
        print(f"Your change is: £{change_due}")
        print("")
        print("Thank you for your purchase!")
        
    #printing the parking ticket with the reg number if its not none     
    def print_parking_ticket():
        if registration_number is not None:
            print("")
            print("Parking ticket:")
            print(f"For registration: {registration_number}")
            print("")
        

    # Main program execution
    surname_input = get_surname()
    os.system("cls")
    entrance_cost = calculate_entrance_cost(num_children, num_adults, num_seniors)
    os.system("cls")
    wristband_cost = purchase_wristbands()
    os.system("cls")
    total_cost = entrance_cost + wristband_cost
    registration_number = handle_parking()
    os.system("cls") 
    change_due = process_payment(total_cost)
    os.system("cls")
    print_ticket()
    print_parking_ticket()
    
def admin_options():
    global wristband_variable_cost
    global senior_price
    global adult_price
    global child_price
    #setting price varables 
    print("Welcome to the admin menue!")
    print("1: wristband price 2:senior price 3:adult price 4:child price")
    while True:
        try:
            which=int(input("enter the number of what you want to edit"))
            break
        except:
            print("invalid input")
    if which == 1:
        while True:
            try:
                wristband_variable_cost=int(input("enter price of wristbands"))
                if wristband_variable_cost>0:
                    break
                else:
                    print("cant be less than 0 (corporate policy)")
            except:
                print("invalid input needs to be an interger")
    elif which == 2:
        while True:
            try:
                senior_price=int(input("enter price of seniors"))
                if senior_price>0:
                    break
                else:
                    print("cant be less than 0 (corporate policy)")
         
            except:
                print("invalid input needs to be an interger")
    elif which == 3:
        while True:
            try:
                adult_price=int(input("enter price of adults"))
                if adult_price>0:
                    break
                else:
                    print("cant be less than 0 (corporate policy)")                

            except:
                print("Invalid input needs to be an interger")
    elif which == 4:
        while True:
            try:
                child_price=int(input("enter price of children"))
                if child_price>0:
                    break
                else:
                    print("cant be less than 0 (corporate policy)")
            except:
                print("Invalid input needs to be an interger")
    else:
        print("invalid number")
    while True:
        try:
            done=input("enter 1 if your done else press enter to continue editing")
            break
        except:
            print("Invalid input")
    if done == "":
        admin_options()
    else:
        print("saving changes..")
        time.sleep(2)
        os.system("cls")
        main()
    
def main():
    # with input vlaidation 1 for regular 2 for admin 
    while True:
        try:
            mode=int(input("enter 1 for customer enter 2 for admin: "))
            break
        except:
            print("invalid input")
    if mode==1:
        run()
    elif mode==2:
        password="password1"
        guesses=3
        penalty=10
        while True:
            passenter=str(input("enter password to enter admin or enter 1 to go back to main menue: "))
            if passenter == "1":
                main()
            if passenter==password:
                print("correct")
                break
            else:
                if guesses>0:
                    print("incorrect")
                    guesses=guesses-1
                    print(f"you have {guesses} strikes left")
                else:
                    print(f"you have a {penalty} second penalty")
                    for i in range(1,penalty+1):
                        print(i)
                        time.sleep(1)
                        os.system("cls")
                    penalty=penalty+10
        admin_options()
    else:
        print("invalid input")

while True:
    main()