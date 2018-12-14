//
// Created by Clayton Wong on 2018-12-13.
//

#include "Model.hpp"


using namespace std;


Model::Model( const string& input ) :
map_{ Map{ input } }
{
    init();
}


void Model::init() noexcept
{
    //
    // gather carts from the map, and replace the character representing the cart
    // with the proper piece of the map ( i.e. replace '<'/'>' with '-' and '^'/'V' with '|' )
    //
    for( size_t y{ 0 }, x{ 0 }, id{ 0 }; y < map_.size(); ++y )
    {
        for( auto line{ map_[ y ] }; ( x = line.find( Director::UP ) ) != string::npos; line = map_[ y ] )
            carts_.emplace_back( Cart{ ++id, {x,y}, Director::Direction::up } ),
            map_.set( {x,y}, '|' );

        for( auto line{ map_[ y ] }; ( x = line.find( Director::RIGHT ) ) != string::npos; line = map_[ y ] )
            carts_.emplace_back( Cart{ ++id, {x,y}, Director::Direction::right } ),
            map_.set( {x,y}, '-' );

        for( auto line{ map_[ y ] }; ( x = line.find( Director::DOWN ) ) != string::npos; line = map_[ y ] )
            carts_.emplace_back( Cart{ ++id, {x,y}, Director::Direction::down } ),
            map_.set( {x,y}, '|' );

        for( auto line{ map_[ y ] }; ( x = line.find( Director::LEFT ) ) != string::npos; line = map_[ y ] )
            carts_.emplace_back( Cart{ ++id, {x,y}, Director::Direction::left } ),
            map_.set( {x,y}, '-' );
    }
}


bool Model::isCollision() const noexcept
{
    std::set<Cart> unique{ carts_.begin(), carts_.end() };
    return unique.size() != carts_.size();
}


Position Model::getCollisionPosition() const noexcept
{
    std::multiset<Cart> duplicate{ carts_.begin(), carts_.end() };
    for( auto pre{ carts_.begin() }, cur{ next(pre) }; cur != carts_.end(); pre = cur++ )
        if( pre->getPosition() == cur->getPosition() )
            return pre->getPosition();
    return {};
}


void Model::tick() noexcept
{
    sort( carts_.begin(), carts_.end() );
    for( auto& cart: carts_ )
    {
        cart.advance( map_ );
        if( isCollision() )
            break;
    }
}