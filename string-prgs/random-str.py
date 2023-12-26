# Generating random strings until a given string is generated

import random
import string

def generate_randm_str(length):
    characters = string.ascii_letters + string.digits
    randm_chars = [random.choice(characters) for _ in range(length)]

    randm_string = ''.join(randm_chars)
    return randm_string

def generate_until_target(target_string):
    generate_string = ""
    attempts = 0

    while generate_string != target_string:
        generate_string = generate_randm_str(len(target_string))

        attempts += 1
    print(f"Attempt {attempts} : {generate_string}")
    print(f"Target string '{target_string}' generated in {attempts} attempts.")

# Test the function

target_string = "A"
generate_until_target(target_string)