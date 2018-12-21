//
// Created by Clayton Wong on 2018-12-20.
//

#include "input.hpp"
#include <iostream>
#include <string>
#include <vector>


using namespace std;
using Stack = vector< int >;


int main()
{
    Stack stack;
    size_t step{ 0 }, maximum{ 0 }, threshold{ 999 }, above{ 0 };
    for( const auto character: INPUT )
        if( isalpha( character ) ) maximum = max( maximum, ++step ), above = ( step > threshold )? above + 1 : above;
        else if( '(' == character ) stack.push_back( step );
        else if( '|' == character ) step = stack.back();
        else if( ')' == character ) step = stack.back(), stack.pop_back();

    cout << "answer part 1: " << maximum << " part 2: " << above << endl;

    return 0;
}
