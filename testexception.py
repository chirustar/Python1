class FlightNotFoundError(Exception):
    pass

class Flight:
    def __init__(self,flight_no,source,destination,total_seats):
        self.flight_no=flight_no
        self.source=source
        self.destination=destination
        self.total_seats=str(total_seats)
        
    def add_flight(self,flight_no,source,destination,total_seats):
        self.flight_no=flight_no
        self.source=source
        self.destination=destination
        self.total_seats=str(total_seats)
        try:
            seats=int(self.total_seats)
            if seats<=0:
                raise ValueError("seats cannot be more then 0")
            print("Flight added successfully")
            
            
        except ValueError as ve:
            print(f"Value error ", {ve})
             
        except Exception as e:
            print(f"Exception error", {e})  
            
f1=Flight("P101", "Banglore", "Hassan", "50")
f1.add_flight("P103","Rajasthan","delhi", "-12")            
            
             
                        

        
    
    