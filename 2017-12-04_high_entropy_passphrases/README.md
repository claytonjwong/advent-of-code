# Day 4. High Entropy Passphrases
[https://adventofcode.com/2017/day/4](https://adventofcode.com/2017/day/4)

## Solution
```cpp
    #include <iostream>
    #include <sstream>
    #include <iterator>
    #include <algorithm>
    #include <vector>
    #include <unordered_set>
    #include "input.hpp"

    using namespace std;

    using Collection = vector< string >;
    using Set = unordered_set< string >;
    using Iter = istream_iterator< string >;

    bool isValid_part1( const string& words ){
        Collection A;
        istringstream stream{ words };
        copy( Iter( stream ), Iter(), back_inserter( A ));
        Set S{ A.begin(), A.end() };
        return A.size() == S.size();
    }

    bool isValid_part2( const string& words ){
        Collection A;
        istringstream stream{ words };
        copy( Iter( stream ), Iter(), back_inserter( A ));
        for( auto& word: A )
            sort( word.begin(), word.end() );
        Set S{ A.begin(), A.end() };
        return A.size() == S.size();
    }

    class Solution {
    public:
        template< typename IsValid >
        int numValid( const string& input, IsValid isValid, int cnt=0 ){
            istringstream stream{ input };
            for( string line; getline( stream, line ); )
                if( isValid( line ))
                    ++cnt;
            return cnt;
        }
    };

    int main() {
        Solution solution;
        auto ans1 = solution.numValid( INPUT, isValid_part1 );
        cout << ans1 << endl;
        auto ans2 = solution.numValid( INPUT, isValid_part2 );
        cout << ans2 << endl;
        return 0;
    }
```
