#Create empty dictionary for items
item_dict={}
shop_dict={}

#Welcome user
username=input("Please enter your name:")
welcomemessage=f"Welcome to the Store {username}"
lenWCMsg=len(welcomemessage)
print("*"*lenWCMsg)
print(welcomemessage)
print("*"*lenWCMsg)

#Read data from the text file
my_file=open("/Users/aviyasingh/Documents/Python/grocery_list.txt")

file_line=my_file.readline()
#print(file_line)
item_list=my_file.readlines()
#print(item_list)

my_file.close()

#Fetch items from the list and add to a dictionary
print("*****************Items available in our Store*****************")
for item in item_list:
    item_name=item.split()[0]
    item_price=item.split()[1]
    print(f"{item_name}: {item_price}")
    item_dict.update({item_name: float(item_price)})
print("*"*62)
#print(item_dict)

#Prompt user to add items
proceedshop=input("Do you wish to proceed shopping in the store(yes/no):")
while proceedshop.lower() == "yes":
    item_add=input("Add an item:")
    if item_add.title() in item_dict:
        print(f"{item_add.title()}")
        item_qty=int(input("Add quantity to be added:"))
        shop_dict.update({item_add:{"quantity":item_qty,"subtotal":item_dict[item_add.title()]*item_qty}})
        print(shop_dict)
        
    else:
        print("Unable to add, item does not exist!!")
    proceedshop=input("Do you wish to add more items in the cart(yes/no):")
else:
    print("\n")
    print("********Bill Summary*********")
    print("\n")
    print("Item       Quantity     Subtotal")
    total=0
    for key in shop_dict:
        print(f"{key}        {shop_dict[key]['quantity']}              {shop_dict[key]['subtotal']}")
        total=shop_dict[key]['subtotal']+total
        print(f"Total: {total}")
    print("**********Thank You**********")
    print("Hope to see you back soon!!")
