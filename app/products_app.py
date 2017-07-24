import csv
username=" Arash"

products = []
csv_file_path = "data/products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)



menu="""
    ------------------------------------
            PRODUCTS APPLICATION
    ------------------------------------
    Hello{1},
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

with open(csv_file_path, "w", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)

def list_products():
    print("LISTING PRODUCTS")

def show_product():
    print("SHOWING A PRODUCT")

def create_product():
    print("CREATING A PRODUCT")

def update_product():
    print("UPDATING A PRODUCT")

def destroy_product():
    print("DESTROYING A PRODUCT")

if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
