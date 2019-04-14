# Day 6. Memory Reallocation
[https://adventofcode.com/2017/day/6](https://adventofcode.com/2017/day/6)

## Solution
```cpp
    #include <iostream>
    #include <sstream>
    #include <algorithm>
    #include <iterator>
    #include <vector>
    #include <unordered_set>
    #include "input.hpp"

    using namespace std;

    using Type = int;
    using Collection = vector< Type >;
    using Seen = unordered_set< string >;

    template< typename Type >
    class Solution {
    public:
        using Result = tuple< Type, Collection, Seen >;
        Result numCycles( Collection& A, Seen seen={} ){
            Type cnt{ 0 }, N = static_cast< Type >( A.size() );
            for( auto K{ 0 }; markSeen( A, seen ); ++cnt ){
                auto max = max_element( A.begin(), A.end() );
                K = *max, *max = 0;
                for( auto it{ max }; K--; ++it, it=(( it < A.end() )? it : A.begin() ), ++( *it ));
            }
            return{ cnt, A, seen };
        }
        bool markSeen( const Collection& A, Seen& seen ){
            ostringstream stream;
            copy( A.begin(), A.end(), ostream_iterator< Type >( stream, "," ));
            return seen.insert( stream.str() ).second;
        }
    };

    Collection readInput( const string& input, Collection A={} ){
        using itr = istream_iterator< Type >;
        istringstream stream{ input };
        copy( itr( stream ), itr(), back_inserter( A ));
        return A;
    }

    int main() {
        Solution< Type > solution;
        Type cnt{ 0 };
        Collection A = readInput( INPUT );
        Seen seen;
        tie( cnt, A, seen ) = solution.numCycles( A );
        cout << cnt << endl;
        tie( cnt, A, seen ) = solution.numCycles( A );
        cout << cnt << endl;
        return 0;
    }
```
