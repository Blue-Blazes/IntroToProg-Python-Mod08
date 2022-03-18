# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KBanfill,3/15/2022,Modified code to complete assignment 8
# KBanfill, 3/16/2022, Modified code to complete assignment 8
# KBanfill, 3/17/2022, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KBanfill,3/15/2022,Modified code to complete assignment 8
        KBanfill, 3/16/2022, Modified code to complete assignment 8
        KBanfill, 3/17/2022, Modified code to complete assignment 8
    """

    # Add Code to the Product class
    # --Fields--

    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --

        self.product_name = (product_name)
        self.product_price = (product_price)


    # -- Properties --
    # Product Name
    @property
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter
    def product_name(self, value):  # (setter or mutator)
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # Product Price
    @property
    def product_price(self):  # (getter or accessor)
        return float(self.__product_price)  # No need for title case since we're working with float values

    @product_price.setter
    def product_price(self, value):  # (setter or mutator)
        try:
            self.__product_price = float(value)
        except:
            raise Exception('Prices cannot be letters')

    # -- Methods --
    def __str__(self):
        return self.product_name + ' | ' + str(self.product_price)  # Turn price back into a string or you receive error


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
        remove_data_from_list(file_name, list_of_rows):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KBanfill,3/15/2022,Modified code to complete assignment 8
        KBanfill, 3/16/2022, Modified code to complete assignment 8
        KBanfill, 3/17/2022, Modified code to complete assignment 8
    """

    # Add Code to process data from a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        try:
            file_obj = open(file_name, "w")
            for row in list_of_product_objects:
                file_obj.write(row.__str__() + "\n")
            file_obj.close()
            print("Data Saved!")
        except Exception as e:
            print('Non-specific error.')
            print('Built-In Python error info: ')
            print(e, e.__doc__, type(e), sep='\n')

    # Add Code to process data to a file
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :return: (list) of rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                product_and_price = line.split(" | ")
                row = Product(product_and_price[0], (product_and_price[1]))
                list_of_rows.append(row)
            file.close()
        except FileNotFoundError:
            print("Error. The file does not exist.")
        except Exception as e:
            print('Non-specific error.')
            print('Built-In Python error info: ')
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

    @staticmethod
    def remove_data_from_list(product_to_remove, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param product: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        for product in list_of_rows:
            if product.product_name.lower() == product_to_remove.lower():
                list_of_rows.remove(product)
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    # Add code to show menu to user
    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('----------Product and Price List----------')
        print('''
           Menu of Options
           1) Show current Products
           2) Add a new Product
           3) Remove an existing Product
           4) Save Data to File        
           5) Exit Program
           ''')
        print()  # Add an extra line for looks

    # Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # Add code to show the current data from the file to user
    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Products in the list of rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* Your current products are: *******")
        for row in list_of_rows:
            print(row.product_name + " | " + str(row.product_price)) #convert price to str or concatenate error
        print()  # Add an extra line for looks

    # Add code to get product data from user
    @staticmethod
    def input_new_product_and_price():
        """  Gets product and price values to be added to the list

        :return: (string, string) with product and price
        """
        try:
            product = str(input("Please enter a product: "))
            price = str(input("Please enter its price: "))  # we're looking for float values for price
            product_and_price = Product(product_name=product, product_price=price)
            return product_and_price

        except Exception as e:
            raise (e)

    # Add code to remove product data
    @staticmethod
    def input_product_to_remove():
        """  Gets the product name to be removed from the list

        :return: (string) with product
        """

        task = str(input("Which product do you want to remove?: "))
        return task


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)  # read file data


# Show user a menu of options
while (True):
    try:
        # Step 3 Show current data
        IO.output_menu_tasks()  # Shows menu

    # Get user's menu option choice
        choice_str = IO.input_menu_choice()  # Get menu option

    # Show user current data in the list of product objects
        if choice_str.strip() == '1':   # Show current products
            IO.output_current_tasks_in_list(lstOfProductObjects)
            continue

    # Let user add data to the list of product objects
        elif choice_str.strip() == '2':  # Add a new product
            lstOfProductObjects.append(IO.input_new_product_and_price())
            continue  # to show the menu

    # Let user remove data from the list of product objects
        elif choice_str.strip() == '3': # Remove a product
            product = IO.input_product_to_remove()
            lstOfProductObjects = FileProcessor.remove_data_from_list(product_to_remove=product, list_of_rows=lstOfProductObjects)

    # let user save current data to file
        elif choice_str == '4':  # Save Data to File
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            continue  # to show the menu

    # Let user exit
        elif choice_str == '5':  # Exit Program
            print("Goodbye!")
            break  # exiting loop

    except Exception as e: # catching an exception; looping back to start
        print('Non-specific error.')
        print('Built-In Python error info: ')
        print(e, e.__doc__, type(e), sep='\n')
        print('Looping back to start')

# Main Body of Script  ---------------------------------------------------- #
