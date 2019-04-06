#include <iostream>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <regex>
#include "input.hpp"

using namespace std;

using Type = string;
using Collection = vector< Type >;
using Graph = unordered_map< Type, Collection >;
using Weight = unordered_map< Type, int >;

template< typename Type >
class Solution {
public:
    Type findRoot( const string& input ){ // the root is the reversed adjacency list's single node without children
        auto G = createGraph( input ).first;
        auto R = reverseGraph( G );
        return findRoot( R );
    }
    Type findRoot( const Graph& G ){ // the root is the reversed adjacency list's single node without children
        for( auto pair: G ){
            auto P = pair.first;  // (P)arent
            auto C = pair.second; // (C)hildren ( adjacency list )
            if( C.empty() )
                return P;
        }
        return {};
    }
    int findBalance( const string& input, Weight memo={}, int delta=0, string target={} ){
        auto[ G,W ] = createGraph( input );
        auto R = reverseGraph( G );
        auto root = findRoot( R );
        findWeight( G, W, root, memo );
        go( G, W, root, memo, delta, target );
        return W[ target ] - delta;
    }
private:
    using GraphWeight = pair< Graph, Weight >;
    GraphWeight createGraph( const string& input, Graph G={}, Weight W={} ){
        regex adj{  "^(\\w+) \\((\\d+)\\) -> (.*)$" },
              node{ "^(\\w+) \\((\\d+)\\)$" };
        istringstream stream{ input };
        for( string line; getline( stream, line ); ){
            smatch group;
            if( regex_match( line, group, adj ) && group.size() == 4 ){
                auto P = string{ group[ 1 ] }; // (P)arent
                {
                    if( G.find( P ) == G.end() )
                        G[ P ] = {};
                }
                auto V = group[ 2 ];           // (V)alue
                {
                    auto value{ 0 };
                    istringstream parser{ V };
                    parser >> value;
                    W[ P ] = value;
                }
                auto A = string{ group[ 3 ] }; // (A)djacency list of children
                {
                    transform( A.begin(), A.end(), A.begin(), []( auto ch ){ return( ch != ',' )? ch : ' '; });
                    istringstream parser{ A };
                    for( string C; parser >> C; G[ P ].push_back( C )); // (P)arent -> (C)hild relationship
                }
            }
            else
            if( regex_match( line, group, node ) && group.size() == 3 ){
                auto C = string{ group[ 1 ] }; // (C)hild
                {
                    if( G.find( C ) == G.end() )
                        G[ C ] = {};
                }
                auto V = group[ 2 ];           // (V)alue
                {
                    auto value{ 0 };
                    istringstream parser{ V };
                    parser >> value;
                    W[ C ] = value;
                }
            }
        }
        return{ G,W };
    }
    Graph reverseGraph( const Graph& G ){
        Graph rev;
        for( auto& pair: G ){
            auto P = pair.first;  // (P)arent
            auto C = pair.second; // (C)hildren ( adjacency list )
            if( C.empty() )
                continue;
            for( auto& child: C ){
                auto it = rev.find( P );
                if( it == rev.end() )
                    rev[ P ] = {};
                it = rev.find( child );
                if( it == rev.end() )
                    rev[ child ] = {};
                rev[ child ].push_back( P );
            }
        }
        return rev;
    }
    void printGraph( const Graph& G ){
        for( auto& pair: G ){
            auto P = pair.first;  // (P)arent
            auto C = pair.second; // (C)hildren ( adjacency list )
            cout << P << " -> { ";
            copy( C.begin(), C.end(), ostream_iterator< string >( cout, ", " ) );
            cout << " }" << endl;
        };
    }
    int findWeight( Graph& G, Weight& W, Type& P, Weight& memo ){
        if( memo.find( P ) != memo.end() )
            return memo[ P ];
        auto sum = W[ P ];
        for( auto& C: G[ P ] )
            sum += findWeight( G, W, C, memo );
        return memo[ P ] = sum;
    }
    void go( Graph& G, Weight& W, Type& P, Weight& memo, int& delta, string& target ){
        unordered_map< int, Type > weightName;
        unordered_map< int, int > weightCnt;
        for( auto& C: G[ P ] ){
            auto total = memo[ C ];
            weightName[ total ] = C;
            ++weightCnt[ total ];
        }
        if( weightName.size() == 2 && weightCnt.size() == 2 ){
            auto single{ 0 }, multi{ 0 };
            for( auto& pair: weightName ){
                auto weight = pair.first;
                auto name = pair.second;
                if( weightCnt[ weight ] == 1 )
                    single = weight;
                else
                    multi = weight;
            }
            delta = single - multi;
            target = weightName[ single ];
            go( G, W, target, memo, delta, target );
        }
    }
};

int main() {
    Solution< Type > solution;
    auto ans1 = solution.findRoot( INPUT );
    cout << ans1 << endl;
    auto ans2 = solution.findBalance( INPUT );
    cout << ans2 << endl;
    return 0;
}
