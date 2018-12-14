//
// Created by Clayton Wong on 2018-12-13.
//

#pragma once


#include <iostream>


struct Position
{
    size_t x{ 0 }, y{ 0 };

    bool operator==( const Position& rhs ) const noexcept;
};

std::ostream& operator<<( std::ostream& stream, const Position& position ) noexcept;
