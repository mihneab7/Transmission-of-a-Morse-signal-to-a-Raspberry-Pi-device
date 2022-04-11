"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt

shortMorseDictionary = {
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
    "?": "1,0,1,0,1,1,1,0,1,1,1,0,1,0,1"    
    }


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Binary Morse Encoder (GPS)',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.byte]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        global shortMorseDictionary
        bits = ""
        file = open("/home/mihneab/PycharmProjects/Licenta/testGPS.txt", "r")
        intermediar = file.read()
        file.close()

        for character in intermediar:
            if (not(character in shortMorseDictionary)):
                character = "?"
            dots = str(shortMorseDictionary.get(character))
            bits = bits + dots
            bits = bits + ",0,0,0,"

        file2 = open("/home/mihneab/PycharmProjects/Licenta/testGPS2.txt", "w")
        file2.write(bits)







        #for element in input_items:
            #element = str(element)
            #for character in element:
                #if (not(character in shortMorseDictionary)):
                    #character = "?"
                #dots = str(shortMorseDictionary.get(character))
                #bits = bits + dots
                #bits = bits + ",0,0,0,"
            #file = open("/home/mihneab/PycharmProjects/Licenta/testGPS2.txt", "w")
            #file.write(element)
            #file.write(" pauza ")
            #file.close()





        #for element in input_items:
         #   stringElement = str(element)
          #  character = stringElement.upper()
           # if (not(character in shortMorseDictionary)):
            #    character = "?"
            #dots = str(shortMorseDictionary.get(character))
            #bits = bits + dots
            #bits = bits + ",0,0,0,"
       # length = len(bits)
        #elementNumber = int((length + 1) / 2)
        #for i in range(length):
         #   out = int(i / 2)
          #  if (bits[i] == "1"):
           #     output_items[0][out] = 1
            #elif (bits[i] == "0"):
             #   output_items[0][out] = 0
           # else:
            #    continue

        #if (len (input_items) > 0):
            #input_items = str(input_items)
            #for element in input_items:
                # get next char
                #stringElement = str (element)
                # convert to upper case
                #character = stringElement.upper()
                # test for character in table
                #if (not(character in shortMorseDictionary)):
                # print ("bad char", ch)
                 #   character = "?"        # replace bad character with a '?'
                # build vector
                #dots = str (shortMorseDictionary.get(character))
                # print (ch, _dots)
                #bits += (dots + ",0,0,0,")    # letter space
        
            #length = len(bits)
            # num of elements = (length+1) / 2
            #elementNumber = int((length + 1) / 2)

            # convert and store elements in output array
            #for i in range (length):
                #out = int(i / 2)
                #if (bits[i] == '1'):
                    #output_items[0][out] = 1
                #elif (bits[i] == '0'):
                #    output_items[0][out] = 0
                #else:
                 #   continue    # skip commas
        #else:
            #elementNumber = 0
        #file = open("/home/mihneab/PycharmProjects/Licenta/testGPS2.txt", "w")
        #file.write(str(input_items))
        #file.close()
        #output_items[0][:] = input_items[0] * self.example_param
        return len(bits)
