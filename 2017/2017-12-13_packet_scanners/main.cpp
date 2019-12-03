#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include "input.hpp"

using namespace std;

namespace Foolish {
    class Solution {
    public:
        using Result = pair< int,int >;
        Result travel( const string& input, Result res={} ){
            auto firewall = gen( input );
            res.first = travel1( firewall );
            res.second = travel2( firewall );
            return res;
        }
    private:
        class Scanner {
        public:
            Scanner( int N ) : cur{ 0 }, next{ 1 }, N{ N } {}
            bool operator[]( int i ){
                return cur == i;
            }
            int size() const {
                return N;
            }
            void step() {
                cur += next;
                if( cur == -1 ){
                    cur = 1;
                    next = 1;
                }
                if( cur == N ){
                    cur = N - 2;
                    next = -1;
                }
            }
        private:
            int cur, next, N;
        };
        using Firewall = map< int,Scanner >;
        Firewall gen( const string& input, Firewall F={}, int depth=0, int range=0 ){
            istringstream stream{ input };
            for( string line; getline( stream, line ); ){
                transform( line.begin(), line.end(), line.begin(), []( auto c ){ return( c == ':' )? ' ' : c; });
                istringstream parser{ line };
                parser >> depth >> range;
                F.insert({ depth, Scanner( range ) });
            }
            return F;
        }
        int travel1( Firewall F, int cost=0 ){
            auto max = depth( F );
            for( auto depth{ -1 }; depth < max; tick( F )){
                auto it = F.find( ++depth );
                if( it != F.end() ){
                    auto scanner = it->second;
                    if( scanner[ 0 ] )
                        cost += depth * scanner.size(); // cost is depth * scanner range
                }
            }
            return cost;
        }
        int travel2( Firewall firewall ){
            for( auto delay{ 0 };; ++delay ){
                auto F{ firewall };
                for( int i{ 0 }; i < delay; ++i, tick( F ));
                auto max = depth( F );
                auto ok{ true };
                for( auto depth{ -1 }; depth < max; tick( F )){
                    auto it = F.find( ++depth );
                    if( it != F.end() ){
                        auto scanner = it->second;
                        if( scanner[ 0 ] ){
                            ok = false;
                            break;
                        }

                    }
                }
                if( ok )
                    return delay;
            }
            return -1;
        }
        void tick( Firewall& F ){
            for( auto& pair: F )
                pair.second.step();
        }
        int depth( const Firewall& F ){
            using Pair = pair< int,Scanner >;
            auto it = max_element( F.begin(), F.end(), []( const Pair& lhs, const Pair& rhs ){ return lhs.first < rhs.first; });
            return( it != F.end() )? it->first : 0;
        }
    };
}
namespace Wise {
    class Solution {
    public:
        using Scanner = pair< int,int >;
        using Scanners = vector< Scanner >;
        using Result = pair< int,int >;
        Result travel( string input, Scanners A={}, int depth=0, int range=0, int severity=0 ){
            istringstream stream{ input };
            for( string _={}; stream >> depth >> _ >> range; A.push_back({ depth,range }) );
            for( auto pair: A ){ // for each (s)canner
                auto[ depth, range ] = pair;
                auto T = 2 * ( range - 1 ); // (T)arget
                if( depth % T == 0 )
                    severity += depth * range;
            }
            auto delay{ 0 };
            for(; any_of( A.begin(), A.end(), [=]( auto& pair ){
                        auto[ depth, range ] = pair;
                        auto T = 2 * ( range - 1 ); // (T)arget
                        return T == 0 || ( depth + delay ) % T == 0; }); ++delay );
            return{ severity, delay };
        }
    };
}

int main() {
    Wise::Solution solution;
    auto[ ans1, ans2 ] = solution.travel( Large::Input );
    cout << "Part 1: " << ans1 << endl
         << "Part 2: " << ans2 << endl;
    return 0;
}
