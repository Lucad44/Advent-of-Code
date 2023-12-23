#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

int hike(int i, int j, std::pair<int, int> finish, std::vector<std::string> &grid, std::set<std::pair<int, int>> &visited) {
    if (i < 0 || j < 0 || i >= grid.size() || j >= grid[i].size() || grid[i][j] == '#' || i == finish.first && j == finish.second || visited.contains({i, j})) {
        return 0;
    }
    visited.insert({i, j});
    int res;
    switch (grid[i][j]) {
        case '^':
            res = hike(i - 1, j, finish, grid, visited);
            break;
        case 'v':
            res = hike(i + 1, j, finish, grid, visited);
            break;
        case '<':
            res = hike(i, j - 1, finish, grid, visited);
            break;
        case '>':
            res = hike(i, j + 1, finish, grid, visited);
            break;
        case '.':
            res = std::max(hike(i - 1, j, finish, grid, visited), 
                    std::max(hike(i + 1, j, finish, grid, visited), 
                    std::max(hike(i, j - 1, finish, grid, visited), hike(i, j + 1, finish, grid, visited))));
            break;
    }
    visited.erase(visited.find({i, j}));
    return 1 + res;
}

int main(int argc, char *argv[]) {
    std::ifstream f("input.txt");
    std::string line;
    std::vector<std::string> lines;
    while (std::getline(f, line)) {
        lines.push_back(line);
    }
    std::pair<int, int> start, finish;
    for (int j = 0; j < lines[0].size(); j++) {
        if (lines[0][j] == '.') {
            start = {0, j};
        }
        if (lines.back()[j] == '.') {
            finish = {lines.size() - 1, j};
        }
    }
    std::set<std::pair<int, int>> visited;
    int ans = hike(start.first, start.second, finish, lines, visited);
    std::cout << ans << std::endl;
    return 0;
}