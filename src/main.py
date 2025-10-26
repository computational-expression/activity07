"""
Activity 7: Halloween Parade Candy Calculator
Student Name: [Your Name Here]
Date: [Today's Date]

Halloween Parade Calculator inspired by Meadville's 58th Annual Halloween Parade
Theme: "Under the Sea"
"""

def calculate_candy_needed(spectators, pieces_per_person):
    """Calculate total candy pieces needed for parade spectators
    
    Args:
        spectators (int): Number of expected spectators
        pieces_per_person (int): Candy pieces to give each person
    
    Returns:
        int: Total candy pieces needed
    """
    # TODO: Implement this function

def pieces_to_bags(total_pieces, pieces_per_bag):
    """Convert candy pieces to number of bags needed
    
    Args:
        total_pieces (int): Total candy pieces needed
        pieces_per_bag (int): Number of pieces in each bag (typically 50)
    
    Returns:
        float: Number of candy bags to purchase
    """
    # TODO: Implement this function

def calculate_total_cost(decoration_cost, costume_cost, candy_cost, tax_rate):
    """Calculate total cost of parade participation with tax
    
    Args:
        decoration_cost (float): Cost of float decorations
        costume_cost (float): Cost of costumes
        candy_cost (float): Cost of candy
        tax_rate (float): Tax rate (e.g., 0.06 for 6%)
    
    Returns:
        float: Total cost including tax
    """
    # TODO: Implement this function

def estimate_total_spectators(route_blocks, spectators_per_block):
    """Estimate total spectators along entire parade route
    
    Args:
        route_blocks (int): Length of parade route in blocks
        spectators_per_block (int): Average spectators per block
    
    Returns:
        int: Estimated total spectators
    """
    # TODO: Implement this function

def compare_candy_deals(option1_cost, option1_pieces, option2_cost, option2_pieces):
    """Compare candy purchasing options and find the best deal
    
    Args:
        option1_cost (float): Cost of first candy option
        option1_pieces (int): Number of pieces in first option
        option2_cost (float): Cost of second candy option
        option2_pieces (int): Number of pieces in second option
    
    Returns:
        str: Recommendation for best candy deal with cost per piece
    """
    # TODO: Implement this function

def create_parade_summary(float_theme, total_spectators, total_candy, total_cost):
    """Create formatted summary of parade participation
    
    Args:
        float_theme (str): Theme of the parade float
        total_spectators (int): Estimated number of spectators
        total_candy (int): Total candy pieces needed
        total_cost (float): Total cost of participation
    
    Returns:
        str: Formatted parade summary with "Under the Sea" theme
    """
    # TODO: Implement this function

def main():
    """Main program to run the Halloween Parade Candy Calculator"""
    print("🎃 === Halloween Parade Candy Calculator === 🎃")
    print("Welcome to the Meadville Parade Planner!")
    print("This year's parade theme: \"Under the Sea\"")
    print()
    
    # Get user input for their float theme and details
    print("🌊 Enter your float details:")
    float_theme = input("Float theme: ")
    route_blocks = int(input("Parade route length (blocks): "))
    pieces_per_person = int(input("Candy pieces per spectator: "))
    decoration_cost = float(input("Decoration budget: $"))
    costume_cost = float(input("Costume budget: $"))
    candy_cost = float(input("Candy budget: $"))
    print()
    
    # Use your functions to calculate parade needs
    # Estimate crowd size (assuming average of 25 spectators per block)
    spectators_per_block = 25
    total_spectators = estimate_total_spectators(route_blocks, spectators_per_block)
    
    # Calculate candy needs
    total_candy = calculate_candy_needed(total_spectators, pieces_per_person)
    pieces_per_bag = 50  # Standard candy bag size
    bags_needed = pieces_to_bags(total_candy, pieces_per_bag)
    
    # Calculate total costs (6% tax rate)
    tax_rate = 0.06
    total_cost = calculate_total_cost(decoration_cost, costume_cost, candy_cost, tax_rate)
    
    # Compare candy deals
    option1_cost = 15.00
    option1_pieces = 150
    option2_cost = 20.00
    option2_pieces = 300
    deal_comparison = compare_candy_deals(option1_cost, option1_pieces, option2_cost, option2_pieces)
    
    # Create parade summary
    summary = create_parade_summary(float_theme, total_spectators, total_candy, total_cost)
    
    # Display results in a festive, formatted way
    print("=== 👥 Crowd Estimation ===")
    print(f"Estimated spectators along route: {total_spectators} people")
    print(f"Total candy pieces needed: {total_candy} pieces")
    print(f"Candy bags to buy: {bags_needed} bags")
    print()
    
    print("=== 💰 Cost Breakdown ===")
    print(f"Float decorations: ${decoration_cost:.2f}")
    print(f"Costumes: ${costume_cost:.2f}")
    print(f"Candy: ${candy_cost:.2f}")
    subtotal = decoration_cost + costume_cost + candy_cost
    tax_amount = subtotal * tax_rate
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax ({tax_rate*100:.0f}%): ${tax_amount:.2f}")
    print(f"Total cost: ${total_cost:.2f}")
    print()
    
    print("=== 🍬 Candy Deal Comparison ===")
    print(f"Option 1: ${option1_cost:.2f} for {option1_pieces} pieces (${option1_cost/option1_pieces:.3f} per piece)")
    print(f"Option 2: ${option2_cost:.2f} for {option2_pieces} pieces (${option2_cost/option2_pieces:.3f} per piece)")
    print(f"💡 {deal_comparison}")
    print()
    
    print("=== 🌊 Parade Summary ===")
    print(summary)
    print()
    
    print("Ready for the Meadville Halloween Parade! 🎃🌊👻")

if __name__ == "__main__":
    main()
