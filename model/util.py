import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    
    random_id = ""

    for i in range(number_of_small_letters):
        abc_lower = string.ascii_lowercase
        random_char = random.choice(abc_lower)
        random_id += random_char

    for i in range(number_of_capital_letters):
        abc_upper = string.ascii_uppercase
        random_char = random.choice(abc_upper)
        random_id += random_char
    
    for i in range(number_of_digits):
        digit = random.randint(0, 9)
        random_id += str(digit)
    
    for i in range(number_of_special_chars):
        random_char = random.choice(allowed_special_chars)
        random_id += random_char
    
    random_id = ''.join(random.sample(random_id,len(random_id)))
    
    return random_id


