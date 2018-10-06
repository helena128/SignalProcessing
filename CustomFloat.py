import math
import struct
import sys
from decimal import *


class CustomFloat:
    def __init__(self, numberDigits):
        self.numberDigits = numberDigits

    def format(self, value):
        self.value = value
        #print('Test value: %f' % value)  
        self.__process()

        ''' normal case and round '''
        return self.result

    def __process(self):
        binary = self.float_to_bin(self.value)
        binary_copy = binary
        #print(' float_to_bin:\t%r' % binary)
        digits = self.numberDigits
        i = 13

        # Trim binary string
        binary = list(binary)
        while i < len(binary):
            if i - 12 >= digits:
                binary[i] = '0'
            i += 1

        ''' + 1 case '''
        #binary = self.bin_ceil_plus_one(binary)

        ''' round '''
        binary = self.bin_round(binary, binary_copy)
        
        binary = ''.join(binary)
        #print(' float processed:\t%r' % binary, '\n')

        floating_point = self.bin_to_float(binary)
        #print(' bin_to_float: %f\n' % floating_point)
        self.result = floating_point

    def bin_round(self, num_to_ceil, num_copy):
        if num_copy[self.numberDigits + 1] == '1':
            num_to_ceil = self.bin_ceil_plus_one(num_to_ceil)
        return num_to_ceil

    def bin_ceil_plus_one(self, num_to_ceil):
        digits = self.numberDigits
        ''' + 1 and round cases '''
        #print('Unprocessed fraction', len(''.join(num_to_ceil)))
        fraction_part = list(str("{:0" + str(digits) + "b}")
                             .format(int(''.join(num_to_ceil[12:12+digits]),
                                         2) + 1))
        if len(fraction_part) < digits:
            #print('LITTLE. Required: ' + digits)
            fraction_part = list('0' * digits - len(fraction_part).join(fraction_part))
            #raise ValueError('Value: ', self.value)
        if len(fraction_part) > digits:
            #print('BIG. Required: ' + str(digits))
            #print('Before: ' + ''.join(fraction_part))
            #raise ValueError('Value: ', self.value)
            fraction_part = fraction_part[len(fraction_part)-digits: len(fraction_part)]
            #print('After: ' + ''.join(fraction_part), 'len:' , len(fraction_part))
            
            
        #print('Fraction', len(''.join(fraction_part)))
        
        num_to_ceil[12:12 + digits] = fraction_part
        #print('Converted: ', len(''.join(num_to_ceil)))
        return num_to_ceil

    def bin_to_float(self, b):
        """ Convert binary string to a float. """
        bf = self.int_to_bytes(int(b, 2), 8)
        return struct.unpack('>d', bf)[0]

    def int_to_bytes(self, n, minlen=0):
        """ Int/long to byte string.
            Python 3.2+ has a built-in int.to_bytes() method that could be
            used instead, but the following is portable.
        """
        nbits = n.bit_length() + (1 if n < 0 else 0)  # +1 for any sign bit.
        nbytes = (nbits + 7) // 8  # Number of whole bytes.
        b = bytearray()
        for _ in range(nbytes):
            b.append(n & 0xff)
            n >>= 8
        if minlen and len(b) < minlen:  # Zero padding needed?
            b.extend([0] * (minlen-len(b)))
        return bytearray(reversed(b))  # High bytes first.

    def float_to_bin(self, value):
        """ Convert float to 64-bit binary string. """
        [d] = struct.unpack(">Q", struct.pack(">d", value))
        return '{:064b}'.format(d)

'''
if __name__ == '__main__':
    # Unit test.
    test = CustomFloat(16)
    #for f in 0.0, 1.0, -14.0, 12.546, math.pi:
    #for f in 12.546, math.pi:
    for f in -1.0000, 0.0000, 1.000000, -1.000000, 0.999999999805694:
        print(test.format(f))
'''
