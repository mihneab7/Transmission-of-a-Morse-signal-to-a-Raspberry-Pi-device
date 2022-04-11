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

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name = 'Combine the message with GPS coordinates',   # will show up in GRC
            in_sig = [np.byte],
            out_sig = [np.byte]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        file = open("/home/mihneab/PycharmProjects/Licenta/testGPS2.txt", "r")
        lines = file.read()
        file.close()
        #lines = lines.replace("\n", "")
        goodString = ""       
        lines = lines[:-1]            
        lines = lines.strip()
        intermediar = lines.split(",")
        for bit in intermediar:
            goodString += str(bit)
        inputMessage = str(input_items[0])
        inputMessage = inputMessage.replace("[", "")
        inputMessage = inputMessage.replace("]", "")
        inputMessage = inputMessage.replace(" ", "")
        finalMessage = goodString + inputMessage
        for i in range(len(finalMessage)):
            output_items[0][:] = finalMessage[i]
        #for element in finalMessage:
            #output_items[0][:] = element
        file = open("/home/mihneab/PycharmProjects/Licenta/testGPS3.txt", "w")
        file.write(str(output_items[0]))
        file.close()        
        #intermediar = intermediar.pop()        
        #output_items[0][:] = input_items[0] * self.example_param
        return len(output_items[0])
