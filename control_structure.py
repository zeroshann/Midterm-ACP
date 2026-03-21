age = int(input("Enter age: "))
has_card = input("Do you have a discount card? (yes/no): ")
if age <= 12:
 if has_card == "yes":
    print("Child ticket with discount: ₱80")
 else:
    print("Child ticket: ₱100")
elif 13 <= age <= 59:
 if has_card == "yes":
    print("Regular ticket with discount: ₱180")
 else:
    print("Regular ticket: ₱220")
elif age >= 60:
 if has_card == "yes":
    print("Senior ticket with discount: ₱60")
 else:
    print("Senior ticket: ₱80")