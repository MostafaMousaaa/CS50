from cs50 import get_float

def calculate_coins(cents):
    """Calculate minimum number of coins for given cents"""
    coins = [25, 10, 5, 1]  # quarters, dimes, nickels, pennies
    coin_names = ["quarters", "dimes", "nickels", "pennies"]
    total_coins = 0
    breakdown = {}
    
    for i, coin_value in enumerate(coins):
        count = cents // coin_value
        cents = cents % coin_value
        total_coins += count
        breakdown[coin_names[i]] = count
    
    return total_coins, breakdown

def main():
    """Calculate minimum coins for change"""
    
    # Get valid input
    while True:
        dollars = get_float("Change owed: ")
        if dollars >= 0:
            break
        print("Please enter a non-negative amount")
    
    # Convert to cents (avoid floating point issues)
    cents = round(dollars * 100)
    
    # Calculate coins
    total_coins, breakdown = calculate_coins(cents)
    
    # Display results
    print(f"\nChange breakdown for ${dollars:.2f}:")
    for coin_type, count in breakdown.items():
        if count > 0:
            print(f"{coin_type.capitalize()}: {count}")
    
    print(f"\nTotal coins: {total_coins}")
    
    # Alternative one-liner approach
    coins_alt = 0
    for coin in [25, 10, 5, 1]:
        coins_alt += cents // coin
        cents %= coin
    
    print(f"Alternative calculation: {coins_alt} coins")

if __name__ == "__main__":
    main()
