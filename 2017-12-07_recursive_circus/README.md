# Day 7. Recursive Circus
[https://adventofcode.com/2017/day/7](https://adventofcode.com/2017/day/7)

## Part 1
Wandering further through the circuits of the computer, you come upon a tower of programs that have gotten themselves into a bit of trouble. A recursive algorithm has gotten out of hand, and now they're balanced precariously in a large tower.

One program at the bottom supports the entire tower. It's holding a large disc, and on the disc are balanced several more sub-towers. At the bottom of these sub-towers, standing on the bottom disc, are other programs, each holding their own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many programs stand simply keeping the disc below them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these towers. You ask each program to yell out their name, their weight, and (if they're holding a disc) the names of the programs immediately above them balancing on that disc. You write this information down (your puzzle input). Unfortunately, in their panic, they don't do this in an orderly fashion; by the time you're done, you're not sure which program gave which information.

For example, if your list is the following:
```
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
```
...then you would be able to recreate the structure of the towers that looks like this:
```
                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth
```
In this example, tknk is at the bottom of the tower (the bottom program), and is holding up ugml, padx, and fwft. Those programs are, in turn, holding up other programs; in this example, none of those programs are holding up any other programs, and are all the tops of their own towers. (The actual tower balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information is correct. What is the name of the bottom program? ```airlri```

## Part 2
The programs explain the situation: they can't get down. Rather, they could get down, if they weren't expending all of their energy trying to keep the tower balanced. Apparently, one program has the wrong weight, and until it's fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms a sub-tower. Each of those sub-towers are supposed to be the same weight, or the disc itself isn't balanced. The weight of a tower is the sum of the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and all programs above it must each match. This means that the following sums must all be the same:

* ```ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251```
* ```padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243```
* ```fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243```

As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the towers balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower? ```1206```

## Solution

```cpp
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
```
