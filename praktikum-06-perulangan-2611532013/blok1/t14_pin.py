correct_pin_2013 = "1234"
MAX_ATTEMPTS_2013 = 3
attempt_2013 = 1
pin_2013 = input("Enter PIN: ")

while pin_2013 != correct_pin_2013 and attempt_2013 < MAX_ATTEMPTS_2013:
    print("Incorrect PIN.")
    attempt_2013 += 1
    pin_2013 = input("Enter PIN: ")

if pin_2013 == correct_pin_2013:
    print("Access granted")
else:
    print("Account locked")