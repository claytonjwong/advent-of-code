# Day 5. A Maze of Twisty Trampolines, All Alike
[https://adventofcode.com/2017/day/5](https://adventofcode.com/2017/day/5)

## Solution
```cpp
    #include <iostream>
    #include <sstream>
    #include <string>
    #include <vector>
    #include <iterator>
    #include <algorithm>
    #include "input.hpp"

    using namespace std;

    using Iter = istream_iterator< int >;
    using Collection = vector< int >;

    enum class Part {
        One,
        Two,
    };

    class Solution {
    public:
        int numSteps( const string& input, Part part ){
            Collection A;
            istringstream stream{ input };
            copy( Iter( stream ), Iter(), back_inserter( A ));
            auto steps{ 0 };
            for( auto i{ 0 }; -1 < i && i < A.size(); ++steps )
                if( part == Part::Two && 2 < A[ i ] )
                    i += A[ i ]--;
                else
                    i += A[ i ]++;

            return steps;
        }
    };

    int main() {
        Solution solution;
        auto ans1 = solution.numSteps( INPUT, Part::One );
        cout << ans1 << endl;
        auto ans2 = solution.numSteps( INPUT, Part::Two );
        cout << ans2 << endl;
        return 0;
    }
```
