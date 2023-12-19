#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

std::vector<int> gen_sequence(std::vector<int> &sequence) {
    std::vector<int> res;
    for (int i = 1; i < sequence.size(); ++i) {
        res.push_back(sequence[i] - sequence[i - 1]);
    }
    return res;
}

int main(int argc, char *argv[]) {
    std::ifstream f("input.txt");
    std::string line;
    int ans = 0;
    while (std::getline(f, line)) {
        std::vector<int> sequence;
        std::istringstream iss(line);
        int num;
        while (iss >> num) {
            sequence.push_back(num);
        }
        
        std::vector<std::vector<int>> history;
        while (!std::all_of(sequence.begin(), sequence.end(), [](int i) { return i == 0; })) {
            history.push_back(sequence);
            sequence = gen_sequence(sequence);
        }
        std::reverse(history.begin(), history.end());
        int curr = 0;
        for (auto &v: history) {
            v.push_back(v.back() + curr);
            curr = v.back();
        }
        ans += curr;
    }
    f.close();
    std::cout << ans << std::endl;
    return 0;
}