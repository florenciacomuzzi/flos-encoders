import pytest

from integer_encoder.integer_encoder import IntegerEncoder


@pytest.mark.parametrize(
    'input, expected',
    [(1, bytes('{0:b}'.format(int('0', 2)), 'utf-8')),
     (2, bytes('{0:b}'.format(int('10', 2)), 'utf-8')),
     (3, bytes('{0:b}'.format(int('110', 2)), 'utf-8')),
     (4, bytes('{0:b}'.format(int('1110', 2)), 'utf-8')),
     (6, bytes('{0:b}'.format(int('111110', 2)), 'utf-8')),
     (8, bytes('{0:b}'.format(int('11111110', 2)), 'utf-8'))])
def test_unary_encoder(input, expected):
    assert expected == IntegerEncoder.unary_encoder(input)


@pytest.mark.parametrize(
    'expected, input',
    [(1, bytes('{0:b}'.format(int('0', 2)), 'utf-8')),
     (2, bytes('{0:b}'.format(int('10', 2)), 'utf-8')),
     (3, bytes('{0:b}'.format(int('110', 2)), 'utf-8')),
     (4, bytes('{0:b}'.format(int('1110', 2)), 'utf-8')),
     (6, bytes('{0:b}'.format(int('111110', 2)), 'utf-8')),
     (8, bytes('{0:b}'.format(int('11111110', 2)), 'utf-8'))])
def test_unary_decoder(expected, input):
    assert expected == IntegerEncoder.unary_decoder(input)


@pytest.mark.parametrize(
    'input', [(-6), (0)])
def test_unary_encoder_out_of_range(input):
    with pytest.raises(ValueError):
        assert IntegerEncoder.unary_encoder(input)


@pytest.mark.parametrize(
    'input, expected',
    [(1, bytes('{0:b}'.format(int('0', 2)), 'utf-8')),
     (2, bytes('{0:b}'.format(int('100', 2)), 'utf-8')),
     (4, bytes('{0:b}'.format(int('11000', 2)), 'utf-8')),
     (9, bytes('{0:b}'.format(int('1110001', 2)), 'utf-8')),
     (24, bytes('{0:b}'.format(int('111101000', 2)), 'utf-8')),
     (511, bytes('{0:b}'.format(int('11111111011111111', 2)), 'utf-8')),
    ])
def test_elias_gamma_encoder(input, expected):
    assert expected == IntegerEncoder.elias_gamma_encoder(input)


@pytest.mark.parametrize(
    'expected, input',
    [(1, bytes('{0:b}'.format(int('0', 2)), 'utf-8')),
     (2, bytes('{0:b}'.format(int('100', 2)), 'utf-8')),
     (4, bytes('{0:b}'.format(int('11000', 2)), 'utf-8')),
     (9, bytes('{0:b}'.format(int('1110001', 2)), 'utf-8')),
     (24, bytes('{0:b}'.format(int('111101000', 2)), 'utf-8')),
     (511, bytes('{0:b}'.format(int('11111111011111111', 2)), 'utf-8')),
    ])
def test_elias_gamma_decoder(expected, input):
    assert expected == IntegerEncoder.elias_gamma_decoder(input)
