"""
I am working through McAnlis' and Haecky's Understanding Compression book.
Chapter 4 is on variable-length codes.
"""


class IntegerEncoder(object):

    @staticmethod
    def unary_encoder(num):
        """Unary coding represents a positive integer, n,
        with n-1 ones followed by a zero.

        The length of the codewords grows linearly by 1 for increasing numbers.
        This code works best for datasets where each symbol is twice as
        probable as the previous.

        :param num (int)
        :return: bytearray
        """
        if num < 1:
            raise ValueError('Unary coding represents positive integers.'
                             ' {} is invalid.'.format(num))
        code = bytearray()
        for bit in range(0, num-1):
            code.append(1)
        code.append(0)
        return code

    @staticmethod
    def unary_decoder(code):
        """Unary decoder returns the original integer.

        The decoder reads and counts value bits from the stream until
        delimiter is reached. Adds 1 to the count and outputs that number.

        :param code (bytearray)
        :return (int)
        """
        count = 0
        num = ''
        for bit in code:
            if bit == 0:
                num += str(count + 1)
                count = 1
            count += 1
        return int(num)

    @staticmethod
    def elias_gamma_encoder(seq):
        num = seq
        encoded = bytearray()
        while num:
            digit = num % 10
            print(digit)
            unary_code = IntegerEncoder.unary_encoder(digit)

            print(unary_code)
            num = num // 10
        return encoded

    @staticmethod
    def elias_gamma_decoder(seq):
        pass


if __name__ == '__main__':
    encoded = IntegerEncoder.unary_encoder(6)
    print(encoded)
    decoded = IntegerEncoder.unary_decoder(encoded)
    print(decoded)
    # print(IntegerEncoder.elias_gamma_encoder(2))
