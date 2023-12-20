#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>

int HASH(const std::string &s) {
    int curr = 0;
    for (char ch: s) {
        curr += ch;
        curr *= 17;
        curr %= 256;
    }
    return curr;
}

int main(int argc, char *argv[]) {
    std::ifstream f("input.txt");
    std::stringstream buffer;
    buffer << f.rdbuf();
    f.close();
    std::string sequence = buffer.str();
    sequence.erase(std::remove(sequence.begin(), sequence.end(), '\n'), sequence.cend());
    std::istringstream iss(sequence);
    std::vector<std::string> steps;
    std::string token;
    while (std::getline(iss, token, ',')) {
        steps.push_back(token);
    }

    std::map<int, std::unordered_map<std::string, int>> boxes;
    for (const std::string &s: steps) {
        std::string hashee = "";
        for (int i = 0; s[i] != '=' && s[i] != '-'; ++i) {
            hashee += s[i];
        }
        int hashed = HASH(hashee);
        if (s[hashee.length()] == '=') {
            boxes[hashed][hashee] = s[hashee.length() + 1] - '0'; 
        }
        else {
            auto it = boxes[hashed].find(hashee);
            if (it != boxes[hashed].end()) {
                boxes[hashed].erase(it);
            }
        }
    }
    int ans = 0;
    for (auto const &m: boxes) {
        int i = m.second.size();
        for (auto const &[k, v]: m.second) {
            ans += (m.first + 1) * i * v;
            --i;
        }
    }
    std::cout << ans << std::endl;
    return 0;
}