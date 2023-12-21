#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <deque>
#include <tuple>


std::set<std::tuple<int, int, int>> walk(int i, int j, std::vector<std::string> &garden, int steps) {
    int m = garden.size(), n = garden[0].length();
    std::set<std::tuple<int, int, int>> visited;
    std::vector<std::pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    std::deque<std::tuple<int, int, int>> dq = {{i, j, steps}};

    while (!dq.empty()) {
        auto [i, j, steps] = dq.front();
        dq.pop_front();
        if (visited.contains({i, j, steps}) || steps < 0)
            continue;
        visited.insert({i, j, steps});

        for (auto const &[di, dj]: directions) {
            int ni = i + di, nj = j + dj;
            if (ni >= 0 && ni < m && nj >= 0 && nj < n && garden[ni][nj] == '.') {
                dq.push_back({ni, nj, steps - 1});
            }
        }
    }
    return visited;
}

int main(int argc, char *argv[]) {
    std::ifstream f("input.txt");
    std::string line;
    std::vector<std::string> garden;
    while (std::getline(f, line)) {
        garden.push_back(line);
    }
    std::set<std::tuple<int, int, int>> res;
    for (int i = 0; i < garden.size(); ++i) {
        for (int j = 0; j < garden[0].length(); ++j) {
            if (garden[i][j] == 'S') {
                res = walk(i, j, garden, 64);
                res.insert({i, j, 0});
            }
        }
    }
    int ans = 0;
    for (auto const &[i, j, steps]: res) {
        if (steps == 0) {
            std::cout << "(" << i << ", " << j << ")" << '\n';
            ans++;
        }
    }
    std::cout << "ans: " << ans << std::endl;
    f.close();
    return 0;
}