#include <iostream>
#include "md5.hpp"

using namespace std;

int main() {
    auto suffix = [](const string& input, const int n, int index=0, string target={}) {
        fill_n(back_inserter(target), n, '0');
        for (auto i=1;; ++i) {
            auto hash = md5(input + to_string(i));
            if (hash.substr(0, n) == target) {
                index = i;
                break;
            }
        }
        return index;
    };
    cout << "Answer 1: " << suffix("ckczppom", 5) << endl
         << "Answer 2: " << suffix("ckczppom", 6) << endl;
    return 0;
}