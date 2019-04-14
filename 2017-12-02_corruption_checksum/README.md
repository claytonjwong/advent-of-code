# Day 2. Corruption Checksum
[https://adventofcode.com/2017/day/2](https://adventofcode.com/2017/day/2)

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
