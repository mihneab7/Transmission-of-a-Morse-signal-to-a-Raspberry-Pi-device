"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt

# shorter dictionary since only digits, periods and spaces are expected
shortMorseDictionary = {
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
    "?": "1,0,1,0,1,1,1,0,1,1,1,0,1,0,1"    
    }


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Binary Morse Encoder (GPS)',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=None
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        global shortMorseDictionary

        bits = ""
        # read the GPS coordinates
        file = open("/home/mihneab/PycharmProjects/Licenta/testGPS.txt", "r")
        intermediary = file.read()
        file.close()
        # similar check with the main encoder
        for character in intermediary:
            if (not(character in shortMorseDictionary)):
                character = "?"
            dots = str(shortMorseDictionary.get(character))
            bits = bits + dots
            bits = bits + ",0,0,0,"
        # write the result in a file
        file2 = open("/home/mihneab/PycharmProjects/Licenta/testGPS2.txt", "w")
        file2.write(bits)
        file2.close()

        return len(bits)
