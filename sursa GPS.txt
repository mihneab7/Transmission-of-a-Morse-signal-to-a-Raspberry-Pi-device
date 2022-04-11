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

    def __init__(self, path='/home/mihneab/PycharmProjects/Licenta/coordinates.txt'):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name = 'GPS Source',   # will show up in GRC
            in_sig = None,
            out_sig = [np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).m
        self.path = path

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        # read the acquired coordinates and process them        
        file = open(self.path, "r")
        interm = file.read()
        listInterm = interm.split()
        length = len(listInterm)
        
        # since 2 float/double values are expected, they can be written directly to the output
        output_items[0][0] = listInterm[0]
        output_items[0][1] = listInterm[1]
        
        # write the output in a file for viewing
        file = open("/home/mihneab/PycharmProjects/Licenta/testGPS.txt", "w")
        file.write(str(output_items[0][0]))
        file.write(" ")
        file.write(str(output_items[0][1]))
        file.close()
        return len(output_items[0][:length])
