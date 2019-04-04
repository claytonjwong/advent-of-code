# Day 4. High Entropy Passphrases
[https://adventofcode.com/2017/day/4](https://adventofcode.com/2017/day/4)

## Part 1
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

* aa bb cc dd ee is valid.
* aa bb cc dd aa is not valid - the word aa appears more than once.
* aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid? ```383```

## Part 2
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

* abcde fghij is a valid passphrase.
* abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
* a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
* oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid? ```265```

## Solution

```cpp
    #include <iostream>
    #include <sstream>
    #include <iterator>
    #include <algorithm>
    #include <vector>
    #include <unordered_set>
    #include "input.hpp"

    using namespace std;

    using Collection = vector< string >;
    using Set = unordered_set< string >;
    using Iter = istream_iterator< string >;

    bool isValid_part1( const string& words ){
        Collection A;
        istringstream stream{ words };
        copy( Iter( stream ), Iter(), back_inserter( A ));
        Set S{ A.begin(), A.end() };
        return A.size() == S.size();
    }

    bool isValid_part2( const string& words ){
        Collection A;
        istringstream stream{ words };
        copy( Iter( stream ), Iter(), back_inserter( A ));
        for( auto& word: A )
            sort( word.begin(), word.end() );
        Set S{ A.begin(), A.end() };
        return A.size() == S.size();
    }

    class Solution {
    public:
        template< typename IsValid >
        int numValid( const string& input, IsValid isValid, int cnt=0 ){
            istringstream stream{ input };
            for( string line; getline( stream, line ); )
                if( isValid( line ))
                    ++cnt;
            return cnt;
        }
    };

    int main() {
        Solution solution;
        auto ans1 = solution.numValid( INPUT, isValid_part1 );
        cout << ans1 << endl;
        auto ans2 = solution.numValid( INPUT, isValid_part2 );
        cout << ans2 << endl;
        return 0;
    }
```
