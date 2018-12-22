//
// Created by Clayton Wong on 2018-12-21.
//

#include <iostream>
#include <vector>


using namespace std;
using L = unsigned long long;
using VL = vector< L >;
using VVL = vector< VL >;


int main()
{
    long long depth{ 4002 }, M{ 5 }, N{ 746 }, MOD{ 20183 }; // input values

    VVL GI = VVL( M+1, VL( N+1, 0 ) ), EL{ GI }; // (G)eological (I)ndexes and (E)rosion (L)evels
    for( int x{ 0 }; x <=M; ++x ) for( int y{ 0 }; y <= N; EL[ x ][ y ] = ( GI[ x ][ y ] + depth ) % MOD, ++y )
        if( x == 0 && y == 0 )
            GI[ x ][ y ] = 0;
        else if( x == 0 )
            GI[ x ][ y ] = y * 48271;
        else if( y == 0 )
            GI[ x ][ y ] = x * 16807;
        else
            GI[ x ][ y ] = EL[ x-1 ][ y ] * EL[ x ][ y-1 ];

    size_t sum{ 0 }; for( int x{ 0 }; x <= M; ++x ) for( int y{ 0 }; y <= N; ++y ) sum += ( EL[ x ][ y ] % 3 );
    cout << "answer part 1: " << sum << endl;

    return 0;
}