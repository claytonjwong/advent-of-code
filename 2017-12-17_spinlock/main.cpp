#include <iostream>
#include <list>

using namespace std;

class Solution {
public:
    using Collection = list< int >;
    int insert( int N, int steps, int target, Collection L={ 0 } ){
        auto it = L.begin();                                            // current position is tracked by the (L)ist (it)erator
        for( auto i{ 1 }; i <= N; it = L.insert( next( it ), i++ ) )    // insert i after position K-steps away
            for( auto K = steps % L.size(); 0 < K; --K )                // move (it)erator forward K-steps
                it = ( next( it ) != L.end() )? next( it ) : L.begin();
        if( N != target )
            it = find( L.begin(), L.end(), target );
        return( next( it ) != L.end() )? *next( it ) : *L.begin();
    }
};

int main() {
    auto N{ 367 };
    Solution solution;
    auto ans1 = solution.insert(     2017, N, 2017 ),
         ans2 = solution.insert( 50 * 1e6, N,    0 );
    assert( ans1 == 1487 );
    assert( ans2 == 25674054 );
    return 0;
}