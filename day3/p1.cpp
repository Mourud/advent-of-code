#include <iostream>
#include <string>
#include <curlpp/cURLpp.hpp>
#include <curlpp/Options.hpp>

curlpp::Cleanup myCleanup;

std::ostringstream os;

os << curlpp::options::Url(std::string("http://adventofcode.com/2022/day/3/input"))

string input = os.str();

int main(){
    std::cout << input << etd::endl;
    return 0;
}