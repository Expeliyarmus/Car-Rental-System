print("Vehicle Rental System")
print("Type of Vehicles Available Here: Car,Bike")
tell=input("Enter the vehicle type that you want to rent: ")
a=input("enter the name of the vehicle: ",)
b=int(input('enter the rent of the vehicle: '))
c=input("enter Available Or Rented: ")
if tell == 'Bike' or tell == 'bike':
    d=input("enter engine per cc: ")
if tell == 'car' or tell == 'Car':
    e=int(input("enter no. of seats: "))
class vehicle:
        def __init__(self,a,b,c):
            self.vehicle_name=a
            self.rent_perday=b
            self.availability=c
class car(vehicle):
    def __init__(self,a,b,c,e):
        super().__init__(a,b,c)
        self.seats=e
class bike(vehicle):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.engine=d
if tell == 'Bike' or tell == 'bike':
    print("name rent availability engine")
    print(a,b,c,d)
if tell == 'car' or tell == 'Car':
    print("name rent availability seats")
    print(a ,b ,c ,e)
t=int(input("enter the no. of days to be taken for rent: "))
print("total cost of rent:",t*b)



    
