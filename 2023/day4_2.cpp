#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <unordered_map>

int main(int argc, char *argv[]) {
    std::ifstream f("input.txt");
    std::string line;
    std::regex num_regex("\\d+");
    std::map<int, int> winners;
    std::map<int, int> copies;
    while (std::getline(f, line)) {
        int pipe_ind;
        for (int i = 0; i < line.length(); ++i) {
            if (line[i] == '|') {
                pipe_ind = i;
                break;
            }
        }
        std::smatch match;
        std::regex_search(line, match, num_regex);
        int game = stoi(match.str());

        std::string winning = line.substr(10, pipe_ind - 10);
        std::string have = line.substr(pipe_ind + 2);

        std::unordered_map<int, int> win_counter;
        std::sregex_iterator it_win(winning.begin(), winning.end(), num_regex);
        std::sregex_iterator end_win;
        while (it_win != end_win) {
            std::smatch match = *it_win;
            win_counter[stoi(match.str())]++;
            ++it_win;
        }

        std::unordered_map<int, int> have_counter;
        std::sregex_iterator it_have(have.begin(), have.end(), num_regex);
        std::sregex_iterator end_have;
        while (it_have != end_have) {
            std::smatch match = *it_have;
            have_counter[stoi(match.str())]++;
            ++it_have;
        }
        copies[game] = 1;
        winners[game] = 0;
        for (auto const &[k, v]: have_counter) {
            if (win_counter.contains(k)) {
                winners[game] += v;
            }
        }
    }
    int ans = 0;
    for (auto const &[k, v]: winners) {
        for (int j = 0; j < copies[k]; ++j) {
            for (int i = k + 1; i <= k + v; ++i) {
                copies[i]++;
            }
        }
    } 
    for (auto const &[k, v]: copies) {
        ans += v;
    }
    std::cout << ans;
    f.close();
    return 0;
}