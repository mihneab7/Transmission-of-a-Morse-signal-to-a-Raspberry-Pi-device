from converters import latinToMorse, morseToLatin

# The main function incorporates all of the functions necessary for the transmission and reception of the message:
# it reads the input of the user, it converts it into the Morse alphabet, then, at the reception,
# it converts it back to the Latin alphabet. The input is obtained using the built-in
# Python function, input(), which can take as argument the user's prompt and converts it into a string. The user prompt
# is then passed on as argument to the function latinToMorse(), which takes as input a string type. The function will
# return a list (stored in the morseArray variable) of each Morse character corresponding
# to each Latin character, in order to facilitate
# further processing of the data. The output is passed on as argument to the morseToLatin() function,
# which will convert the message written in Morse alphabet to a message written
# in Latin alphabet (stored in the latinArrayString variable). Thus, the final output to be printed
# will be the original message that was typed by the user, provided the transmission was successful. After the result
# is printed in the console, the user is prompted if he/she wishes to transmit another message. If the the answer is
# the character "y" (substitute for "yes"), then the program shall start again,
# following the same steps described previously.
# If the answer to the prompt is anything other than the character "y", then the program will stop, as the while loop
# is broken. The program may run infinitely, as long as the user wishes to keep transmitting messages.


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

if __name__ == '__main__':

    while True:

        morseArray = latinToMorse(input('Type the text to be transmitted: '))

        if (isinstance(morseArray, bool)):
            if (input('Pointless or invalid transmission.\nPlease provide a message that does not only contain'
                      ' whitespace characters and does not contain any characters besides'
                      ' the Latin alphabet and Arabic numerals.\nDo you wish to transmit a new message? ') == 'y'):
                continue
            else:
                break

        latinArrayString = morseToLatin(morseArray)

        print(latinArrayString)

        if (input('Do you wish to transmit a new message? ') == 'y'):
            continue
        else:
            break