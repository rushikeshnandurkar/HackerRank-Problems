"""
HackerRank Validating Credit Card Numbers problem
"""
import re

num_of_cards = int(input().strip())
for i in range(0, num_of_cards):
    credit_card_number = input().strip()
    is_card_valid = True

    pattern = re.compile(r'[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}')
    matches = pattern.match(credit_card_number)

    if matches is not None:     # comparison to None should always be performed with is OR is not operators
        if credit_card_number == matches.group(0):
            simplified_number = re.sub(r"[^\d]","",credit_card_number)
            pattern = re.compile(r"(0000|1111|2222|3333|4444|5555|6666|7777|8888|9999)")
            matches = pattern.search(simplified_number)
            if matches is not None:
                is_card_valid = False
        else:
            is_card_valid = False
    else:
        is_card_valid = False

    if is_card_valid:
        print("Valid")
    else:
        print("Invalid")