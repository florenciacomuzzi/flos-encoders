#pragma once

#include <bitset>
#include <vector>

#define M 32

class IntegerCodec {
private:
    static int digits(int);
public:
    // each element in bitset occupies only 1 bit
    static std::vector<bool> unary_encoder(int);
//    std::bitset<M> elias_gamma_encoder(int) const;

    static int unary_decoder(std::vector<bool>);
//    int elias_gamma_decoder(std::bitset<M>) const;
};