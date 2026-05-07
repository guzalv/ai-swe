def calculate_discount(price, discount_percent):
    """Apply discount to a price."""
    if discount_percent > 100:
        discount_percent = 100
    result = price - (price * discount_percent / 100)
    return result

def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
