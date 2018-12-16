//
// Created by Clayton Wong on 2018-12-15.
//

#include "input.hpp"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>


using namespace std;


struct Coordinate{ int row{ 0 }, col{ 0 }; };
struct Cell{ int id{ 0 }, distance{ numeric_limits< int >::max() }; };


using VC = vector< Coordinate >;
using VI = vector< int >;
using PII = pair< int, int >;
using GridLines = vector< Cell >;
using Grid = vector< GridLines >;
using Counter = unordered_map< int, int >;
using Border = unordered_set< int >;


class Solution
{
public:

    PII getMaxArea( const string& input, int id=0, int row=0, int col=0, PII ans={},
        VI rows={}, VI cols={}, VC coords={}, Counter counter={}, Border border={ 0 } ) const noexcept
    {
        string in{ input }; for( char& c: in ) if( c == 44 ) c = 32; // transform commas to spaces
        istringstream inputStream{ in };
        for( string line; getline( inputStream, line ); )
        {
            istringstream lineStream{ line }; lineStream >> col >> row;
            coords.emplace_back( Coordinate{ row, col } ), rows.push_back( row ), cols.push_back( col );
        }

        auto [ minRow, maxRow ] = minmax_element( rows.cbegin(), rows.cend() );
        auto [ minCol, maxCol ] = minmax_element( cols.cbegin(), cols.cend() );
        Grid grid( *maxRow + 1, GridLines( *maxCol + 1 ) );
        for( const auto& coord: coords )
        {
            grid[ coord.row ][ coord.col ].distance = 0;
            grid[ coord.row ][ coord.col ].id = ++id;
            for( auto row{ *minRow }; row <= *maxRow; ++row ) for( auto col{ *minCol }; col <= *maxCol; ++col )
            {
                auto distance{ abs( coord.row - row ) + abs( coord.col - col ) };
                if( grid[ row ][ col ].distance > distance )
                    grid[ row ][ col ].distance = distance,
                    grid[ row ][ col ].id = id;
                else
                if( grid[ row ][ col ].distance == distance && grid[ row ][ col ].id != id )
                    grid[ row ][ col ].id = 0;
            }
        }

        for( auto row{ *minRow }; row <= *maxRow; ++row ) for( auto col{ *minCol }; col <= *maxCol; ++col )
        {
            id = grid[ row ][ col ].id;
            if( row == *minRow || row == *maxRow || col == *minCol || col == *maxCol )
                border.insert( id );
            else
            if( border.find( id ) == border.end() )
                ++counter[ grid[ row ][ col ].id ];
        }
        ans.first = max_element( counter.begin(), counter.end(),
            []( const PII& lhs, const PII& rhs ){ return lhs.second < rhs.second; })->second;

        return ans;
    }
};


int main()
{

    Solution s;
    auto result = s.getMaxArea( INPUT );
    cout << "first: " << result.first << " second: " << result.second << endl;

    return 0;
}