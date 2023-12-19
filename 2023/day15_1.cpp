#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>

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
    std::cout << sequence << std::endl;
    int ans = 0;
    for (const std::string &s: steps) {
        int curr = 0;
        for (char ch: s) {
            curr += ch;
            curr *= 17;
            curr %= 256;
        }
        std::cout << s << ": " << curr << std::endl;
        ans += curr;
    }
    std::cout << ans << std::endl;
    return 0;
}