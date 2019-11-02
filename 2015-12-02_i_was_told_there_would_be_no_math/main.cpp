/*
 * https://adventofcode.com/2015/day/2
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main() {
    auto paper = 0,
         ribbon = 0;
    auto getArea = [](int l, int w, int h) -> int {
        auto s = vector<int>{(l * w), (w * h), (h * l)}; // 3 sides
        return (s[0] << 1) + (s[1] << 1) + (s[2] << 1) + min({s[0], s[1], s[2]});
    };
    ifstream fs{"./input.txt"};
    string s;
    while (fs >> s) {
        transform(s.begin(), s.end(), s.begin(), [](auto c) { return c == 'x' ? ' ' : c; });
        istringstream parser{s};
        vector<int> d(3);
        parser >> d[0] >> d[1] >> d[2];
        auto [l, w, h] = tie(d[0], d[1], d[2]);
        paper += getArea(l, w, h);
        sort(d.begin(), d.end());
        ribbon += (d[0] << 1) + (d[1] << 1) + (l * w * h);
    }
    cout << "Answer 1: " << paper << endl
         << "Answer 2: " << ribbon << endl;
    return 0;
}
