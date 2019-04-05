#include <iostream>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <unordered_map>
#include <regex>
#include "input.hpp"

using namespace std;

using Type = string;
using Collection = vector< Type >;
using Map = unordered_map< Type, Collection >;

template< typename Type >
class Solution {
public:
    Type findRoot( const string& input ){
        auto G = reverseGraph( createGraph( input ));
        for( auto pair: G ){
            auto P = pair.first;
            auto C = pair.second;
            if( C.empty() )
                return P;
        }
        return {};
    }
private:
    Map createGraph( const string& input, Map m={} ){
        regex adj{ "^(\\w+) \\(\\d+\\) -> (.*)$" },
              node{ "^(\\w+) \\(\\d+\\)$" };
        istringstream stream{ input };
        for( string line; getline( stream, line ); ){
            smatch group;
            if( regex_match( line, group, adj ) && group.size() == 3 ){
                auto P = string{ group[ 1 ] }, // (P)arent
                     A = string{ group[ 2 ] }; // (A)djacency list of children
                auto it = m.find( P );
                if( it == m.end() )
                    m[ P ] = {};
                transform( A.begin(), A.end(), A.begin(), []( auto ch ){ return( ch != ',' )? ch : ' '; });
                istringstream parser{ A };
                for( string C; parser >> C; m[ P ].push_back( C )); // (P)arent -> (C)hild relationship
            }
            else
            if( regex_match( line, group, node ) && group.size() == 2 ){
                auto C = string{ group[ 1 ] };
                auto it = m.find( C );
                if( it == m.end() )
                    m[ C ] = {};
            }
        }
        return m;
    }
    Map reverseGraph( Map&& m ){
        Map rev;
        for( auto& pair: m ){
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
    void printGraph( const Map& m ){
        for( auto& pair: m ){
            auto P = pair.first;  // (P)arent
            auto C = pair.second; // (C)hildren ( adjacency list )
            cout << P << " -> { ";
            copy( C.begin(), C.end(), ostream_iterator< string >( cout, ", " ) );
            cout << " }" << endl;
        };
    }
};

int main() {
    Solution< Type > solution;
    auto ans = solution.findRoot( INPUT );
    cout << ans << endl;
    return 0;
}
