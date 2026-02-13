correct_pin = "12345"

for i in range(5):
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")

else:
    print("Account Locked")
