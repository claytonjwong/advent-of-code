#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include "input.hpp"

using namespace std;

template< typename Type >
class Partical {
public:
    using XYZ_t = vector< Type >;
    XYZ_t p{ 0,0,0 },
          v{ 0,0,0 },
          a{ 0,0,0 };
    void tick() {
        for( auto i{ 0 }; i < 3; ++i ){
            v[ i ] += a[ i ];
            p[ i ] += v[ i ];
        }
    }
    bool operator<( const Partical& rhs ) const {
        Type first{ 0 }, second{ 0 };
        for( auto val: p )
            first += abs( val );
        for( auto val: rhs.p )
            second += abs( val );
        return first < second;
    }
    string pos() const {
        ostringstream os;
        copy( p.begin(), p.end(), ostream_iterator< Type >( os, "," ) );
        return os.str();
    }
};

template< typename Type >
class Solution {
public:
    using Partical_t = Partical< Type >;
    using XYZ_t = typename Partical< Type >::XYZ_t;
    using Swarm = vector< Partical_t >;
    using Unique = unordered_set< size_t >;
    Swarm readInput( const string& input, string line={}, Swarm swarm={} ){
        istringstream stream{ input };
        for( Type i{ 0 }; getline( stream, line ); ++i ){
            istringstream parser{ line };
            swarm.emplace_back( readPartical( parser ) );
        }
        return swarm;
    }
    Partical_t readPartical( istringstream& stream, Partical_t partical={} ){
        partical.p = readXYZ( stream );
        partical.v = readXYZ( stream );
        partical.a = readXYZ( stream );
        return partical;
    }
    XYZ_t readXYZ( istringstream& stream, XYZ_t xyz=XYZ_t( 3 ) ){
        for( auto i{ 0 }; i < 3; ++i )
            xyz[ i ] = readValue( stream );
        return xyz;
    }
    Type readValue( istringstream& stream, Type val={} ){
        next( stream );
        stream >> val;
        return val;
    }
    void next( istringstream& stream ){
        for( char _={}; ! isdigit( stream.peek() ) && stream.peek() != '-'; stream >> _ );
    }
    using Result = pair< Type, size_t >;
    Result closest( Swarm& swarm, Unique destroyed={} ){
        for( auto ticks{ 0 }; ticks < 1e3; ++ticks ){
            for( auto i{ 0 }; i < swarm.size(); ++i )
                if( destroyed.find( i ) == destroyed.end() )
                    swarm[ i ].tick();
            markCollisions( swarm, destroyed );
        }
        return{ distance( swarm.begin(), min_element( swarm.begin(), swarm.end() ) ), swarm.size() - destroyed.size() };
    }
    using Collisions = unordered_map< string, Unique >;
    void markCollisions( const Swarm& swarm, Unique& destroyed, Collisions collisions={} ){
        for( auto i{ 0 }; i < swarm.size(); ++i ){
            if( destroyed.find( i ) != destroyed.end() )
                continue;
            auto pos = swarm[ i ].pos();
            collisions[ pos ].insert( i );
        }
        for( auto& pair: collisions ){
            auto collided = pair.second;
            if( 1 < collided.size() )
                for( auto i: collided )
                    destroyed.insert( i );
        }
    }
};

int main() {
    using Type = long long;
    Solution< Type > solution;
    auto swarm = solution.readInput( Large::INPUT );
    auto[ closest, left ] = solution.closest( swarm );
    cout << "Part 1: " << closest << endl
         << "Part 2: " << left << endl;
    assert( closest == 119 );
    assert(    left == 471);
    return 0;
}
