# Day 3. Spiral Memory
[https://adventofcode.com/2017/day/3](https://adventofcode.com/2017/day/3)

## Part 1
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:
```
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
```
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

* Data from square 1 is carried 0 steps, since it's at the access port.
* Data from square 12 is carried 3 steps, such as: down, left, left.
* Data from square 23 is carried only 2 steps: up twice.
* Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified
in your puzzle input all the way to the access port? ```419```

## Part 2
As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

* Square 1 starts with the value 1.
* Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
* Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
* Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
* Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:
```
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
```

What is the first value written that is larger than your puzzle input? ```295229```

Your puzzle input is still 289326.

## Solution

```cpp
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
        auto ans2 = solution.stressTest( N );
        cout << ans2 << endl;
        return 0;
    }
```
