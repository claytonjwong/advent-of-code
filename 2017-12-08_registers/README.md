# Day 8: I Heard You Like Registers
* [https://adventofcode.com/2017/day/8](https://adventofcode.com/2017/day/8)

## Part One
What is the largest value in any register after completing the instructions in your puzzle input? ```4416```

## Part Two
What is the highest value held in any register during this process? ```5199```

## Solution
```cpp
#include <iostream>
#include <sstream>
#include <regex>
#include <unordered_map>
#include <numeric>
#include "input.hpp"

using namespace std;

class Solution {
public:
    using SymbolTable = unordered_map< string, int >;
    using Result = pair< int,int >;
    Result maxRegister( const string& input, string line={}, smatch group=smatch{}, SymbolTable table={} ){
        auto maxEnd = numeric_limits< int >::min(),
             maxAll = numeric_limits< int >::min();
        regex pattern{ "^(\\w+) (inc|dec) ([-]?\\d+) if (\\w+) ([!=<>]+) ([-]?\\d+)$" };
        for( istringstream stream{ input }; getline( stream, line ); ){
            if( regex_match( line, group, pattern ) && group.size() == 7 ){
                auto s1 = group[ 1 ],  // first (s)ymbol
                     op = group[ 2 ],  // (op)eration
                     s2 = group[ 4 ],  // second (s)ymbol
                     ch = group[ 5 ];  // predicate constraint to (ch)eck
                auto v1{ 0 }, v2{ 0 }; // first/second (v)alue
                {
                    stringstream parser;
                    parser << group[ 3 ] << " " << group[ 6 ];
                    parser >> v1 >> v2;
                }
                bool predicate =
                    ( ch == "<"  && table[ s2 ] <  v2 ) ||
                    ( ch == "<=" && table[ s2 ] <= v2 ) ||
                    ( ch == ">"  && table[ s2 ] >  v2 ) ||
                    ( ch == ">=" && table[ s2 ] >= v2 ) ||
                    ( ch == "==" && table[ s2 ] == v2 ) ||
                    ( ch == "!=" && table[ s2 ] != v2 );
                if( predicate ){
                    table[ s1 ] += ( op == "inc" )? v1 : -v1;
                    if( maxAll < table[ s1 ] )
                        maxAll = table[ s1 ];
                }
            }
        }
        for( const auto& pair: table ){
            auto symbol = pair.first;
            auto value = pair.second;
            if( maxEnd < value )
                maxEnd = value;
        }
        return{ maxEnd, maxAll };
    }
};

int main() {
    Solution solution;
    auto[ maxEnd, maxAll ] = solution.maxRegister( INPUT );
    cout << "part 1: " << maxEnd << endl
         << "part 2: " << maxAll << endl;
    return 0;
}
```
