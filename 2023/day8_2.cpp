#include <iostream>
#include <map>
#include <fstream>
#include <sstream>
#include <utility>
#include <vector>
#include <numeric>

int main(int argc, char *argv[]) {
    std::map<std::string, std::pair<std::string, std::string>> network;
    std::ifstream f("input.txt");
    std::string line;
    std::string instructions;
    int i = 0;
    while (std::getline(f, line)) {
        i++;
        if (i == 2)
            continue;
        if (i == 1) {
            instructions = line;
            continue;
        }
        network[line.substr(0, 3)] = std::make_pair(line.substr(7, 3), line.substr(12, 3));
    }
    f.close();
    std::vector<std::string> currs;
    for (auto const &entry: network) {
        if (entry.first.back() == 'A')
            currs.push_back(entry.first);
    }
    std::vector<long> ans(currs.size(), 0);
    for (int i = 0; i < currs.size(); ++i) {
        while (1) {
            if (currs[i].back() == 'Z')
                break;
            for (char ch: instructions) {
                if (ch == 'L') {
                    currs[i] = network[currs[i]].first;
                }
                else {
                    currs[i] = network[currs[i]].second;
                }
                ans[i]++;
                if (currs[i].back() == 'Z')
                    break;
            }
        }
    }
    std::cout << "ans: " << std::reduce(ans.begin(), ans.end(), 1L, [](long a, long b) {return std::lcm(a, b);}) << std::endl;
    return 0;
}