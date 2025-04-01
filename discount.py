# Define the function to calculate the discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and print the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price after applying the discount (or the original price)
print(f"The final price is: ${final_price:.2f}")