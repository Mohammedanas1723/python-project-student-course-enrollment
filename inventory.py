products={}
def  Add_Product():
        
        product_id=input("enter prodcut id:")
        if product_id in products:
            print ("product alredy exists")
            return
        product_name  =input("enter product name:")
        product_price = (input("Enter prodp'uct price:"))

        if product_price <= 0:
             print("Price must be greater than 0")
             return
           
        product_quantity=int(input("enter product quantity:"))
        if product_quantity<0:
            print(" Quantity cannot be negative")
            return
        products[product_id]={
            "name":product_name,
            "price":product_price,
            "quantity":product_quantity
        }
        print("product added successfully") 
        print(products)
    #  UPDATE PRODUCTS------------->>>>>>>
def  Update_Product():
        product_id=int(input("Enter product_id"))
        if product_id not in products:
            print("product not found")
            return
        products[product_id]["name"]=input("enter new product name:")    
        products[product_id]["price"]=float(input("enter new prodcut price:"))
        products[product_id]["quantity"]=float(input("enter new product quantity"))

        
        print(products)

        # DELETE PRODUCT........>>>>>>>

def  Delete_product() :
        product_id=input("enter product id:")
        if product_id in products:
            del products[product_id]
            print("product deleted successfully")
        else:
            print("product not found")
    
     


    # SEARCH PRODUCT BY PRODUCT ID .........>>>>>>
def search_product():
        product_id=input("enter product id:")
        if product_id not in products:
            print("product not found")
            return
        product=products[product_id]
        print(f"prodcut founded !")
        print(f"product id:{product_id}")
        print(f"product name:{product['name']}")
        print(f"product price:{product['price']}")
        print(f"product quantity:{product['quantity']}")
       
        print(products)
def View_products():
        if not products:
            print("No products found.")
            return
        print("Product List:")
        for product_id, product in products.items():
            print("Product ID:", product_id)
            print("product name:",product["name"])
            print("product price:",product["price"])
            print("product quantity:",product["quantity"])
            print("--------------------") 
def Sell_Product():
       product_id=input("enter prodcut id:")
       if product_id in products:
            quantity=int(input("enter product quantity:"))
            if quantity <= products[product_id]["quantity"]:
                products[product_id]["quantity"] -= quantity
                total=products[product_id]["price"]*quantity
                print("product sold sucessfully")
                print("total amount",total)
                print("Balance stock",products[product_id]["quantity"])
            else:
                print("Insufficient quantity.")
       else:
            print("Product not found.")

def Restock_Product():
    product_id=input("enter prodcut id:")
    if product_id in products:
        quantity=int(input("enter number of quantity"))
        products[product_id]["quantity"]+=quantity
        print("restock sucessfully")
    elif quantity<0:
         print("ivalid quantity")
    else:
         print("quantity cant be negative")     


def Lowstock_product():
    Lowstock_product = []

    for product_id, product in products.items():
        if product["quantity"] < 5:
            Lowstock_product.append(product_id)

    if Lowstock_product:
        print("Low stock products:", Lowstock_product)
    
         


products={}
while True:
    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. View Product")
    print("6. Sell Product")
    print("7. Restock Product")
    print("8. Low Stock Products")
    print("9. Sort Products")
    print("10. Inventory Value")
    print("11. Exit")

    choice = input("Enter your choice: ")
   
    if choice == '1':
        Add_Product()
    
    elif choice =='2'    :
         Update_Product()
    elif choice=='3':
        Delete_product()
    elif choice=='4':
       search_product()
    elif choice =='5':
        View_products()
    elif choice=='6':
        Sell_Product()
    elif choice =='7':
        Restock_Product()
    elif choice =='8':
        Lowstock_product()
    elif choice =='9':
        print("sort prodcut")
    elif choice =='10':
        print ("inventory value")
    elif choice =='11':
        print("exit")
        break
        
    