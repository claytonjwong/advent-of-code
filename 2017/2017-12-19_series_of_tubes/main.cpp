#include <iostream>
#include <sstream>
#include <vector>
#include <cassert>
#include "input.hpp"

using namespace std;

class Solution {
public:
    using Input = vector< string >;
    enum class Dir { Up, Right, Down, Left };
    using Answer = pair< string,int >;
    Answer traverse( const Input& A, Dir dir=Dir::Down, string letters={}, int steps=1 ){
        auto M = static_cast< int >( A.size() ),
             N = static_cast< int >( A[ 0 ].size() );
        auto i = 0, j = static_cast< int >( A[ i ].find( '|' ) );
        for( auto next = peek( A, i, j, dir ); isValid( next ); ++steps, next = peek( A, i, j, dir ) ){
            auto c = step( A, i, j, dir );
            if( isalpha( c ) )
                letters.push_back( c );
            if( c == '+' )
                turn( A, i, j, dir );
        }
        return{ letters,steps };
    }
private:
    bool isValid( char next ){
        return next == '|' || next == '-' || next == '+' || isalpha( next );
    }
    char peek( const Input& A, int i, int j, Dir dir ){ // peek is idempotent: i,j are copies
        return step( A, i, j, dir );
    }
    char step( const Input& A, int& i, int& j, Dir dir ){
        switch( dir ){
            case Dir::Up:    --i; break;
            case Dir::Right: ++j; break;
            case Dir::Down:  ++i; break;
            case Dir::Left:  --j; break;
        }
        return A[ i ][ j ];
    }
    void turn( const Input& A, int i, int j, Dir& dir ){
        if( dir == Dir::Up || dir == Dir::Down ){
            auto L = peek( A, i, j, Dir::Left ),
                 R = peek( A, i, j, Dir::Right );
            if( isValid( L ) ) dir = Dir::Left;
            if( isValid( R ) ) dir = Dir::Right;
        } else {
            auto U = peek( A, i, j, Dir::Up ),
                 D = peek( A, i, j, Dir::Down );
            if( isValid( U ) ) dir = Dir::Up;
            if( isValid( D ) ) dir = Dir::Down;
        }
    }
};

int main() {
    Solution::Input A;
    istringstream stream{ INPUT };
    for( string line; getline( stream, line ); A.push_back( line ) );
    auto[ letters, steps ] = Solution().traverse( A );
    cout << "Part 1: " << letters << endl
         << "Part 2: " << steps << endl;
    return 0;
}
