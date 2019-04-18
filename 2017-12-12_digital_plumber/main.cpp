#include <iostream>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <unordered_set>
#include "input.hpp"

using namespace std;

class Solution {
public:
    using Result = pair< int, int >;
    Result groupSize( const string& input, int target ){
        DisjointSet ds{ input };
        return{ ds.Size( target ), ds.Size() };
    }
private:
    class DisjointSet {
    public:
        using Lines = vector< string >;
        using Iter = istream_iterator< string >;
        explicit DisjointSet( const string& input, Lines lines={} ){
            istringstream stream{ input };
            for( string line; getline( stream, line ); lines.push_back( line ));
            A = Collection( lines.size() );
            generate( A.begin(), A.end(), [i=0]() mutable { return i++; });
            for( const auto& line: lines ){
                auto parent{ 0 };
                string delim;
                istringstream parser{ line };
                parser >> parent >> delim;
                for( string word; parser >> word; ){
                    if( word.back() == ',' )
                        word.pop_back();
                    auto child{ 0 };
                    istringstream parser{ word };
                    parser >> child;
                    Union( parent, child );
                }
            }
        }
        int Find( int x ){
            if( A[ x ] == x )
                return A[ x ];
            return A[ x ] = Find( A[ x ] );
        }
        void Union( int a, int b ){
            auto pa = Find( a ),
                 pb = Find( b );
            A[ pa ] = pb;
        }
        int Size( int T ){
            auto p = Find( T );
            return count_if( A.begin(), A.end(), [&]( auto x ){ return p == Find( x ); });
        }
        int Size() {
            using Unique = unordered_set< int >;
            Unique U;
            for( auto x: A )
                U.insert( Find( x ) );
            return U.size();
        }

    private:
        using Collection = vector< int >;
        Collection A;
    };
};

int main() {
    Solution solution;
    auto[ ans1, ans2 ] = solution.groupSize( Large::Input, 0 );
    cout << "Part 1: " << ans1 << endl
         << "Part 2: " << ans2 << endl;
    return 0;
}
