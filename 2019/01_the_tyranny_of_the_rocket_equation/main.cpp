/*
 * Day 1: The Tyranny of the Rocket Equation
 *
 * Q: https://adventofcode.com/2019/day/1
 * A: https://www.reddit.com/r/adventofcode/comments/e51aqm/2019_day_1_javascript_solution/
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <numeric>

using namespace std;
using VI = vector<int>;

auto f = [](auto x) { return (x / 3) - 2; };

int go(int x) {
    return f(x) <= 0 ? 0 : f(x) + go(f(x));
}

int main() {
    int x=0; VI A={};
    fstream input{"input.txt"};
    for (string word; input >> word; ) {
         istringstream parser{word}; parser >> x, A.push_back(x);
    }
    auto part1 = [&](auto A) {
        transform(A.begin(), A.end(), A.begin(), [&](auto x) { return f(x); });
        return accumulate(A.begin(), A.end(), 0);
    };
    auto part2 = [&](auto A) {
        transform(A.begin(), A.end(), A.begin(), [&](auto x) { return go(x); });
        return accumulate(A.begin(), A.end(), 0);
    };
    cout << "Part 1: " << part1(A) << endl
         << "Part 2: " << part2(A) << endl;
    return 0;
}

// Part 1: 3376997
// Part 2: 5062623
