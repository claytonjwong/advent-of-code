//
// Created by Clayton Wong on 2018-12-16.
//

#include <iostream>
#include <vector>
#include <memory>


using namespace std;
using Register = vector< int >;
ostream& operator<<( ostream& os, const Register& R )
{
    if( R.size() == 4 )
        os << "R[ 0 ] = " << R[ 0 ] << endl
           << "R[ 1 ] = " << R[ 1 ] << endl
           << "R[ 2 ] = " << R[ 2 ] << endl
           << "R[ 3 ] = " << R[ 3 ] << endl;
   return os;
}
class Command
{
protected:
    const int A{ 0 }, B{ 0 }, C{ 0 };
public:
    Command( const int a, const int b, const int c ) : A{ a }, B{ b }, C{ c }{ }
    virtual Register execute( const Register& input ) const noexcept { return {}; }
};
using CommandSet = vector< shared_ptr< Command > >; // opcode is the index [0:15] ( size() == 16 )
using Iter = vector< shared_ptr< Command > >::const_iterator;


class AddRegister : public Command // stores into register C the result of adding register A and register B
{
public:
    AddRegister( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ] = R[ A ] + R[ B ]; return R;
    }
};

class AddImmediate : public Command // stores into register C the result of adding register A and value B
{
public:
    AddImmediate( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ] = R[ A ] + B; return R;
    }
};

class MultiplyRegister : public Command // stores into register C the result of multiplying register A and register B
{
public:
    MultiplyRegister( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ] = R[ A ] * R[ B ]; return R;
    }
};

class MultiplyImmediate : public Command // stores into register C the result of multiplying register A and value B
{
public:
    MultiplyImmediate( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ] = R[ A ] * B; return R;
    }
};

class BitwiseAndRegister : public Command // stores into register C the result of the bitwise AND of register A and register B
{
public:
    BitwiseAndRegister( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ] = R[ A ] & R[ B ]; return R;
    }
};

class BitwiseAndImmediate : public Command // stores into register C the result of the bitwise AND of register A and value B
{
public:
    BitwiseAndImmediate( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ] = R[ A ] & B; return R;
    }
};

class BitwiseOrRegister : public Command // stores into register C the result of the bitwise OR of register A and register B
{
public:
    BitwiseOrRegister( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ] = R[ A ] | R[ B ]; return R;
    }
};

class BitwiseOrImmediate : public Command // stores into register C the result of the bitwise OR of register A and value B
{
public:
    BitwiseOrImmediate( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ] = R[ A ] | B; return R;
    }
};

class SetRegister : public Command // copies the contents of register A into register C. (Input B is ignored.)
{
public:
    SetRegister( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ] = R[ A ]; return R;
    }
};

class SetImmediate : public Command // stores value A into register C. (Input B is ignored.)
{
public:
    SetImmediate( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ] = A; return R;
    }
};

class GreaterImmediateRegister : public Command // sets register C to 1 if value A is greater than register B.
{                                                   // Otherwise, register C is set to 0
public:
    GreaterImmediateRegister( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ]=( A > R[ B ] )? 1 : 0; return R;
    }
};

class GreaterRegisterImmediate : public Command // sets register C to 1 if register A is greater than value B
{                                                   // Otherwise, register C is set to 0
public:
    GreaterRegisterImmediate( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ]=( R[ A ] > B )? 1 : 0; return R;
    }
};

class GreaterRegisterRegister : public Command // sets register C to 1 if register A is greater than register B
{                                                   // Otherwise, register C is set to 0.
public:
    GreaterRegisterRegister( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ]=( R[ A ] > R[ B ] )? 1 : 0; return R;
    }
};

class EqualImmediateRegister : public Command // sets register C to 1 if value A is equal to register B.
{                                             // Otherwise, register C is set to 0
public:
    EqualImmediateRegister( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ]=( A == R[ B ] )? 1 : 0; return R;
    }
};

class EqualRegisterImmediate : public Command // sets register C to 1 if register A is equal to value B
{                                             // Otherwise, register C is set to 0
public:
    EqualRegisterImmediate( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ]=( R[ A ] == B )? 1 : 0; return R;
    }
};

class EqualRegisterRegister : public Command // sets register C to 1 if register A is equal to register B
{                                                   // Otherwise, register C is set to 0.
public:
    EqualRegisterRegister( const int a, const int b, const int c ) : Command{ a,b,c }{ }
    Register execute( const Register& input ) const noexcept override
    {
        Register R{ input }; R[ C ]=( R[ A ] == R[ B ] )? 1 : 0; return R;
    }
};


class CommandSuite
{
    CommandSet commands_;

public:

    CommandSuite( const int a, const int b, const int c ) noexcept
    {
        commands_.emplace_back( make_shared< AddRegister >( a,b,c ) );
        commands_.emplace_back( make_shared< AddImmediate >( a,b,c ) );
        commands_.emplace_back( make_shared< MultiplyRegister >( a,b,c ) );
        commands_.emplace_back( make_shared< MultiplyImmediate >( a,b,c) );
        commands_.emplace_back( make_shared< BitwiseAndRegister >( a,b,c) );
        commands_.emplace_back( make_shared< BitwiseAndImmediate >( a,b,c) );
        commands_.emplace_back( make_shared< BitwiseOrRegister >( a,b,c) );
        commands_.emplace_back( make_shared< BitwiseOrImmediate >( a,b,c) );
        commands_.emplace_back( make_shared< SetRegister >( a,b,c) );
        commands_.emplace_back( make_shared< SetImmediate >( a,b,c) );
        commands_.emplace_back( make_shared< GreaterImmediateRegister >( a,b,c) );
        commands_.emplace_back( make_shared< GreaterRegisterImmediate >( a,b,c) );
        commands_.emplace_back( make_shared< GreaterRegisterRegister >( a,b,c) );
        commands_.emplace_back( make_shared< EqualImmediateRegister >( a,b,c) );
        commands_.emplace_back( make_shared< EqualRegisterImmediate >( a,b,c) );
        commands_.emplace_back( make_shared< EqualRegisterRegister >( a,b,c) );
    }

    Iter begin(){ return commands_.begin(); }
    Iter end(){ return commands_.end(); }
};


int main()
{
    Register input{ 3, 0, 7, 0 };
    Register target{  3, 0, 7, 2 };
    int A{ 0 }, B{ 2 }, C{ 3 };

    CommandSuite commandSuite{ A,B,C };
    for( auto command: commandSuite )
    {
        Register output = command->execute( input );

        if( output == target )
        {
            cout << "match! " << endl << output << endl;
        }
        else
        {
            cout << "no match!" << endl << output << endl;
        }
    }

    return 0;
}