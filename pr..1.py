print ("Welcome to Interactive Personal Data Collector")
name = input ("Enter your Name :")
age = int (input ("Enter your Age t "))
weight = float (input ("Enter Your Weight : "))
height = float (input ("Enter Your Heicht in Meters : "))
fav_number = int(input ("Enter your favourite number: "))
                       
print ("Thank you! Here is the information we collected:  ")
                       
current_year = 2026
birth_year = current_year - age
height_cm = height * 100

print(f"Name: (name]")
print(f"Age: (age)")
print(f"Height: (height) meters")
print(f"Heiaht in cm: (height_cm)")
print(f"Favourite Number: (fav _number)")
print(f"Your approximate Birth Year is: (birth_year) (Based on your (agel)")
print("name -> Value: (name), Type: (type(name)), Memory Address: (id(name)]")
print(f"age -> Value: (age), Type: [type(age)), Memory Address: lid(age))")
print(f"height -> Value: (height), Type: [type(height)], Memory Address:")
print(f"fav_number -> Value: (fav_number), Type: [type (fav_number)), Memory Address:")
print(f"birth_year -> Value: (birth_year), Type: (type (birth_year)), Memory Address:")
print(f"height_cm -> Value: (height)_cm), Type: [type (height_cm)), Memory Address:")
print()
print("Thank you for using the Personal Data Collector. Goodbye!")
