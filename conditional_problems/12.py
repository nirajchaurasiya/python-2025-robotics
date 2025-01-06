# Calculate electricity bills based on units consumed using different rates for different ranges.

# For the first 50 units: $0.50 per unit
# For the next 100 units: $0.75 per unit
# For the next 100 units: $1.20 per unit
# Beyond 250 units: $1.50 per unit


def calculate_bill(units):
    bill = 0
    if units <= 50:
        bill = units * 0.50
    elif units <= 150:
        bill = (50 * 0.50) + ((units - 50) * 0.75)
    elif units <= 250:
        bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
    else:
        bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)
    return bill


units_consumed = 270
print(f"Total Electricity Bill: ${calculate_bill(units_consumed):.2f}")
