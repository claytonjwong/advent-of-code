#include <iostream>
#include <sstream>
#include "input.hpp"

using namespace std;

class Solution {
public:
    int minSteps( const string& input, char delim=',' ){
        auto x{ 0 }, y{ 0 };
        istringstream stream{ input };
        for( string dir; stream >> dir >> delim; ){
        }
    }
};

int main() {
    Solution solution;
    auto ans = solution.minSteps( INPUT );
    return 0;
}
