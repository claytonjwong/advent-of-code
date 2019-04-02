# Day 2. Corruption Checksum
[https://adventofcode.com/2017/day/2](https://adventofcode.com/2017/day/2)

## Part 1
As you walk through the door, a glowing humanoid shape yells in your direction. "You there!
Your state appears to be idle. Come help us repair the corruption in this spreadsheet
if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process
is on the right track, they need you to calculate the spreadsheet's checksum. For each row,
determine the difference between the largest value and the smallest value; the checksum
is the sum of all of these differences.

For example, given the following spreadsheet:
```
5 1 9 5
7 5 3
2 4 6 8
```
* The first row's largest and smallest values are 9 and 1, and their difference is 8.
* The second row's largest and smallest values are 7 and 3, and their difference is 4.
* The third row's difference is 6.

In this example, the spreadsheet's checksum would be ```8 + 4 + 6 = 18```

What is the checksum for the spreadsheet in your puzzle input? ```44887```

## Part 2
"Great work; looks like we're on the right track after all. Here's a star for your effort."
However, the program seems a little worried. Can programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some information
about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped
for that kind of calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other,
that is, where the result of the division operation is a whole number. They would like you
to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:
```
5 9 2 8
9 4 7 3
3 8 6 5
```
* In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
* In the second row, the two numbers are 9 and 3; the result is 3.
* In the third row, the result is 2.
* In this example, the sum of the results would be ```4 + 3 + 2 = 9```.

What is the sum of each row's result in your puzzle input? ```242```

## Solution

```cpp
    #include <iostream>
    #include <sstream>
    #include <vector>
    #include <numeric>
    #include "input.hpp"

    using namespace std;

    using Type = int;
    using VT = vector< Type >;
    using VVT = vector< VT >;

    Type checksum_part1( const VT& A ){
        auto[ lo, hi ] = minmax_element( A.begin(), A.end() );
        auto delta = abs( *lo - *hi );
        return delta;
    }

    Type checksum_part2( const VT& A ){
        auto N = static_cast< Type >( A.size() );
        for( auto i{ 0 }; i+1 < N; ++i )
            for( auto j{ i+1 }; j < N; ++j )
                if( A[ i ] % A[ j ] == 0 )
                    return A[ i ] / A[ j ];
                else
                if( A[ j ] % A[ i ] == 0 )
                    return A[ j ] / A[ i ];
        return 0;
    }

    template< typename Type >
    class Solution {
    public:
        template< typename Checksum >
        Type corruptChecksum( const string& input, Checksum checksum, VT R={} ){
            auto A = readInput( input );
            for( auto& row: A ){
                auto res = checksum( row );
                R.push_back( res );
            }
            return accumulate( R.begin(), R.end(), 0 );
        }
    private:
        VVT readInput( const string& input, VVT res={} ){
            istringstream stream{ input };
            for( string line; getline( stream, line ); ){
                res.push_back( {} );
                istringstream parser{ line };
                for( Type x{ 0 }; parser >> x; res.back().push_back( x ));
            }
            return res;
        }
    };

    int main() {
        Solution< Type > solution;
        auto ans1 = solution.corruptChecksum( INPUT, checksum_part1 );
        cout << ans1 << endl;
        auto ans2 = solution.corruptChecksum( INPUT, checksum_part2 );
        cout << ans2 << endl;
        return 0;
    }
```
