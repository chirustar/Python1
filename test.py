class Flight:
    def __init__(self, flight_no, base_price, total_seats):
        self.flight_no = flight_no
        self.base_price = base_price
        self.total_seats = total_seats
        print("We are into the Flight Constructor")
        
    def display_flight_info(self):
        print(f"Flight {self.flight_no} has a base price of INR {self.base_price} with total seats {self.total_seats}")


class DomesticFlight(Flight):
    def __init__(self, flight_no, base_price, total_seats, tax_percent):
        super().__init__(flight_no, base_price, total_seats)
        self.tax_percent = tax_percent
        print("We are into the DomesticFlight Constructor")
        
    def calculate_price(self):
        total_price = self.base_price + self.tax_percent
        return total_price


class BookingFlight(DomesticFlight):
    def __init__(self, flight_no, base_price, total_seats, tax_percent, booked_seats):
        super().__init__(flight_no, base_price, total_seats, tax_percent)
        self.booked_seats = booked_seats
        print("We are into the BookingFlight Constructor")
        
    def seat_availability(self):
        if self.booked_seats <= self.total_seats:
            print("seats are available")
        else:
            print("you need seat no {self.booked_seats} but seats available are {self.total_seats}")
            
    def book_seats(self):      
        left_seats= self.total_seats-self.booked_seats
        print("total remining seats after booked ", left_seats)
        
    def get_final_price(self):
        final_price  = self.base_price * self.booked_seats  
        print("final price is ", final_price)


BF = BookingFlight("AB121", 5000, 30, 2, 28)
BF. seat_availability()
BF.book_seats
BF.get_final_price()