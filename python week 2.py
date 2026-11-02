
# Python Project 2 - Expense Tracker
# DecodeLabs Industrial Training Kit

# Step 1: Initialize the total
total = 0

# Step 2: Continuous input loop
while True:

    print("\n===== EXPENSE TRACKER =====")

    user_input = input("Enter expense amount (or type 'quit' to stop): ")

    # Step 3: Check exit condition
    if user_input.lower() == "quit":
        break

    # Step 4: Validate and convert input
    try:
        expense = int(user_input)

        # Step 5: Accumulate the expense
        total = total + expense

        print("Expense added successfully!")
        print("Current Total:", total)

    except ValueError:
        print("Invalid Data! Please enter a number.")

# Step 6: Display final output
print("\n===== EXPENSE SUMMARY =====")
print("Final Total Spent: $", format(total, ".2f"))
print("Thank you for using Expense Tracker!")
