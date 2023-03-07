customer: str = "Cece"
pizza_base: str = "Thin"
pizza_size: int = 12
topping: str = "Olives"
extra_cheese: bool = True
price: float = 8.99


# print(f"Received order from {customer}")
# print(f"Pizza Base: {pizza_base}, Size {pizza_size} inches, Topping: {topping}")
# print(f"Is extra cheese required: {extra_cheese}")
# print(f"Bill Amount: {price}")


order_details: str = f"""
Received order from: {customer}
Pizza Base: {pizza_base}, Size {pizza_size} inches, Topping: {topping}
Is extra cheese required: {extra_cheese}
Bill Amount: {price}
"""

print(order_details)