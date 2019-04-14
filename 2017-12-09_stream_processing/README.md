# Day 9: Stream Processing

* [https://adventofcode.com/2017/day/9](https://adventofcode.com/2017/day/9)

## Part One
What is the total score for all groups in your input? ```10800```

## Part Two
How many non-canceled characters are within the garbage in your puzzle input? ```4522```

## Solution
```cpp
#include <iostream>
#include <sstream>
#include <string>
#include "input.hpp"

using namespace std;

class Solution {
public:
    using Result = pair< int,int >; // < part 1, part 2 >
    Result process( const string& input ){
        auto[ str, cnt ] = reduce( input );
        return{ go( str ), cnt };
    }
    using StringCount = pair< string,int >; // < reduced string to {}'s, garbage count >
    StringCount reduce( const string& input, string str={}, int cnt=0 ){
        auto state = State::Ready;
        istringstream stream{ input };
        for( char c{ 0 }; stream >> c; ){
            if( c == '!' )
                stream >> c; // ignore next (c)haracter
            else
            if( State::Ready == state && ( c == '{' || c == '}' ))
                str.push_back( c );
            else
            if( State::Ready == state && c == '<' )
                state = State::Garbage;
            else
            if( State::Garbage == state && c == '>' )
                state = State::Ready;
            else
            if( State::Garbage == state && c != '>' )
                ++cnt;
        }
        return{ str, cnt };
    }
    int go( const string& S, int i=0, int d=0 ){ // (S)tring of {}'s, (i)ndex of S, and (d)epth
        if( i == S.size() )
            return 0;
        return( S[ i ] == '{' )? go( S, i+1, d+1 ) : d + go(S, i+1, d-1 );
    }
private:
    enum class State {
        Ready,
        Garbage,
    };
};

int main() {
    Solution solution;
    auto[ ans1, ans2 ] = solution.process( INPUT );
    cout << "part 1: " << ans1 << endl;
    cout << "part 2: " << ans2 << endl;
    return 0;
}
```
