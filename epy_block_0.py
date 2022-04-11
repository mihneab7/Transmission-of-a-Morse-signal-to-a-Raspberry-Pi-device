"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt

guiString = ""

morseDictionary = {
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
    " ": "0",            
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
    ".": "1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1",          
    ",": "1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1",      
    ":": "1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1",          
    "?": "1,0,1,0,1,1,1,0,1,1,1,0,1,0,1",              
    "'": "1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1",      
    "-": "1,1,1,0,1,0,1,0,1,0,1,0,1,1,1",              
    "/": "1,1,1,0,1,0,1,0,1,1,1,0,1",                  
    "(": "1,1,1,0,1,0,1,1,1,0,1,1,1,0,1",              
    ")": "1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1",      
    "\"": "1,0,1,1,1,0,1,0,1,0,1,1,1,0,1",             
    "=": "1,1,1,0,1,0,1,0,1,0,1,1,1",                  
    "+": "1,0,1,1,1,0,1,0,1,1,1,0,1",                  
    "@": "1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1",           
    "!": "1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1",      
    "&": "1,0,1,1,1,0,1,0,1,0,1",                      
    ";": "1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1",          
    "_": "1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1",          
    "$": "1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1"           
    }

class blk(gr.sync_block):  
    """Binary Morse Encoder"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name = 'Binary Morse Encoder',   # will show up in GRC
            in_sig = None,
            out_sig = [np.byte]
        )

        self.message_port_register_out(pmt.intern("Clear"))
        self.message_port_register_in(pmt.intern("inputMessage"))
        self.set_msg_handler(pmt.intern("inputMessage"), self.guiMessage)
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).

    def guiMessage(self, message):

        global guiString

        coordinateFile = open("/home/mihneab/PycharmProjects/Licenta/coordinates.txt", "r")
        fileRead = coordinateFile.read() 
      
        guiString += fileRead
        guiString += " "        
        guiString += pmt.symbol_to_string(message)
        guiString = guiString.replace("\n", "")

        print(guiString)

    def work(self, input_items, output_items):
        """Turn GPS coordinates and the input message in binary"""
        global morseDictionary
        global guiString

        bits = ""

        if (len (guiString) > 0):
            for element in guiString:
                # convert to string in case there are just numbers
                stringElement = str(element)
                # convert to upper case
                character = stringElement.upper()
                # check if the character is in the dictionary
                if (not(character in morseDictionary)):
                    # unknown characters are replaced with ?                        
                    character = "?" 
                # save the morse character in a variable       
                morseCh = str(morseDictionary.get(character))
                # concatenate it to the bit string, 0,0,0 is the space between characters
                bits += (morseCh + ",0,0,0,")
            
            # concatenate 0,0,0,0 to mark the word's end
            bits += "0,0,0,0"

            # get the length of the string, commas included
            length = len(bits)
            # obtain number of commas
            commaNumber = bits.count(",")
            # obtain the number of elements, no commas included
            elementNumber = length - commaNumber
            # split by comma
            bitsSplit = bits.split(",")
            length = len(bitsSplit)

            # write the values in the output
            for i in range(length):
                output_items[0][i] = bitsSplit[i]
            
            # update the message edit box
            guiString = ""
            self.message_port_pub(pmt.intern('Clear'), pmt.intern(""))
        # in case there is no input        
        else:
            elementNumber = 0
        # not relevant
        return(elementNumber)
