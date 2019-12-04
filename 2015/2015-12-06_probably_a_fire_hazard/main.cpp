/*
 * https://adventofcode.com/2015/day/6
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;
using VI = vector<int>;
using VVI = vector<VI>;

int main() {
    auto coord = [](auto s, string x={}, string y={}) -> pair<int, int> {
        transform(s.begin(), s.end(), s.begin(), [](auto c) { return c == ',' ? ' ' : c; });
        istringstream parser{s};
        parser >> x >> y;
        return {stoi(x), stoi(y)};
    };
    VVI A(1000, VI(1000));
    auto mod_A = [](auto& cell, const auto& cmd, const auto& action) -> void {
        if (cmd == "turn")
            cell = action == "on" ? 1 : 0;
        if (cmd == "toggle")
            cell ^= 1;
    };
    VVI B(1000, VI(1000));
    auto mod_B = [](auto& cell, const auto& cmd, const auto& action) -> void {
        if (cmd == "turn")
            cell += action == "on" ? 1 : cell > 0 ? -1 : 0; // increase/decrease total by 1 (minimum of zero)
        if (cmd == "toggle")
            cell += 2;
    };
    fstream fs{"./input.txt"};
    for (string line, cmd, action, beg, end, _; getline(fs, line); ) {
        istringstream parser{line};
        parser >> cmd;
        if (cmd == "turn")   parser >> action >> beg >> _ >> end;
        if (cmd == "toggle") parser >>           beg >> _ >> end;
        auto [x1, y1] = coord(beg);
        auto [x2, y2] = coord(end);
        for (auto i=x1; i <= x2; ++i)
            for (auto j=y1; j <= y2; ++j)
                mod_A(A[i][j], cmd, action),
                mod_B(B[i][j], cmd, action);
    }
    auto cnt = 0;
    for (auto& row: A)
        cnt += count_if(row.begin(), row.end(), [](auto cell) { return cell == 1; });
    cout << "Answer 1: " << cnt << endl;
    auto total = 0;
    for (auto& row: B)
        total += accumulate(row.begin(), row.end(), 0);
    cout << "Answer 2: " << total << endl;
    return 0;
}
