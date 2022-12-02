items = {}
total_amount = 0

def market():
    global total_amount
    status = True
    while status:
        print("---------------Welcome to fruit Market------------")
        print(" ")
        print("Select Your Role:")
        print("\t 1) Manager")
        print("\t 2) Customer")

        Role1 = int(input("Select Your Role: "))
        print(Role1)
                
        market_manager = True
        while market_manager:
            if Role1 == 1:
                print("\t Fruit Market Manager")
                print(" ")
                print("\t 1) Add Fruit Stock")
                print("\t 2) View Fruit Stock")
                print("\t 3) Update Fruit Stock")
                print("\t 4) Return to main menu")
                choice = int(input("Enter your choice: "))
                print(choice)

                if choice == 1:
                    fruit_name = input("Enter Fruit Name: ")
                    fruit_qty = int(input("Enter qty(in kg): "))
                    fruit_price = int(input("Enter Price(in kg): "))
                    items.update([(fruit_name,(fruit_qty,fruit_price))])
                    operation = input("Do you want to more operations : Press y for yes and n for NO: ")
                    if operation=='y':
                        market_manager = True
                    elif operation=='n':
                        market_manager = False
                elif choice==2:
                    print(items)
                elif choice==3:
                    print(items)
                elif choice==4:
                    break

            
            elif Role1==2:
                Jignesh_store = True
                while Jignesh_store:
                    print("\t Welcome to the Jignesh Store")
                    print(" ")
                    customer_fruit = input("Enter Fruit Name: ")
                    customer_qty = int(input("Enter qty(in kg): "))
                    customer_rate = int(input("Enter Rate of Fruit: "))
                    customer_amount = customer_qty*customer_rate
                    total_amount += customer_amount
                    
                    if customer_fruit in items.keys():
                        print("Fruit:-     ", customer_fruit)
                        print("Quantity:-  ",customer_qty)
                        print("Rate:-      ", customer_rate)
                        print("Amount:-    ", total_amount)
                        asking = input("Do you want to add more, Press y for Yes and N for No: ")

                        if asking == 'y':
                            Jignesh_store = True
                        else:
                            print("Your final amount is: \n", total_amount)
                            print("Thank you for visiting Jignesh Store \n")
                            print("See You Soon\n")
                            break
                    else:
                        print("Sorry Stock is not available")
                Jignesh_store = False        

    status = False
market()
    




            




        



    
    
