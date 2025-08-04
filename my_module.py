# my_module.py

# Function to greet a user
def greet_user(name):
    """Display a greeting message."""
    print(f"Hello, {name.title()}! Welcome to the module demo.")

# Function to describe a pet
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Function to make a pizza
def make_pizza(size, *toppings):
    """Print the list of toppings for a pizza."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")
