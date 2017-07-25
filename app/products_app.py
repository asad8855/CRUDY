import csv

# can assume these headers
headers = ["id", "name", "aisle", "department", "price"]

def read_products_from_file(csv_file_path):
    products = []
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for ordered_dict in reader:
            products.append(dict(ordered_dict))
    return products

def write_products_to_file(products, csv_file_path):
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

#
# CRUD OPERATION HELPERS
#

def user_inputtable_headers():
    return [header for header in headers if header != "id"]

def map_id(product): return int(product["id"])

def auto_increment_id(products):
    product_ids = list(map(map_id, products))
    if len(product_ids) == 0: next_id = 1
    else: next_id = max(product_ids) + 1
    return next_id

def user_inputs_product_id():
    product_id = input("OK. Please specify the product's identifier: ")
    return product_id

def prompt_user_for_product_info():
    print("OK. Please specify the product's information...")

def handle_index_error():
    print("OOPS. There are no products matching the given identifier. Try listing products to see which ones exist.")

# param product_id should be an integer
# param products should be a list of dictionary-like items
def lookup_product(product_id, products):
    matching_products = [p for p in products if int(p["id"]) == int(product_id)]
    return matching_products[0]

#
# CRUD OPERATIONS
#

def list_products(products):
    print("THERE ARE", len(products), "PRODUCTS:")
    for product in products:
        print("  +", product) #print(" + Product #" + str(product["id"]) + ": " + product["name"])
    return products

def create_product(products):
    prompt_user_for_product_info()
    product = {"id": auto_increment_id(products) }
    for header in user_inputtable_headers():
        product[header] = input("    {0}: ".format(header))
    products.append(product)
    print("CREATING A PRODUCT HERE!")
    print(product)
    return product

def update_product(products):
    product_id = user_inputs_product_id()
    try:
        product = lookup_product(product_id, products)
        prompt_user_for_product_info()
        for header in user_inputtable_headers():
            product[header] = input("    Change {0} from '{1}' to: ".format(header, product[header]))
        print("UPDATING A PRODUCT HERE!")
        print(product)
        return product
    except IndexError as e:
        handle_index_error()

def show_product(products):
    product_id = user_inputs_product_id()
    try:
        product = lookup_product(product_id, products)
        print("SHOWING A PRODUCT HERE!")
        print(product)
        return product
    except IndexError as e:
        handle_index_error()

def destroy_product(products):
    product_id = user_inputs_product_id()
    try:
        product = lookup_product(product_id, products)
        del products[products.index(product)]
        print("DESTROYING A PRODUCT HERE!")
        print(product)
        return product
    except IndexError as e:
        handle_index_error()

#
# USER INTERFACE
#

def compile_menu(products = [], username="Unidentified User"):
    menu = """
-----------------------------------
PRODUCTS APPLICATION
-----------------------------------
Welcome {0}!

There are {1} products in the database. Please select an operation:

    operation | description
    --------- | ------------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.

""".format(username, len(products))
    return menu

def process_unrecognized_operation():
    print("UNRECOGNIZED OPERATION. PLEASE TRY AGAIN.")

def enlarge(i):
    return i * 100

def run():
    file_path = "data/products.csv"
    products = read_products_from_file(csv_file_path=file_path)

    menu = compile_menu(products=products, username="@s2t2")
    crud_operation = input(menu).title()
    if crud_operation == "List": list_products(products)
    elif crud_operation == "Show": show_product(products)
    elif crud_operation == "Create": create_product(products)
    elif crud_operation == "Update": update_product(products)
    elif crud_operation == "Destroy": destroy_product(products)
    else: process_unrecognized_operation()

    write_products_to_file(products, csv_file_path=file_path)

# don't run this app unless this script is executed from the command line.
# this strategy allows us to test the app's component functions without asking for user input
if __name__ == "__main__": # "if this script is run from the command-line"
    run()
