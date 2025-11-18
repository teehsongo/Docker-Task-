'''This program is a shoe inventory management system.
It allows users to read shoe data from a file, capture new shoe data,
view all shoes, restock the lowest quantity shoe, search for a shoe,
calculate the value per item, and find the shoe with the highest quantity.'''


# ========The beginning of the class==========
class Shoe:
    """
    A class to represent a shoe with its associated details.
    Attributes:
        country (str): The country where the shoe is manufactured.
        code (str): The unique code identifying the shoe.
        product (str): The name or description of the shoe product.
        cost (float): The cost of the shoe.
        quantity (int): The quantity of the shoe in stock.
    Methods:
        get_cost():
            Returns the cost of the shoe.
        get_quantity():
            Returns the quantity of the shoe in stock.
        __str__():
            Returns a string representation of the shoe object.
    """

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return (
            f"Country: {self.country}, Code: {self.code}, "
            f"Product: {self.product}, Cost: {self.cost}, "
            f"Quantity: {self.quantity}"
        )

# The list will be used to store a list of objects of shoes.


shoe_list = []


# ==========Functions outside the class==============


def read_shoes_data():
    '''This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file
    represents data to create one object of shoes. You must use the
    try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open('inventory.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines[1:]:  # Skip the first line (header)
                data = line.strip().split(',')
                if len(data) == 5:  # Ensure there are exactly 5 fields
                    country, code, product, cost, quantity = data
                    shoe = Shoe(
                        country, code, product, float(cost), int(quantity)
                    )
                    shoe_list.append(shoe)
                    print(f"\nShoe added: {shoe}")
    except FileNotFoundError:
        print("\nError: The file 'inventory.txt' was not found.")
    except ValueError as e:
        print(f"\nError: Data format issue - {e}")


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("\nEnter the country: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the product name: ")
    try:
        cost = float(input("Enter the cost of the shoe: "))
        quantity = int(input("Enter the quantity of the shoe: "))
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        print("\nShoe successfully added to the inventory.")
    except ValueError:
        print("\nError: Please enter valid numeric "
              "values for cost and quantity.")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''
    if not shoe_list:
        print("\nNo shoes in the inventory.")
        return

    for shoe in shoe_list:
        print(shoe)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    # Find the shoe with the lowest quantity
    if not shoe_list:
        print("\nNo shoes in the inventory to restock.")
        return

    lowest_quantity_shoe = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity < lowest_quantity_shoe.quantity:
            lowest_quantity_shoe = shoe

    print(f"\nThe shoe with the lowest quantity is:\n{lowest_quantity_shoe}")

    try:
        add_quantity = int(input("\nEnter the quantity to add: "))
        if add_quantity < 0:
            print("\nError: Quantity cannot be negative.")
            return

        # Update the quantity
        lowest_quantity_shoe.quantity += add_quantity
        print(
            f"\nUpdated quantity for {lowest_quantity_shoe.product}: "
            f"{lowest_quantity_shoe.quantity}"
        )

        # Update the file
        with open('inventory.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open('inventory.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 5 and data[1] == lowest_quantity_shoe.code:
                    # Update the line with the new quantity
                    data[4] = str(lowest_quantity_shoe.quantity)
                    file.write(','.join(data) + '\n')
                else:
                    file.write(line)

    except ValueError:
        print("\nError: Please enter a valid numeric value for the quantity.")


def search_shoe():
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''
    if not shoe_list:
        print("\nNo shoes in the inventory.")
        return

    search_code = input("\nEnter the shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code == search_code:
            print("Shoe found:")
            print(shoe)
            return

        print("\nShoe with the given code not found.")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    if not shoe_list:
        print("\nNo shoes in the inventory.")
        return

    print("\nValue per item:")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: Value = {value}")


def highest_qty():
    '''
    Determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    if not shoe_list:
        print("\nNo shoes in the inventory.")
        return

# Find the shoe with the highest quantity
    highest_quantity_shoe = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity > highest_quantity_shoe.quantity:
            highest_quantity_shoe = shoe
    print(
        f"\nThe shoe with the highest quantity is:\n{highest_quantity_shoe}"
            )
    print(
        f"{highest_quantity_shoe.product} is available for sale!"
        )

# ==========Main Menu=============


while True:
    print("\nShoe Inventory Management System")
    print("1. Read shoes data from file")
    print("2. Capture new shoe data")
    print("3. View all shoes")
    print("4. Restock the lowest quantity shoe")
    print("5. Search for a shoe by code")
    print("6. Calculate value per item")
    print("7. Find the shoe with the highest quantity")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        read_shoes_data()
    elif choice == '2':
        capture_shoes()
    elif choice == '3':
        view_all()
    elif choice == '4':
        re_stock()
    elif choice == '5':
        search_shoe()
    elif choice == '6':
        value_per_item()
    elif choice == '7':
        highest_qty()
    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
