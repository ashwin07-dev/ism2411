# Module 7: Functions
#
# Self-Assessment 1:
# TODO: After debugging the original broken_sales.py, describe the first bug
# you spotted, how you found it, and what you learned about debugging.
#
# Self-Assessment 2:
# apply_discount takes an original price and a membership tier.
# It checks whether the tier is gold, silver, bronze, or another tier,
# and returns the price after the corresponding discount.
#
# AI disclosure (Self-Assessment 3):
# I used ChatGPT to help draft and explain Exercises 1-4 and 6.
# I reviewed the code and need to complete Exercise 5 myself.
# AI helped explain function composition and variable scope.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier + ':':<8}${apply_discount(200, tier):.2f}")


# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
with_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${with_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
# TODO: Download broken_sales.py and paste its corrected code here.
# The original three bugs and your own debugging explanation are required.
# Do not submit this starter file until Exercise 5 is completed.


# --- Exercise 6 ---
x = 100  # global variable


def double_it():
    x = 999  # local variable; only exists inside this function
    return x * 2


print(x)
print(double_it())
print(x)
# Scope explanation: The x inside double_it is local to that function.
# It is separate from the global x, so the global value remains 100.
