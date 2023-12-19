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
        std::istringstream iss(line);
        if (i == 1) {
            instructions = line;
            continue;
        }
        network[line.substr(0, 3)] = std::make_pair(line.substr(7, 3), line.substr(12, 3));
    }
    f.close();

    std::string curr = "AAA";
    int ans = 0;
    while (1) {
        if (curr == "ZZZ")
            break;
        for (char ch: instructions) {
            if (ch == 'L') {
                curr = network[curr].first;
            }
            else {
                curr = network[curr].second;
            }
            ans++;
            if (curr == "ZZZ")
                break;
        }
    }
    std::cout << "ans: " << ans << std::endl;
    return 0;
}