#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include "input.hpp"

using namespace std;

class Solution {
public:
    using Collection = vector< int >;
    int hash( const int N, string input, int pos=0, int len=0, int skip=0 ){
        Collection cur( N ), L; // (cur)rent list, (L)engths
        generate( cur.begin(), cur.end(), [ i=0 ]() mutable { return i++; });
        transform( input.begin(), input.end(), input.begin(), []( auto c ){ return( c == ',' )? ' ' : c; });
        istringstream stream{ input };
        using Iter = istream_iterator< int >;
        copy( Iter( stream ), Iter(), back_inserter( L ));
        for( auto len: L )
            knot( cur, pos, len, skip );
        return cur[ 0 ] * cur[ 1 ];
    }
    string hash64( const int N, const string& input, int pos=0, unsigned char len=0, int skip=0, string ans={} ){
        Collection cur( N ), L; // (cur)rent list, (L)engths
        generate( cur.begin(), cur.end(), [i=0]() mutable { return i++; });
        istringstream stream{ input };
        using Iter = istream_iterator< unsigned char >;
        copy( Iter( stream ), Iter(), back_inserter( L ));
        L.insert( L.end(), { 17, 31, 73, 47, 23 });
        for( auto round{ 64 }; round--; )
            for( auto len: L )
                knot( cur, pos, len, skip );
        for( auto chunk{ 0 }; chunk < 16; ++chunk ){
            auto begin = chunk * 16;
            auto x = cur[ begin ];
            for( auto i{ begin+1 }; i < begin + 16; x ^= cur[ i++ ] );
            ostringstream stream;
            stream << setw( 2 ) << setfill( '0' ) << hex << x;
            ans.append( stream.str() );
        }
        return ans;
    }
private:
    void knot( Collection& cur, int& pos, int len, int& skip ){
        const auto N = cur.size();
        auto next{ cur };
        for( auto i{ 0 }; i < len; ++i ){
            auto p = ( pos + i ) % N,
                 q = ( pos + len - i - 1 ) % N;
            if( p < 0 ) p += len;
            if( q < 0 ) q += len;
            next[ q ] = cur[ p ];
        }
        swap( cur, next );
        pos += ( len + skip ) % N;
        ++skip;
    }
};

int main() {
    Solution solution;
    auto N{ 256 };
    auto ans1 = solution.hash( N, INPUT );
    auto ans2 = solution.hash64( N, INPUT );
    cout << "part 1: " << ans1 << endl;
    cout << "part 2: " << ans2 << endl;
    return 0;
}
