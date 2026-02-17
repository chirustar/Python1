class product:
    name="chiranth"
    price =2000
    brand="nike"
    warranty=1
    
    def display(self):
        print(f"This is a product")
        
    def cal_price(self):
        price=self.price * self.count
        print(f"this is price", price)
        
class electronics(product):
    type="mobile"
    count=10
    
    def displayalldetails(self):
        print(f"This is a product of type {self.type} with count {self.count}")
        
mobile=electronics()
mobile.display()
mobile.displayalldetails()                    