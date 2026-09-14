"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time = 10):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining

print(bake_time_remaining)

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time remaining.

    Parameters:
        number_of_layers (int): The magic number

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function multiply this by 2 and return int.
    """
    PREPARATION_TIME = number_of_layers * 2

    return PREPARATION_TIME


print(preparation_time_in_minutes)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the preparation time remaining.

    Parameters:
        number_of_layers (int): The magic number
        elapsed_bake_time (int): The baking time already elapsed.
        
    Returns:
        int: time multiple preparation and sum bake time
    """
    PREPARATION_TIME = number_of_layers * 2
    bake_time = PREPARATION_TIME + elapsed_bake_time
    
    return bake_time


print(elapsed_time_in_minutes)