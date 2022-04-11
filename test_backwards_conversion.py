morseCode = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "/": " ",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
    ".-.-.-": ".",          # period
    "--..--": ",",      # comma
    "---...": ":",          # colon
    "..--..": "?",              # question
    ".----.": "'",      # apostrophe
    "-....-": "-",              # dash or minus
    "-..-.": "/",                  # slash
    "-.--.": "(",              # left parenthesis
    "-.--.-": ")",      # right parenthesis
    ".-..-.": "\"",             # quote
    "-...-": "=",                  # equals
    ".-.-.": "+",                  # plus
    ".--.-.": "@",          # at sign (@)
  # these punctuation marks are not included in the ITU recommendation,
  # but are found in https://en.wikipedia.org/wiki/morseBinary_code
    "-.-.--": "!",      # exclamation point
    ".-...": "&",                      # ampersand (also prosign for 'WAIT')
    "-.-.-.": ";",          # semicolon
    "..--.-": "_",          # underscore
    "...-..-": "$"           # dollar sign
}

#morse = "1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0000"
morse = "10101000111011101110001010100000001010100011101110111000101010000000"
#morse = "10111000111010001011100000001011100010111010001000000011101110001000101110100010000000"
#morse = "00001000000010000000"
morse = morse.replace(",", "")
morse = morse.replace("0000000", "/")
morse = morse.replace("111", "-")
morse = morse.replace("000", " ")
#morse = morse.replace("0", "")
morse = morse.replace("1", ".")
morse = morse[:-1]
morseList = morse.split(" ")
testList = []
newString = []
for sequence in morseList:
    sequenceClear = sequence.replace("0", "")
    #sequenceClear = sequenceClear.split("/")
    if ("/" in sequenceClear):
        slashPosition = sequenceClear.find("/")
        finalSequence = sequenceClear[:slashPosition] + " " + "/" + " " + sequenceClear[slashPosition + 1:]
        finalSequence = finalSequence.split(" ")
        for subsequence in finalSequence:
            testList.append(subsequence)
    else:
        testList.append(sequenceClear)

translation = ""
for character in testList:
    if (not(character in morseCode)):
        character = "?"
    else:
        character = morseCode.get(character)
    translation += character

print(translation)