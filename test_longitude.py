testInput = input("Enter the coordinate in NMEA format: ")
longDegrees = testInput[0:3]

if longDegrees[0] == "0":
    longDegrees = longDegrees[1:]

if input("Choose the hemisphere: ") == 'W':
    longitudeDegrees = float(longDegrees) * -1
else:
    longitudeDegrees = float(longDegrees)

longitudeDegrees = str(longitudeDegrees).strip('.0')
longDDD = testInput[3:10]
print(longDDD)
longMMM = float(longDDD) / 60
longMMM = str(longMMM).strip('0.')[:8]
longitude = longitudeDegrees + "." + longMMM
print(longitude)

# morseCode = {
#     "A": ".-",
#     "B": "-...",
#     "C": "-.-.",
#     "D": "-..",
#     "E": ".",
#     "F": "..-.",
#     "G": "--.",
#     "H": "....",
#     "I": "..",
#     "J": ".---",
#     "K": "-.-",
#     "L": ".-..",
#     "M": "--",
#     "N": "-.",
#     "O": "---",
#     "P": ".--.",
#     "Q": "--.-",
#     "R": ".-.",
#     "S": "...",
#     "T": "-",
#     "U": "..-",
#     "V": "...-",
#     "W": ".--",
#     "X": "-..-",
#     "Y": "-.--",
#     "Z": "--..",
#     " ": "/",            # space
#     "1": ".----",
#     "2": "..---",
#     "3": "...--",
#     "4": "....-",
#     "5": ".....",
#     "6": "-....",
#     "7": "--...",
#     "8": "---..",
#     "9": "----.",
#     "0": "-----",
#     ".": ".-.-.-",          # period
#     ",": "--..--",      # comma
#     ":": "---...",          # colon
#     "?": "..--..",              # question
#     "'": ".----.",      # apostrophe
#     "-": "-....-",              # dash or minus
#     "/": "-..-.",                  # slash
#     "(": "-.--.",              # left parenthesis
#     ")": "-.--.-",      # right parenthesis
#     "\"": ".-..-.",             # quote
#     "=": "-...-",                  # equals
#     "+": ".-.-.",                  # plus
#     "@": ".--.-.",          # at sign (@)
#   # these punctuation marks are not included in the ITU recommendation,
#   # but are found in https://en.wikipedia.org/wiki/morseBinary_code
#     "!": "-.-.--",      # exclamation point
#     "&": ".-...",                      # ampersand (also prosign for 'WAIT')
#     ";": "-.-.-.",          # semicolon
#     "_": "..--.-",          # underscore
#     "$": "...-..-"           # dollar sign
# }
#
# altString = ""
# stringTest = "SOS"
# for c in stringTest:
#     if (not(c in morseCode)):
#         # print("Character is valid")
#         print(c)
#     else:
#         altString += morseCode[c]
#
# print(altString)