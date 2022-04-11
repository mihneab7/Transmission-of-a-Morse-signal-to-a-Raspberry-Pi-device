import time
from playsound import playsound

# The latinToMorse() function will process the user's input (a string obtained through the input() function) and
# transform it in a message written in Morse code. In the first steps it is required to process the message so that
# it is simpler to convert it. The objective is to obtain a message that contains only letters and numerals from
# the Latin alphabet, so no dashes ("-"), full stops ("."), ampersands ("&") or other similar characters. The whitespace
# characters space and tab are allowed, but the tab will be converted to a single space. Messages that contain only
# whitespace characters are not allowed, in order to prevent pointless transmissions.
# The input string is first converted to lower case (stored in the same variable), which is the standard chosen
# for the message in this project, then
# the message is split into an array which contains all the words (stored in the words variable),
# eliminating any whitespace characters.
# Several variables which will be used are also initialized: characterArray (stores all the Latin characters
# from the message, including space characters, but not of tab type), morseArray (similar to characterArray, but all
# the characters are now transformed into Morse characters), morseArrayString (contains the Morse message from
# morseArray, but written as a string, not an array), badTx (boolean variable which will signal if there is any issue
# with the input).
# For loops will be used to iterate through the list of words, as well as the characters of each word. The first loop
# uses the variable i as an index, which represents one word from the list. Each word is made up of characters, so the
# second loop iterates through the characters, using the c variable as index, which is then appended to the list of
# characters, characterArray. Since the words list does not contain the whitespaces from between the words, they must be
# added back to the message: after each word except the last one, a space character is added; when the program reaches
# the last word in the list, the loop is ended in order to prevent the appearance of a whitespace character at the end
# of the new list.
# To convert the message to Morse code, the program must also iterate through the list of characters obtained
# previously, using the c index, as in the previous loop. The boolean variable badTx has been initialized with a true
# value, so it should be assumed that the input is initially incorrect. The first use of this variable is to verify
# whether or not the message is entirely composed of whitespace characters. When the first non-whitespace character
# is found, the variable changes its value to false, and the evaluated condition also becomes false for the rest
# of the program. The next step is to convert every Latin character into Morse, according to the conversion chart
# (the space character will be represented by the forward slash character, "/"). Using an if-else conditional
# instruction, the character c is converted, and the corresponding Morse letter is added to the Morse array of
# characters, morseArray. If there is no match, the function will return the value true to the main function,
# because this signals that invalid characters were used. Earlier it was stated that space and tab characters may be
# used, but a message must contain at least one letter or numeral in order to represent a useful transmission, so the
# program shall evaluate once more the badTx boolean variable to determine if its value is true (case in which it has
# not been changed and indicates a message that contains only whitespace characters) or false (case in which its value
# has been changed, as a non-whitespace characters has been identified in the input string). Naturally, if badTx has
# indeed, a true value, it will return a true value to the main function, otherwise the program continues uninterrupted.
# Finally, the morseArray variable contains all Morse characters, separated by commas, so another and final for loop
# will be used in order to concatenate the elements of the array into a string, which may be read more easily by a
# human. The output to be transmitted is contained in morseArray, which is also the returned,
# as this form will prove it is much easier to convert back to the Latin alphabet, concluding the
# latinToMorse() function.

## A = .- ## B = -... ## C = -.-. ## D = -.. ## E = . ## F = ..-.
################################################################
## G = --. ## H = .... ## I = .. ## J == .--- ## K = -.-
################################################################
## L = .-.. ## M = -- ## N = -. ## O = --- ## P = .--.
################################################################
## Q = --.- ## R = .-. ## S = ... ## T = - ## U = ..-
################################################################
## V = ...- ## W = .-- ## X = -..- ## Y = -.-- ## Z = --..
################################################################
## 1 = .---- ## 2 = ..--- ## 3 = ...-- ## 4 = ....-
################################################################
## 5 = ..... ## 6 = -.... ## 7 = --... ## 8 = ---..
################################################################
## 9 = ----. ## 0 = -----

def latinToMorse(input):

    # example: input = "ana are mere"
    # output = ".--..-/.-.-../--..-.."
    # I might do it w/o slashes, they represent space characters, \s -> regex
    # Don't forget to mention that this is using ITU standard (Internation Telecommunication Union)
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
        " ": "/",  # space
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
        ".": ".-.-.-",  # period
        ",": "--..--",  # comma
        ":": "---...",  # colon
        "?": "..--..",  # question
        "'": ".----.",  # apostrophe
        "-": "-....-",  # dash or minus
        "/": "-..-.",  # slash
        "(": "-.--.",  # left parenthesis
        ")": "-.--.-",  # right parenthesis
        "\"": ".-..-.",  # quote
        "=": "-...-",  # equals
        "+": ".-.-.",  # plus
        "@": ".--.-.",  # at sign (@)
        # these punctuation marks are not included in the ITU recommendation,
        # but are found in https://en.wikipedia.org/wiki/morseBinary_code
        "!": "-.-.--",  # exclamation point
        "&": ".-...",  # ampersand (also prosign for 'WAIT')
        ";": "-.-.-.",  # semicolon
        "_": "..--.-",  # underscore
        "$": "...-..-"  # dollar sign
    }
    input = input.upper()
    words = input.split()
    characterArray = []
    morseArray = []
    morseArrayString = ''
    badTx = True

    for i in words:
        for c in i:
            characterArray.append(c)
        if (i == words[len(words) - 1]):
            break
        else:
            characterArray.append(' ')

    for c in characterArray:

        if (badTx):
            if c != ' ':
                badTx = False

        # if c == 'a':
        #     morseArray.append('.-')
        # elif c == 'b':
        #     morseArray.append('-...')
        # elif c == 'c':
        #     morseArray.append('-.-.')
        # elif c == 'd':
        #     morseArray.append('-..')
        # elif c == 'e':
        #     morseArray.append('.')
        # elif c == 'f':
        #     morseArray.append('..-.')
        # elif c == 'g':
        #     morseArray.append('--.')
        # elif c == 'h':
        #     morseArray.append('....')
        # elif c == 'i':
        #     morseArray.append('..')
        # elif c == 'j':
        #     morseArray.append('.---')
        # elif c == 'k':
        #     morseArray.append('-.-')
        # elif c == 'l':
        #     morseArray.append('.-..')
        # elif c == 'm':
        #     morseArray.append('--')
        # elif c == 'n':
        #     morseArray.append('-.')
        # elif c == 'o':
        #     morseArray.append('---')
        # elif c == 'p':
        #     morseArray.append('.--.')
        # elif c == 'q':
        #     morseArray.append('--.-')
        # elif c == 'r':
        #     morseArray.append('.-.')
        # elif c == 's':
        #     morseArray.append('...')
        # elif c == 't':
        #     morseArray.append('-')
        # elif c == 'u':
        #     morseArray.append('..-')
        # elif c == 'v':
        #     morseArray.append('...-')
        # elif c == 'w':
        #     morseArray.append('.--')
        # elif c == 'x':
        #     morseArray.append('-..-')
        # elif c == 'y':
        #     morseArray.append('-.--')
        # elif c == 'z':
        #     morseArray.append('--..')
        # elif c == '0':
        #     morseArray.append('-----')
        # elif c == '1':
        #     morseArray.append('.----')
        # elif c == '2':
        #     morseArray.append('..---')
        # elif c == '3':
        #     morseArray.append('...--')
        # elif c == '4':
        #     morseArray.append('....-')
        # elif c == '5':
        #     morseArray.append('.....')
        # elif c == '6':
        #     morseArray.append('-....')
        # elif c == '7':
        #     morseArray.append('--...')
        # elif c == '8':
        #     morseArray.append('---..')
        # elif c == '9':
        #     morseArray.append('----.')
        # elif c == ' ':
        #     morseArray.append('/')
        # else:
        #     return True

        if (c in morseCode):
            # return True
            morseArray.append(morseCode[c])
            print("am intrat aici")
        # else:
        #     morseArray.append(morseCode[c])
        #     badTx = False

    print(morseArray)
    if (badTx):
        return True

    for c in morseArray:
        morseArrayString += c

    print(characterArray)

    return morseArray

# In contrast to the morseToLatin() function, latinToMorse() aims to perform the reverse operation, as the name
# suggests. Its input is represented by the values stored in the morseArray variable and the desired output is the
# original message that was typed in by the user. Two variables are initialized: latinArray, which contains the Latin
# characters separated by comma, and latinArrayString, which contains the same characters, but concatenated into a
# string to provide improved viewing and reading of the message.
# A for loop is used to iterate through the input array of characters, each one of them being converted to a Latin
# character, according to the conversion chart. If the morseArray contains any value that is not in the chart, it will
# be simply added to the Latin array. In a similar manner to the morseToLatin() function, all Latin characters are
# concatenated into a string for better viewing and reading, using another for loop; this string value is also
# the one that is returned, since it will be stored in the database. Another for loop is started, having the objective
# of playing the correct Morse sounds, according to each word's dots and dashes. If the character is a dot ("."), the
# shorter tone is played, and if the character is a dash ("-"), the longer tone is played, thus allowing the user
# to distinguish the words. To account for the whitespace characters ("/"), the program's execution is paused for a
# period of 0.3 seconds using the sleep() function of the time module, which leads to an audible separation of the
# words. The sounds are played using the playsound() function, contained in the playsound module.

## A = .- ## B = -... ## C = -.-. ## D = -.. ## E = . ## F = ..-.
################################################################
## G = --. ## H = .... ## I = .. ## J == .--- ## K = -.-
################################################################
## L = .-.. ## M = -- ## N = -. ## O = --- ## P = .--.
################################################################
## Q = --.- ## R = .-. ## S = ... ## T = - ## U = ..-
################################################################
## V = ...- ## W = .-- ## X = -..- ## Y = -.-- ## Z = --..
################################################################
## 1 = .---- ## 2 = ..--- ## 3 = ...-- ## 4 = ....-
################################################################
## 5 = ..... ## 6 = -.... ## 7 = --... ## 8 = ---..
################################################################
## 9 = ----. ## 0 = -----

def morseToLatin(input):

    # example: input = ".--..-/.-.-../--..-.."
    # output = "ana are mere"

    latinArray = []
    latinArrayString = ''

    for c in input:
        if c == '.-':
            latinArray.append('a')
        elif c == '-...':
            latinArray.append('b')
        elif c == '-.-.':
            latinArray.append('c')
        elif c == '-..':
            latinArray.append('d')
        elif c == '.':
            latinArray.append('e')
        elif c == '..-.':
            latinArray.append('f')
        elif c == '--.':
            latinArray.append('g')
        elif c == '....':
            latinArray.append('h')
        elif c == '..':
            latinArray.append('i')
        elif c == '.---':
            latinArray.append('j')
        elif c == '-.-':
            latinArray.append('k')
        elif c == '.-..':
            latinArray.append('l')
        elif c == '--':
            latinArray.append('m')
        elif c == '-.':
            latinArray.append('n')
        elif c == '---':
            latinArray.append('o')
        elif c == '.--.':
            latinArray.append('p')
        elif c == '--.-':
            latinArray.append('q')
        elif c == '.-.':
            latinArray.append('r')
        elif c == '...':
            latinArray.append('s')
        elif c == '-':
            latinArray.append('t')
        elif c == '..-':
            latinArray.append('u')
        elif c == '...-':
            latinArray.append('v')
        elif c == '.--':
            latinArray.append('w')
        elif c == '-..-':
            latinArray.append('x')
        elif c == '-.--':
            latinArray.append('y')
        elif c == '--..':
            latinArray.append('z')
        elif c == '-----':
            latinArray.append('0')
        elif c == '.----':
            latinArray.append('1')
        elif c == '..---':
            latinArray.append('2')
        elif c == '...--':
            latinArray.append('3')
        elif c == '....-':
            latinArray.append('4')
        elif c == '.....':
            latinArray.append('5')
        elif c == '-....':
            latinArray.append('6')
        elif c == '--...':
            latinArray.append('7')
        elif c == '---..':
            latinArray.append('8')
        elif c == '----.':
            latinArray.append('9')
        elif c == '/':
            latinArray.append(' ')
        else:
            latinArray.append(c)
        for symbol in c:
            if symbol == '.':
                playsound("morse_tone_long.wav")
            elif symbol == "-":
                playsound("morse_tone_short.wav")
            else:
                time.sleep(0.3)
    for c in latinArray:
        latinArrayString += c

    return latinArrayString