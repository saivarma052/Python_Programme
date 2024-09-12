import re

num_passengers = int(input("Enter the numbers of passengers: "))

passengers = []

#i =1;

for i in range(num_passengers):
    print("\nEnter details for the passenger: ", i+1)

    username = input("Enter your username: ")
    first_name = input("Enter your first name: ")
    second_name = input("Enter your second name: ")
    age = int(input("Enter your age: "))
    gender = str(input("Enter your gender Male/Female: "))

    if age > 18:
        user_type = "Adult"
    elif age < 5:
        user_type = "Child"
    else:
        user_type = "Minor"
    # Validate the mobile number

    mobile = input('Enter a Mobile number :')
    # Taking user input
    a = re.fullmatch('[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', mobile)
    # calling fullmatch function by passing pattern and n
    if a != None:  # checked the number is valid  or not
        print('This is a valid mobile number')
    else:
        print('This is not a valid mobile number')

    distance = float(input("Enter the distance from source to destination (in KM): "))

    if distance > 750:
        fare = distance * 3
    elif distance > 500:
        fare = distance * 2
    else:
        fare = 500

    passenger_details = {
        'username': username,
        'first_name': first_name,
        'second_name': second_name,
        'age': age,
        'gender': gender,
        'user_type': user_type,
        'mobile': mobile,
        'distance': distance,
        'fare': fare
    }
    passengers.append(passenger_details)

#n = len(passengers)

#i = 0
for passenger in passengers:
    print("Passenger details")
    for key, value in passenger.items():
        print(f"{key}:{value}")


''' print(f"\n Details for passenger {i}:")
    print(f"Username: {passenger['username']}")
    print(f"first_name: {passenger['first_name']}")
    print(f"second_name: {passenger['second_name']}")
    print(f"age: {passenger['age']}")
    print(f"gender: {passenger['gender']}")
    print(f"user_type: {passenger['user_type']}")
    print(f"mobile: {passenger['mobile']}")
    print(f"Distance: {passenger['distance']}")
    print(f"Fare: {passenger['fare']}")'''


#print(passengers)



#fare = max(fare, 500)
