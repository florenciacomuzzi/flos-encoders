#include <list>
#include <iostream>
#include <math.h>
#include "IntegerCodec.hpp"


int IntegerCodec::digits(int num) {
    int digits = ceil(log10(num));
    return digits;
}


std::vector<bool> IntegerCodec::unary_encoder(int num) {
    if(num < 1) {
        throw std::invalid_argument("Unary coding represents positive integers.");
    }
    std::vector<bool> code;
    for(int index = 0; index < num - 1; index++) {
        code.push_back(true);
    }
    code.push_back(false);


    for (std::vector<bool>::const_iterator i = code.begin(); i != code.end(); i++){
        std::cout << *i << ' ';
    }
    return code;
}
