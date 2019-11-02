#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

const unordered_set<char> vowels{'a','e','i','o','u'};

int main() {
    auto isNice1 = [](const string& s) -> bool {
        auto cnt = 0;
        auto pre = '\0',
             cur = '\0';
        auto found = false;
        for (auto c: s) {
            if (vowels.find(c) != vowels.end())
                ++cnt;
            pre = cur;
            cur = c;
            if (pre == cur)
                found = true;
            else if ((pre == 'a' && cur == 'b') || (pre == 'c' && cur == 'd') || (pre == 'p' && cur == 'q') || (pre == 'x' && cur == 'y'))
                return false;
        }
        return cnt >= 3 && found;
    };
    auto isNice2 = [](const string& s) -> bool {
        auto match = false,
             repeat = false;
        unordered_map<string, int> kmer; // track last index of each unique kmer seen
        for (auto i=0; i + 1 < s.size(); ++i) {
            auto key = s.substr(i, 2);
            if (kmer.find(key) == kmer.end())
                kmer[key] = i;
            else if (i - kmer[key] > 1)
                match = true;
        }
        for (auto i=2; i < s.size(); ++i)
            if (s[i - 2] == s[i])
                repeat = true;
        return match && repeat;
    };
    auto cnt1 = 0,
         cnt2 = 0;
    fstream fs{"./input.txt"};
    string s;
    while (fs >> s) {
        if (isNice1(s))
            ++cnt1;
        if (isNice2(s))
            ++cnt2;
    }
    cout << "Answer 1: " << cnt1 << endl
         << "Answer 2: " << cnt2 << endl;
    return 0;
}