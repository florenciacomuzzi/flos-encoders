"""
I am working through McAnlis' and Haecky's Understanding Compression book.
Chapter 4 is on variable-length codes.
"""
import math


class IntegerEncoder(object):

    @staticmethod
    def unary_encoder(num):
        """Unary coding represents a positive integer, n,
        with n-1 ones followed by a zero.

        The length of the codewords grows linearly by 1 for increasing numbers.
        This code works best for datasets where each symbol is twice as
        probable as the previous.

        :param num (int)
        :return: bytes
        """
        if num < 1:
            raise ValueError('Unary coding represents positive integers.'
                             ' {} is invalid.'.format(num))
        code = ''
        for bit in range(0, num-1):
            code += str(1)
        code += str(0)
        return bytes('{0:b}'.format(int(code, 2)), 'utf-8')

    @staticmethod
    def unary_decoder(code):
        """Unary decoder returns the original integer.

        The decoder reads and counts value bits from the stream until
        delimiter is reached. Adds 1 to the count and outputs that number.

        :param code (bytes)
        :return: int
        """
        num = ''
        for count, bit in enumerate(code):
            # Python represents bytes as ints... delimiter = 0 --> 48
            if bit == 48:
                num += str(count + 1)
                return int(num)
            else:
                count += 1
        raise Exception('Invalid encoding. No delimiter found.')

    @staticmethod
    def elias_gamma_encoder(num):
        """Elias gamma encoder returns encoding for given positive integer.

        Elias gamma encoding is most commonly used for integers whose upper
        bound is unknown before processing.

        :param num (int)
        :return: bytes
        """
        if num < 1:
            raise ValueError('Elias gamma encoding represents positive '
                             'integers. {} is invalid.'.format(num))
        offset = bytes('{0:b}'.format(num), 'utf-8')[1:]
        selector = len(offset) + 1

        # encoding prefixes order of magnitude
        encoded = IntegerEncoder.unary_encoder(selector) + offset
        return encoded

    @staticmethod
    def elias_gamma_decoder(code):
        """Decoder returns the original integer according to the following
        formula:
            N = 2**n + L

        The decoder reads and counts value bits from the stream until
        delimiter is reached and decodes unary encoding. The length of the
        unary encoding determines the length, L, of the binary number that
        follows in the stream.

        :param code (bytes)
        :return: int
        """
        for count, bit in enumerate(code):
            # Python represents bytes as ints... delimiter = 0 --> 48
            if bit == 48:
                selector = IntegerEncoder.unary_decoder(code[:count+1])
                if selector == 1:
                    return selector
                offset = code[count+1:]
                thing = ''
                if len(offset) < selector:
                    for i in range(0, selector - len(offset)):
                        thing += str(1)
                offset_str = ''
                for i in offset:
                    if i == 48:
                        offset_str += str(0)
                    if i == 49:
                        offset_str += str(1)
                almost = thing + offset_str
                return int(almost, 2)
        raise Exception('Invalid encoding. No delimiter found.')


if __name__ == '__main__':
    print('Unary encoding')
    encoded = IntegerEncoder.unary_encoder(6)
    print(encoded)
    decoded = IntegerEncoder.unary_decoder(encoded)
    print(decoded)
    print('Elias gamma encoding')
    encoded = IntegerEncoder.elias_gamma_encoder(6)
    print(encoded)
    decoded = IntegerEncoder.elias_gamma_decoder(encoded)
    print(decoded)
