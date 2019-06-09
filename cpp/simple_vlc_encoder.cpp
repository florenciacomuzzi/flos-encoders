//
//  simple_vlc_encoder.cpp
//

#include "simple_vlc_encoder.hpp"
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include<iostream>

using namespace std;

std::map<char,std::string> get_codeword_table(std::map<char,int> histogram) {
    std::string codes[] = {"11", "00", "011", "101", "0100", "0101"};
    // order histogram by frequency of occurrence in descending order
    // assign codes
    // doesn't work because some symbols have the same frequency
    std::vector<int> frequencies;
    for(auto entry : histogram) {
        frequencies.push_back(entry.second);
    }
    sort(frequencies.begin(), frequencies.end(), greater <int>());
    for(auto freq : frequencies) {
        cout << freq << "\n";
    }
    std::map<char,std::string> codeword_table;
    for(int freq = 0; freq < frequencies.size(); freq++) {
        for(auto entry: histogram) {
            if(entry.second == frequencies[freq]) {
                codeword_table[entry.first] = codes[freq];
            }
        }
    }
    for(auto code_to_word: codeword_table) {
        std::cout << "key = " << code_to_word.first << " value = " << code_to_word.second << "\n";
    }
    return codeword_table;
    
}

std::map<char,int> get_histogram(string str) {
    // create histogram
    std::map<char,int> histogram;
    string::iterator it;
    for (it = str.begin(); it < str.end(); it++) {
        ++histogram[*it];
    }
    return histogram;
}


string encode(string str) {
    // create histogram and maintain order by more frequent symbol
    std::map<char,int> histogram = get_histogram(str);
    for(auto elem : histogram)
    {
        std::cout << "key = " << elem.first << " value = " << elem.second << "\n";
    }
    std::map<char,std::string> codeword_table = get_codeword_table(histogram);
    
    std::string encoded = "";
    string::iterator it;
    for (it = str.begin(); it < str.end(); it++) {
        encoded += codeword_table[*it];
    }
    return encoded;
    // assign symbols
    // encode
}


int main() {
    cout << encode("TOBEORNOTTOBEORTOBEORNOT") << "\n";
    return 0;
}

