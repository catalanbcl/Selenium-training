inputText = input('Type some text to count letters/characters/spaces: ')
# intialize count
numLetters = 0
numDigits = 0
numSp = 0
numSpaces = 0


for i in inputText:
    if i.isalpha():
        # counts letters
        numLetters += 1
    elif i.isdigit():
        # counts digits
        numDigits += 1
    elif i.isspace():
        # counts spaces
        numSpaces += 1
    else:
        # counts special characters
        numSp += 1

print('Number of spaces: ', numSpaces)
print('Number of letters: ', numLetters)
print('Number of digits: ', numDigits)
print('Number of special characters: ', numSp)