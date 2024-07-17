details = {
    "Name" : "John",
    "Age" : 25,
    "Place" : "Hyderabad",
    "Course" : "Engneering"
}
#adding more info to details  variable:

details["Graduation"] = 2020
details["Grade"] = "A+"

keys = list(details.keys())
i = 0
#using while loop

while i < len(keys):
    item = keys[i]
    print(f"{item}:{details[item]}")
    i += 1
