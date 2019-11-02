#include <iostream>
#include <fstream>
#include <unordered_set>

using namespace std;

struct Hash {
    const int INF = static_cast<int>(1e5 + 1);
    size_t operator()(const pair<int, int>& p) const {
        return p.first * INF + p.second;
    }
};
using Seen = unordered_set<pair<int, int>, Hash>;

class Santa {
public:
    void move(char dir) {
        switch (dir) {
            case '^': --x_; break;
            case '>': ++y_; break;
            case 'v': ++x_; break;
            case '<': --y_; break;
        }
        seen_.insert({x_, y_});
    }
    const Seen& seen() const {
        return seen_;
    }
private:
    int x_ = 0,
        y_ = 0;
    Seen seen_;
};

int main() {
    {
        Santa santa;
        fstream fs{"./input.txt"};
        for (char dir; fs >> dir; santa.move(dir));
        cout << "Answer 1: " << santa.seen().size() << endl;
    }
    {
        Santa santa,
              robot;
        fstream fs{"./input.txt"};
        for (char dir, isSanta = 1; fs >> dir; isSanta ^= 1)
            if (isSanta)
                santa.move(dir);
            else
                robot.move(dir);
        Seen all;
        all.insert(santa.seen().begin(), santa.seen().end());
        all.insert(robot.seen().begin(), robot.seen().end());
        cout << "Answer 2: " << all.size() << endl;
    }
    return 0;
}
