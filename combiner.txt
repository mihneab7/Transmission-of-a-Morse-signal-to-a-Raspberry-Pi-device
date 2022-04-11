"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name = 'Combine the message with GPS coordinates',   # will show up in GRC
            in_sig = [np.byte],
            out_sig = [np.byte]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).

    def work(self, input_items, output_items):
        """This should combine GPS coordinates and the input message seamlessly"""
        # read the encoded GPS coordinates
        file = open("/home/mihneab/PycharmProjects/Licenta/testGPS2.txt", "r")
        lines = file.read()
        file.close()

        goodString = ""
       
        # remove whitespace from the end, split by comma
        lines = lines[:-1]            
        lines = lines.strip()
        intermediary = lines.split(",")
        
        # add the bits in a string
        for bit in intermediary:
            goodString += str(bit)

        # read the input from the binary morse encoder block and process it
        inputMessage = str(input_items[0])
        inputMessage = inputMessage.replace("[", "")
        inputMessage = inputMessage.replace("]", "")
        inputMessage = inputMessage.replace(" ", "")
        # combine the GPS coordinates and the input message
        finalMessage = goodString + inputMessage

        # write them to the output
        for i in range(len(finalMessage)):
            output_items[0][:] = finalMessage[i]
        
        # write them in a file in order to be checked
        file = open("/home/mihneab/PycharmProjects/Licenta/testGPS3.txt", "w")
        file.write(str(output_items[0][:]))
        file.close()        

        return len(output_items[0])
