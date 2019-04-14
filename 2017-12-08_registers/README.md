# Day 8: I Heard You Like Registers
* [https://adventofcode.com/2017/day/8](https://adventofcode.com/2017/day/8)

## Part One
You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:
```
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
```
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter ```<=``` (less than or equal to) or ```!=``` (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input? ```4416```

## Part Two
To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated). ```5199```

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
