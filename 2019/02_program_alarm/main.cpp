/*
 * Day 2: 1202 Program Alarm
 *
 * Q: https://adventofcode.com/2019/day/2
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-2-1202-program-alarm
 */
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;
using VI = vector<int>;

int main() {
    auto gravityAssist = [](int noun, int verb, VI A) {
        A[1] = noun, A[2] = verb;
        for (auto i=0; i < A.size(); i += 4) {
            auto [op, u, v, w] = tie(A[i], A[i+1], A[i+2], A[i+3]);
            if (op == 99)
                break;
            if (op == 1) A[w] = A[u] + A[v];
            if (op == 2) A[w] = A[u] * A[v];
        }
        return A[0];
    };
    fstream file{"input.txt"};
    string input; file >> input;
    transform(input.begin(), input.end(), input.begin(), [](auto c) { return c == ',' ? ' ' : c; });
    stringstream stream{input};
    VI A; copy(istream_iterator<int>(stream), istream_iterator<int>(), back_inserter(A));
    cout << "Part 1: " << gravityAssist(12, 2, A) << endl;
    for (auto i=0; i < 100; ++i)
        for (auto j=0; j < 100; ++j)
            if (gravityAssist(i, j, A) == 19690720)
                cout << "Part 2: " << i << j << endl;
    return 0;
}
// Part 1: 5098658
// Part 2: 5064
