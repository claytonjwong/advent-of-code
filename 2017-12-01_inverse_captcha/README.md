# Day 1. Inverse Captcha
[https://adventofcode.com/2017/day/1](https://adventofcode.com/2017/day/1)

## Part 1
The night before Christmas, one of Santa's Elves calls you in a panic.
"The printer's broken! We can't print the Naughty or Nice List!"
By the time you make it to sub-basement 17, there are only a few minutes
until midnight. "We have a big problem," she says; "there must be almost fifty bugs
in this system, but nothing else can print The List. Stand in this square, quick!
There's no time to explain; if you can convince them to pay you in stars,
you'll be able to--" She pulls a lever and the world goes blurry.

When your eyes can focus again, everything seems a lot more pixelated than before.
She must have sent you inside the computer! You check the system clock:
25 milliseconds until midnight. With that much time, you should be able
to collect all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available
on each day millisecond in the advent calendar; the second puzzle is unlocked
when you complete the first. Each puzzle grants one star. Good luck!

You're standing in a room with "digitization quarantine" written in LEDs along one wall.
The only door is locked, but it includes a small interface.
"Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to prove
you're not a human. Apparently, you only get one millisecond to solve the captcha:
too fast for a normal human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your puzzle input)
and find the sum of all digits that match the next digit in the list.
The list is circular, so the digit after the last digit is the first digit in the list.

For example:

* 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit
and the third digit (2) matches the fourth digit.
* 1111 produces 4 because each digit (all 1) matches the next.
* 1234 produces 0 because no digit matches the next.
* 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

What is the solution to your captcha? ```1222```

## Puzzle Input
```
649713959682898259577777982349515784822684939966191359164369933435366431847754488661965363557985166219358714739318371382388296151195361571216131925158492441461844687324923315381358331571577613789649166486152237945917987977793891739865149734755993241361886336926538482271124755359572791451335842534893192693558659991171983849285489139421425933638614884415896938914992732492192458636484523228244532331587584779552788544667253577324649915274115924611758345676183443982992733966373498385685965768929241477983727921279826727976872556315428434799161759734932659829934562339385328119656823483954856427365892627728163524721467938449943358192632262354854593635831559352247443975945144163183563723562891357859367964126289445982135523535923113589316417623483631637569291941782992213889513714525342468563349385271884221685549996534333765731243895662624829924982971685443825366827923589435254514211489649482374876434549682785459698885521673258939413255158196525696236457911447599947449665542554251486847388823576937167237476556782133227279324526834946534444718161524129285919477959937684728882592779941734186144138883994322742484853925383518651687147246943421311287324867663698432546619583638976637733345251834869985746385371617743498627111441933546356934671639545342515392536574744795732243617113574641284231928489312683617154536648219244996491745718658151648246791826466973654765284263928884137863647623237345882469142933142637583644258427416972595241737254449718531724176538648369253796688931245191382956961544775856872281317743828552629843551844927913147518377362266554334386721313244223233396453291224932499277961525785755863852487141946626663835195286762947172384186667439516367219391823774338692151926472717373235612911848773387771244144969149482477519437822863422662157461968444281972353149695515494992537927492111388193837553844671719291482442337761321272333982924289323437277224565149928416255435841327756139118119744528993269157174414264387573331116323982614862952264597611885999285995516357519648695594299657387614793341626318866519144574571816535351149394735916975448425618171572917195165594323552199346814729617189679698944337146
```

## Part 2
You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied,
but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list.
That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it.
Fortunately, your list has an even number of elements.

For example:

* 1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
* 1221 produces 0, because every comparison is between a 1 and a 2.
* 123425 produces 4, because both 2s match each other, but no other digit has a match.
* 123123 produces 12.
* 12131415 produces 4.

What is the solution to your new captcha? ```1238```

## Solution

```cpp
    #include <iostream>
    #include <string>
    #include "input.hpp"

    using namespace std;

    using Type = int;
    using Collection = string;

    Type next_part1( const Type i, const Type N ){
        return( i + 1 );
    }

    Type next_part2( const Type i, const Type N ){
        return( i + ( N / 2 )) % N;
    }

    template< typename Type, typename Collection >
    class Solution {
    public:
        template< typename Next >
        Type inverseCaptcha( const Collection& A, Next next, Type ans=0 ) {
            Type N = static_cast< Type >( A.size() );
            for( Type i{ 0 }, j{ next(i,N) }; i < N; ++i, j=( next(i,N) ))
                if( A[ i ] == A[ j ] )
                    ans += A[ i ] - '0';
            return ans;
        }
    };

    int main() {
        Solution< Type, Collection > solution;
        auto ans1 = solution.inverseCaptcha( INPUT, next_part1 );
        cout << "answer 1: " << ans1 << endl;
        auto ans2 = solution.inverseCaptcha( INPUT, next_part2 );
        cout << "answer 2: " << ans2 << endl;
        return 0;
    }
```
