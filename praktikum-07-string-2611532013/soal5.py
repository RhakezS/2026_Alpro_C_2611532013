# Name: Rhakez Elvano Stonie
# NIM: 2611532013
# Question: 5

#Bagian A
username = input("Username: ")
if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

#Bagian B
nim = input("NIM: ")
if len(nim) != 10:
    print("Invalid NIM")
elif not nim.isdigit():
    print("Invalid NIM")
else:
    intake = nim[0:2]
    print("year:", "20" + intake)