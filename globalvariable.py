discount = 10
productid = 101
prodName="Laptop"
price=50000

def displayProductDetails():
    global discount
    
    print("Product id:", productid)
    print("Product Name:", prodName)
    print("Product Price:", price)
    
    discountedPrice=price-(price*discount/100)
    print("Price after discount:", discountedPrice)
    
def calculateTotalPrice(quantity):
    global discount
    
    totalPrice=quantity*price
    finalPrice=totalPrice-(totalPrice*discount/100)
    
    return finalPrice

displayProductDetails()

qty=3
result=calculateTotalPrice(qty)
print("Total price after discount for", qty,"quantity",result)
    