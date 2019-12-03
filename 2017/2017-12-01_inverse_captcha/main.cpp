#include <iostream>
#include <string>
#include "input.hpp"

using namespace std;

using Type = int;

Type next_part1( const Type i, const Type N ){
    return( i + 1 );
}

Type next_part2( const Type i, const Type N ){
    return( i + ( N / 2 )) % N;
}

template< typename Type >
class Solution {
public:
    using Collection = string;
    template< typename Next >
    Type inverseCaptcha( const Collection& A, Next next, Type ans=0 ) {
        Type N = static_cast< Type >( A.size() );
        for( Type i{ 0 }, j{ next(i,N) }; i < N; ++i, j=( next(i,N) ))
            if( A[ i ] == A[ j ] )
                ans += A[ i ] - '0';
        return ans;
    }
};

int main() {
    Solution< Type > solution;
    auto ans1 = solution.inverseCaptcha( INPUT, next_part1 );
    cout << "answer 1: " << ans1 << endl;
    auto ans2 = solution.inverseCaptcha( INPUT, next_part2 );
    cout << "answer 2: " << ans2 << endl;
    return 0;
}
