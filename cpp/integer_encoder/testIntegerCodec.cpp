#include <gtest/gtest.h>
#include "IntegerCodec.hpp"


TEST(TestSuiteName, correct_output){
    ASSERT_EQ(IntegerCodec::unary_encoder(1), std::vector<bool>({0})) << "Result is wrong.";
    ASSERT_EQ(IntegerCodec::unary_encoder(5), std::vector<bool>({1,1,1,1,0})) << "Result is wrong.";
    ASSERT_EQ(IntegerCodec::unary_encoder(10), std::vector<bool>({1,1,1,1,1,1,1,1,1,0})) << "Result is wrong.";
}

TEST(TestSuiteName, invalid_arg){
    try {
        IntegerCodec::unary_encoder(0);
    } catch (std::invalid_argument const &err) {
        EXPECT_EQ(err.what(),std::string("Unary coding represents positive integers."));
    } catch (...) {
        FAIL() << "Expected std::invalid_argument" << std::endl;
    }
}