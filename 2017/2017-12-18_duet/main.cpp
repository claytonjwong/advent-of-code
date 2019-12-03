#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include "input.hpp"

using namespace std;

template< typename Type >
class Solution {
public:
    explicit Solution( const string& input ) : commands_{}, symbols_{}, last_{ 0 } {
        istringstream stream{ input };
        for( string line; getline( stream, line ); commands_.emplace_back( line ) );
    }
    Type process(){
        string cmd, first, second;
        for( auto i{ 0 }; i < commands_.size(); ){
            auto line = commands_[ i ];
            istringstream stream{ line };
            stream >> cmd >> first >> second;
            auto T = first[ 0 ]; // (T)arget symbol
            if( cmd == "snd" )
                last_ = symbols_[ T ];
            else if( cmd == "rcv" && symbols_[ T ] )
                return last_;
            else if( cmd == "set" ) symbols_[ T ]  = value( second );
            else if( cmd == "add" ) symbols_[ T ] += value( second );
            else if( cmd == "mul" ) symbols_[ T ] *= value( second );
            else if( cmd == "mod" ) symbols_[ T ] %= value( second );
            // next command: either jump or increment by one
            if( cmd == "jgz" && symbols_[ T ] )
                i += value( second );
            else
                ++i;
        }
    }
private:
    using Command = string;
    using Commands = vector< Command >;
    Commands commands_;
    using SymbolTable = unordered_map< char,Type >;
    SymbolTable symbols_;
    Type last_;
    Type value( const string& s ){
        auto ch = s[ 0 ];
        if( isalpha( ch ) )
            return symbols_[ ch ];
        istringstream parser{ s };
        Type num{ 0 };
        parser >> num;
        return num;
    }
};

int main() {
    Solution< long long >solution( Part1::Input );
    auto ans = solution.process();
    cout << ans << endl;
    return 0;
}
