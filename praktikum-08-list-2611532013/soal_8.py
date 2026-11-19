number_of_rows = 4
seats_per_row = 5
# Write your code below

seats = []
for r in range(number_of_rows):
    row = []
    for s in range(seats_per_row):
        row.append(".")
    seats.append(row)

while True:
    for r in range(number_of_rows):
        print("Row " + str(r + 1) + ": ", end="")
        for s in range(seats_per_row):
            print(seats[r][s] + " ", end="")
        print()

    row_number = int(input("Row (0 to stop): "))
    if row_number == 0:
        break
    seat_number = int(input("Seat: "))

    if row_number < 1 or row_number > number_of_rows or seat_number < 1 or seat_number > seats_per_row:
        print("Invalid seat.")
    elif seats[row_number - 1][seat_number - 1] == "X":
        print("Seat already taken.")
    else:
        seats[row_number - 1][seat_number - 1] = "X"
        print("Seat booked.")

taken = 0
for r in range(number_of_rows):
    for s in range(seats_per_row):
        if seats[r][s] == "X":
            taken += 1
print("Seats taken: " + str(taken))