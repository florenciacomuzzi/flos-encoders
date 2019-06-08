"""
I am working through McAnlis' and Haecky's Understanding Compression book.
Chapter 4 is on variable-length codes.

```
usage: simple_vlc_encoder.py [-h] --input INPUT

Simple VLC Encoder

optional arguments:
  -h, --help     show this help message and exit
  --input INPUT  Input string. Max of 6 unique symbols.
```

Sample usage:
```
usage: simple_vlc_encoder.py --input TOBEORNOTTOBEORTOBEORNOT

Symbol	Count	Probability			Log2(p)	p*Log2(p)
O		8		1.3333333333333333		0.41503749927884376		0.5533833323717916
T		5		0.8333333333333334		-0.2630344058337938		-0.21919533819482817
R		3		0.5		-1.0		-0.5
E		3		0.5		-1.0		-0.5
B		3		0.5		-1.0		-0.5
N		2		0.3333333333333333		-1.5849625007211563		-0.5283208335737187
Average of 1.6941328393967554 bits per symbol to represent "TOBEORNOTTOBEORTOBEORNOT".
0011010010111011010111000011010010111011001101001011101101011100
```
"""
import argparse
import sys
from math import log2


class SimpleVLCEncoder(object):
    codes = ['11', '00', '011', '101', '0100', '0101']

    @staticmethod
    def encode(string):
        histogram = SimpleVLCEncoder._get_histogram(string)
        if len(histogram) > len(SimpleVLCEncoder.codes):
            raise ValueError('Invalid input: encoder supports encoding max of '
                             '{max} unique symbols. {provided} found.'.format(
                              max=len(SimpleVLCEncoder.codes),
                              provided=len(histogram)))
        codeword_table = SimpleVLCEncoder._get_codeword_table(histogram)
        bitstream = ''
        for char in string:
            bitstream += codeword_table[char]['code']
        return bitstream

    @staticmethod
    def _get_histogram(string):
        """Returns histogram of symbols and their occurrence in a string
        sorted by frequency of occurrence.
        """
        histogram = {}
        for char in string:
            histogram[char] = histogram[char] + 1 if histogram.get(char) else 1
        return dict(reversed(sorted(histogram.items(),
                                    key=lambda kv: (kv[1], kv[0]))))

    @staticmethod
    def _get_codeword_table(histogram):
        """Returns codeword table of symbol to code and frequency."""
        codeword_table = {}
        for index, (k, v) in enumerate(histogram.items()):
            codeword_table[k] = {'count': v,
                                 'code': SimpleVLCEncoder.codes[index]}
        return codeword_table

    @staticmethod
    def calculate_entropy(string):
        """Calculates entropy or the smallest number of bits required to
        represent a value following Claude Shannon's definition.
        """
        histogram = SimpleVLCEncoder._get_histogram(string)
        unique_symbols = len(histogram)
        entropy = 0
        print('Symbol\tCount\tProbability\t\t\tLog2(p)\tp*Log2(p)')
        for symbol, occurrence in histogram.items():
            p = float(occurrence)/float(unique_symbols)
            entropy += log2(p) * p
            print('{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(
                symbol, str(occurrence), str(p), log2(p), log2(p) * p))
        return entropy * -1


def parse_args(argz):
    parser = argparse.ArgumentParser(description='Simple VLC Encoder')
    parser.add_argument('--input', type=str, required=True,
                        help="Input string. Max of 6 unique symbols.")
    return parser.parse_args(argz)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    entropy = SimpleVLCEncoder.calculate_entropy(args.input)
    print('Average of {} bits per symbol to represent \"{}\".'.format(
        entropy, args.input))
    print(SimpleVLCEncoder.encode(args.input))
