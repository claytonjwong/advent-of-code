#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <unordered_set>
#include <iomanip>
#include "input.hpp"

using namespace std;

class Solution {
public:
    void dance( string& S, const string& input ){
        istringstream stream{ input };
        for( string line; getline( stream, line, ',' ); ){
            istringstream parser{ line };
            char c{ 0 }; parser >> c;
            if( c == 's' ){
                auto N{ 0 }; parser >> N;
                rotate( S.rbegin(), S.rbegin() + N, S.rend() );
            }
            if( c == 'x' ){
                auto i{ 0 }, j{ 0 }; char _{ 0 }; parser >> i >> _ >> j;
                swap( S[ i ], S[ j ] );
            }
            if( c == 'p' ){
                char A{ 0 }, B{ 0 }, _{ 0 }; parser >> A >> _ >> B;
                auto i = find( S.begin(), S.end(), A ),
                     j = find( S.begin(), S.end(), B );
                iter_swap( i, j );
            }
        }
    }
};

int main() {
#ifdef DEBUG
    string S{ "abcde" };
#else
    string S{ "abcdefghijklmnop" };
#endif

    Solution solution;
    solution.dance( S, INPUT );

#ifdef DEBUG
    assert( S == "baedc" );
#else
    assert( S == "lbdiomkhgcjanefp" ); // answer for part 1
    using Collection = vector< string >;
    using Unique = unordered_set< string >;
    Collection A;
    for( Unique U; U.insert( S ).second; A.push_back( S ), solution.dance( S, INPUT ) ); // pisano period is |A|
    auto X = static_cast< int >( 1e9-1 ) % A.size(); // one-billion minus one since one dance was performed for part 1 already
    assert( A[ X ] == "ejkflpgnamhdcboi" ); // answer for part 2
#endif

    return 0;
}