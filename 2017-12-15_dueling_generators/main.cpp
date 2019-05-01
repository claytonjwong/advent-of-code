#include <iostream>
#include <vector>

using namespace std;

template< typename Type >
class Solution {
public:
    using VT = vector< Type >;
    Type generate( Type A, Type B, Type N, Type modA=0, Type modB=0, Type ans=0 ){
        const Type P{ 2147483647 }, mask{ 0xFFFF };
        while( N-- ){
            do A = A * 16807 % P; while( A & modA );
            do B = B * 48271 % P; while( B & modB );
            ans += (( A & mask ) == ( B & mask ));
        }
        return ans;
    }
};

int main() {
    using Type = unsigned long long;
    using Solution = Solution< Type >;
    Solution solution;
    constexpr Type A{ 618 }, B{ 814 };
    auto ans1 = solution.generate( A, B, 40 * 1e6 ),
         ans2 = solution.generate( A, B,  5 * 1e6, 3, 7 );
    cout << "Part 1: " << ans1 << endl
         << "Part 2: " << ans2 << endl;
    return 0;
}