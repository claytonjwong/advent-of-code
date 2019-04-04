#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <string>
#include <unordered_map>

using namespace std;

template< typename Type >
class Solution {
public:
    using Steps = vector< Type >;
    using Cell = pair< Type, Type >;
    struct Hash{ size_t operator()( const Cell& c ) const { return 10001 * c.first + c.second; }};
    using Map = unordered_map< Cell, Type, Hash >;
    Type numSteps( int N, Steps steps={} ){
        init( N );
        for( auto i{ 1 }, sum{ 0 }; sum <= N; sum+=( 2*i ), ++i )
            generate_n( back_inserter( steps ), 2, [&](){ return i; });
        for( auto step: steps ){
            if( N == 0 )
                break;
            step = min( step, N );
            walk( step );
            N -= step;
        }
        return abs( x ) + abs( y );
    }
    Type stressTest( int N, Steps steps={} ){
        auto T{ N };
        init( N );
        for( auto i{ 1 }, sum{ 0 }; sum <= T; sum+=( 2*i ), ++i )
            generate_n( back_inserter( steps ), 2, [&](){ return i; });
        Map map{{ make_pair( x,y ), 1 }};
        for( auto step: steps ){
            if( T < map[{ x,y }] )
                break;
            walk( step, T, map );
        }
        return map[{ x,y }];
    }
private:
    int x{ 0 },
        y{ 0 },
        d{ 3 }; // (d)irection index
    void init( int& N ) {
        --N; // convert one-based indexing to zero-based indexing
        x = 0;
        y = 0;
        d = 3;
    }
    char nextDir() {
        static const string D{ "RULD" }; // (D)irections: right, up, left, down
        d = ( d+1 < D.size() )? d+1 : 0;
        return D[ d ];
    }
    void walk( int step ){
        auto dir = nextDir();
        switch( dir ){
            case 'R': x += step; break;
            case 'U': y -= step; break;
            case 'L': x -= step; break;
            case 'D': y += step; break;
        }
    }
    void walk( int step, int T, Map& m ){
        auto dir = nextDir();
        if( dir == 'R' )
            for( int begin{ x }, end{ begin + step }; x < end && !( T < m[{ x,y }] ); ++x, m[{ x, y }] = sumAdj( m ));
        else
        if( dir == 'U' )
            for( int begin{ y }, end{ begin - step }; y > end && !( T < m[{ x,y }] ); --y, m[{ x,y }] = sumAdj( m ));
        else
        if( dir == 'L' )
            for( int begin{ x }, end{ begin - step }; x > end && !( T < m[{ x,y }] ); --x, m[{ x,y }] = sumAdj( m ));
        else
        if( dir == 'D' )
            for( int begin{ y }, end{ begin + step }; y < end && !( T < m[{ x,y }] ); ++y, m[{ x,y }] = sumAdj( m ));
    }
    Type sumAdj( Map& m ){
        return m[{ x  , y-1 }]
             + m[{ x+1, y-1 }]
             + m[{ x+1, y   }]
             + m[{ x+1, y+1 }]
             + m[{ x  , y+1 }]
             + m[{ x-1, y-1 }]
             + m[{ x-1, y   }]
             + m[{ x-1, y+1 }];
    }
};

int main() {
    using Type = int;
    Solution< Type > solution;
    auto N{ 289326 };
    auto ans1 = solution.numSteps( N );
    cout << ans1 << endl;
    auto ans2 = solution.stressTest( 289326 );
    cout << ans2 << endl;
    return 0;
}
