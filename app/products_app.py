import csv
import getpass
username = getpass.getuser()
# p = getpass.getpass()
# print ("You entered:",p)

#Read Products
products = []
headers = ["id", "name", "aisle", "department", "price"]
user_input_headers = [header for header in headers if header != "id"]
def get_product_id(product): return int(product["id"])


def creat_new_pid():
    last_pid = map(get_product_id, products)
    return max(last_pid) + 1

csv_file_path = "data/products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)



menu="""
    ------------------------------------
            PRODUCTS APPLICATION
    ------------------------------------
    Hello {1},
    There are {0} products (Exit and reopen app to refresh product count)
    Please choose an operation:
    'List'    | Display a list of product identifiers
    'Show'    | Show information about a product
    'Create'  | Add a new product
    'Update'  | Edit an existing product
    'Destroy' | Delete an existing product
""".format(len(products),username)
chosen_operation = input(menu)
chosen_operation = chosen_operation.title()



def list_products():
    print("LISTING PRODUCTS")
    for product in products:
        print(product["id"], product['name'])

def show_product():
    while True:
        show_request = input("WOULD YOU LIKE CRUDY TO LOOK UP AN ITEM? (Y/N): ")
        if show_request == "N": break
        elif show_request == "Y":
            while True:
                lookup = input("ENTER ID: ")
                if int(lookup) > len(products):
                    print("Please select a product ID with the range 0 -", len(products))
                    break
                elif int(lookup)< len(products):
                    product = [p for p in products if p["id"] == lookup][0]
                    if product:
                        print("READING PRODUCT HERE:",
                        "\n", "        ID #: ",product["id"],
                        "\n", "NAME @ PRICE: ",product["name"].title(), "@" ,'${0:.2f}'.format(float(product["price"])),
                        "\n", "       AISLE: ", product["aisle"].title(),
                        "\n", "  DEPARTMENT: ",product["department"].title())
                    else:
                        print("CRUDY COULDNT FIND THE PRODUCT", product)
                else:print("Please enter 'Y' for 'yes' or 'N' or 'no'")

def create_product():
    print("PLEASE PROVIDE CRUDY WITH NEW PRODUCT INFORMATION")
    new_product = {"id": creat_new_pid() }
    for header in user_input_headers:
        new_product[header] = input("The '{0}' is: ".format(header).title())
    print("Please review and CONFIRM the information for the new product you added:",
        "\n", "        ID #: ",new_product["id"],
        "\n", "NAME @ PRICE: ",new_product["name"].title(), "@" ,'${0:.2f}'.format(float(new_product["price"])),
        "\n", "       AISLE: ",new_product["aisle"].title(),
        "\n", "  DEPARTMENT: ",new_product["department"].title())
    confirmation = input("Would you like to save your changes? (Y/N): ")
    if confirmation == "Y":
        products.append(new_product)
        print("Your changes have been saved!")
    elif confirmation == "N": print("Sorry about that, let's try again.")
    else: print("Please enter 'Y' for 'yes' or 'N' or 'no'")
    print("There are now",len(products), "unique products in your inventory.")
    print("CREATING A PRODUCT")

def update_product():
    while True:
        show_request = input("Would you like CRUDY to update a product? (Y/N): ")
        if show_request == "N": break
        elif show_request == "Y":
            lookup = input("PLEASE ENTER THE PRODUCT ID OF THE PRODUCT YOU ARE UPDATING: ")
            product = [p for p in products if p["id"] == lookup][0]
            if product:
                print("\n","PLEASE ENTER THE PRODUCTS UPDATED INFORMATION", "\n")
                for header in user_input_headers:
                    product[header] = input("Change '{0}' from '{1}' to: ".format(header.title(), product[header]))
                print("\n","REVIEW UPDATED PRODUCT INFO:",
                "\n", "        ID #: ",product["id"],
                "\n", "NAME @ PRICE: ",product["name"].title(), "@" ,'${0:.2f}'.format(float(product["price"])),
                "\n", "       AISLE: ",product["aisle"].title(),
                "\n", "  DEPARTMENT: ",product["department"].title(),
                "\n", "\n", "If this is incorrect, please start over from the main menu.", "\n")
            else:
                print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product)
        else: print("Please enter 'Y' for 'Yes' or 'N' or 'No'")

def destroy_product():
    while True:
        show_request = input("Would you like CRUDY to delete a product? (Y/N): ")
        if show_request == "N": break
        elif show_request == "Y":
            lookup = input("ENTER ID: ")
            product = [p for p in products if p["id"] == lookup][0]
            if product:
                while True:
                    print("Please confirm you'd like to PERMANENTLY DELETE:", "\n","\n",
                        "ID #:",product["id"],"\n",
                        "NAME:",product["name"].title(),"\n",)
                    confirmation = input("'Y' to CONFIRM, 'N' to ABORT: ")
                    if confirmation == "N": break
                    elif confirmation == "Y":
                        del products[products.index(product)]
                        print("\n","THE FOLLOWING PRODUCT HAS BEEN PERMANENTLY REMOVED:",
                        "\n", "        ID #: ",product["id"],
                        "\n", "NAME @ PRICE: ",product["name"].title(), "@" ,'${0:.2f}'.format(float(product["price"])),
                        "\n", "       AISLE: ",product["aisle"].title(),
                        "\n", "  DEPARTMENT: ",product["department"].title(), "\n")
                        break
                    else: "Please enter a valid confirmation ('Y' to CONFIRM, 'N' to ABORT): "
            else:
                print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", lookup)
        else: print("Please enter 'Y' for 'yes' or 'N' or 'no':")

if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("CRUDY DID NOT UNDERSTAND, PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS")


#
#WRITE PRODUCTS To FILE
#

with open(csv_file_path, "w", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)
        
def enlarge (i):
    return i * 100
