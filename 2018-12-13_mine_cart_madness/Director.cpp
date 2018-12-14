//
// Created by Clayton Wong on 2018-12-13.
//

#include "Director.hpp"
#include <iostream>


using namespace std;


const string Director::mapping_ = "|-\\/LSR"; // |-\/LSR

const vector< string > Director::stateMachine_ =
{
    //
    // tightly coupled to the director's direction values, each row represents the direction, each col represents the map char
    // at an arbitary map position, LSR represent the choices for intersections '+', we can choose Left, Straight, Right
    //
    // '.' represents invalid states
    // ( ex: [0][1] == '.' because we cannot be in the "up" direction while the map only allows left/right '-' )
    //

    //   |-\/LSR
    //  "U.LRLUR", // up == 0
    //  ".RDUURD", // right == 1
    //  "D.RLRDL", // down == 2
    //  ".LUDDLU"  // left == 3

        "0.31301",
        ".120012",
        "2.13123",
        ".302230"
};


Director::Direction Director::getNextDirection( const Director::Direction& dir, char mapped ) noexcept
{
    size_t row = static_cast< int >( dir ), col{ mapping_.find( mapped ) };
    assert( 0 <= row && row < numeric_limits<short>::max() && 0 <= col && col < numeric_limits<short>::max());
    char next{ stateMachine_[ row ][ col ] };
    auto nextDirection{ static_cast< Direction >( next - '0' ) };
    assert( 0 <= next - '0' && next - '0' <= 3);
    return nextDirection;
}


char Director::to_char( const Director::Direction& dir ) noexcept
{
    return ( dir == Direction::up )? UP : ( dir == Direction::right )? RIGHT : ( dir == Direction::down )? DOWN : LEFT;
}


ostream& operator<<( ostream& stream, const Director::Direction& dir ) noexcept
{
    stream << Director::to_char( dir );
    return stream;
}
