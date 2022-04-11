import numpy as np

morseBinary = {
  # codes from https://www.itu.int/rec/R-REC-M.1677-1-200910-I/en
    "A": "1,0,1,1,1",
    "B": "1,1,1,0,1,0,1,0,1",
    "C": "1,1,1,0,1,0,1,1,1,0,1",
    "D": "1,1,1,0,1,0,1",
    "E": "1",
    "F": "1,0,1,0,1,1,1,0,1",
    "G": "1,1,1,0,1,1,1,0,1",
    "H": "1,0,1,0,1,0,1",
    "I": "1,0,1",
    "J": "1,0,1,1,1,0,1,1,1,0,1,1,1",
    "K": "1,1,1,0,1,0,1,1,1",
    "L": "1,0,1,1,1,0,1,0,1",
    "M": "1,1,1,0,1,1,1",
    "N": "1,1,1,0,1",
    "O": "1,1,1,0,1,1,1,0,1,1,1",
    "P": "1,0,1,1,1,0,1,1,1,0,1",
    "Q": "1,1,1,0,1,1,1,0,1,0,1,1,1",
    "R": "1,0,1,1,1,0,1",
    "S": "1,0,1,0,1",
    "T": "1,1,1",
    "U": "1,0,1,0,1,1,1",
    "V": "1,0,1,0,1,0,1,1,1",
    "W": "1,0,1,1,1,0,1,1,1",
    "X": "1,1,1,0,1,0,1,0,1,1,1",
    "Y": "1,1,1,0,1,0,1,1,1,0,1,1,1",
    "Z": "1,1,1,0,1,1,1,0,1,0,1",
    " ": "0",            # space
    "1": "1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1",
    "2": "1,0,1,0,1,1,1,0,1,1,1,0,1,1,1",
    "3": "1,0,1,0,1,0,1,1,1,0,1,1,1",
    "4": "1,0,1,0,1,0,1,0,1,1,1",
    "5": "1,0,1,0,1,0,1,0,1",
    "6": "1,1,1,0,1,0,1,0,1,0,1",
    "7": "1,1,1,0,1,1,1,0,1,0,1,0,1",
    "8": "1,1,1,0,1,1,1,0,1,1,1,0,1,0,1",
    "9": "1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1",
    "0": "1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1",
    ".": "1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1",          # period
    ",": "1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1",      # comma
    ":": "1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1",          # colon
    "?": "1,0,1,0,1,1,1,0,1,1,1,0,1,0,1",              # question
    "'": "1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1",      # apostrophe
    "-": "1,1,1,0,1,0,1,0,1,0,1,0,1,1,1",              # dash or minus
    "/": "1,1,1,0,1,0,1,0,1,1,1,0,1",                  # slash
    "(": "1,1,1,0,1,0,1,1,1,0,1,1,1,0,1",              # left parenthesis
    ")": "1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1",      # right parenthesis
    "\"": "1,0,1,1,1,0,1,0,1,0,1,1,1,0,1",             # quote
    "=": "1,1,1,0,1,0,1,0,1,0,1,1,1",                  # equals
    "+": "1,0,1,1,1,0,1,0,1,1,1,0,1",                  # plus
    "@": "1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1",          # at sign (@)
  # these punctuation marks are not included in the ITU recommendation,
  # but are found in https://en.wikipedia.org/wiki/morseBinary_code
    "!": "1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1",      # exclamation point
    "&": "1,0,1,1,1,0,1,0,1,0,1",                      # ampersand (also prosign for 'WAIT')
    ";": "1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1",          # semicolon
    "_": "1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1",          # underscore
    "$": "1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1"           # dollar sign
      }

morseCode = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",            # space
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",          # period
    ",": "--..--",      # comma
    ":": "---...",          # colon
    "?": "..--..",              # question
    "'": ".----.",      # apostrophe
    "-": "-....-",              # dash or minus
    "/": "-..-.",                  # slash
    "(": "-.--.",              # left parenthesis
    ")": "-.--.-",      # right parenthesis
    "\"": ".-..-.",             # quote
    "=": "-...-",                  # equals
    "+": ".-.-.",                  # plus
    "@": ".--.-.",          # at sign (@)
  # these punctuation marks are not included in the ITU recommendation,
  # but are found in https://en.wikipedia.org/wiki/morseBinary_code
    "!": "-.-.--",      # exclamation point
    "&": ".-...",                      # ampersand (also prosign for 'WAIT')
    ";": "-.-.-.",          # semicolon
    "_": "..--.-",          # underscore
    "$": "...-..-"           # dollar sign
}

textBoxValue = input("Enter the message here: ")
bitVector = ""
output = ""
output = dict(output)

if (len(textBoxValue) > 0):
    for character in textBoxValue:
        # convert to string in case the input is made up of numbers only
        toString = str(character)
        # convert to uppercase cuz this is the standard
        upperCharacter = toString.upper()
        # if there is a character that is not in the Morse table, replace it with a question mark
        if (not(upperCharacter in morseBinary)):
            upperCharacter = "?"
        # this is the binary morse code, convert it to string to process it further
        binaryMorseStream = str(morseBinary.get(upperCharacter))
        # construct the bit vector; add 0,0,0 to separate letters
        bitVector = bitVector + binaryMorseStream + ",0,0,0,"
    # if (bitVector[-1] == ","):
    #     bitVector = bitVector[0:len(bitVector) - 1]
    # print(bitVector)

    # finish the stream with a "space"
    bitVector = bitVector + "0,0,0,0"
    bitVectorLength = len(bitVector)
    # compute the number of elements (bits), without the commas
    # the number of commas is the number of elements - 1
    numberOfElements = int((bitVectorLength + 1) / 2)
    for x in range(bitVectorLength):
        y = int(x / 2)
        # print(y)
        if (bitVector[x] == "1"):
            output[y] = 1
        elif (bitVector[x] == "0"):
            output[y] = 0
        else:
            continue

else:
    numberOfElements = 0

for i in output:
    print(output[i])