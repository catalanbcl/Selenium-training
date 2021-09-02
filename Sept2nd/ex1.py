# break integer into single digits
number = 12345678848262641

digits = []

while number > 0:
    digits.insert(0, number % 10)
    # double division sign returns a integer instead of a double
    number = (number - number % 10)//10

print(*digits)