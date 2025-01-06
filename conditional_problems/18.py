# Check if a user is eligible for a discount based on purchase amount.

# For discount rules:
#   Purchase of more than $10,000: get a discount of 10%
#   Purchase of more than $100,000: get a discount of 15%
#   Purchase of more than $1,000,000: get a discount of 20%
#   For lower than $10,000: doesn't get a discount


# Discount rules based on purchase amount
purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount > 1_000_000:
    discount = 20  # 20% discount
elif purchase_amount > 100_000:
    discount = 15  # 15% discount
elif purchase_amount > 10_000:
    discount = 10  # 10% discount
else:
    discount = 0  # No discount

if discount > 0:
    discount_amount = purchase_amount * (discount / 100)
    final_amount = purchase_amount - discount_amount
    print(f"You get a {discount}% discount.")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Final Amount to Pay: ${final_amount:.2f}")
else:
    print("No discount applied.")
    print(f"Total Amount to Pay: ${purchase_amount:.2f}")
