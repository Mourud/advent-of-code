#include <iostream>
#include <string>
#include <sstream>
#include <curlpp/cURLpp.hpp>
#include <curlpp/Options.hpp>
#include <curlpp/Easy.hpp>

int main() {
    curlpp::Cleanup myCleanup;

    // Create an ostringstream to write the result to.
    std::ostringstream os;

    // Create an instance of curlpp::Easy.
    curlpp::Easy request;

    // Set the URL option on the request.
    request.setOpt(new curlpp::options::Url("http://adventofcode.com/2022/day/3/input"));
    
    // Set the WriteStream option on the request to write to the ostringstream.
    request.setOpt(new curlpp::options::WriteStream(&os));

    // Perform the request.
    request.perform();

    // Extract the result.
    std::string result = os.str();

    std::cout << result << std::endl;

    return 0;
}
