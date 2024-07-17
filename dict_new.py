details = {
    "Name" : "John",
    "Age" : 25,
    "Place" : "Hyderabad",
    "Course" : "Engneering"
}

#print(details)

#access dict values
print("Student's Name is:", details["Name"])
print(f"Student's age is:", details["Age"])
print("Student place is: ", details["Place"])
print("student course is: ", details["Course"])

details["Graduation_year"] = 2025
print("Student Graduation year:", details["Graduation_year"])
details["grade"] = "A+"
print("Student grade:", details["grade"])

for key, value in details.items():
    print(f"{key}:{value}")