# Integer
age: int = 25
number_of_seats: int = 1
bus_number: int = 5090

# Float
ticket_price: float = 1005.75  # rupee
distance: float = 559.7  # Kms

# String
name: str = "Sai Varma"
bus_route: str = "MMD to HYD"
bus_operator: str = "ORANGE TOURS and TRAVELS"

# Boolean
booking_confirmed: bool = True
booking_is_not_confirmed: bool = True

# Date and Time
date_of_travel: str = "2024-07-03"
Departure_time: str = "2024-07-02 22:00:00"
# List


print(f"Name: {name}")
print(f"Age: {age}")
print(f"Date_of_Travel: {date_of_travel}")
print(f"Seats: {number_of_seats}")
print(f"Bus_number: {bus_number}")
print(f"Bus_route: {bus_route}")
print(f"Bus_Operator: {bus_operator}")
print(f"Price_of_the_Tickets: {ticket_price}")
print(f"Time: {Departure_time}")
print(f"Distance: {distance}")
print(f"Confirmation: {booking_confirmed}")

#print declation
if booking_confirmed:
    print("your ticket is confirmed")

else:
    print("your ticket is not confirmed")