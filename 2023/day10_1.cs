using System;

namespace day10_1 {
    class Solution {
        static void Main(string[] args) {
            List<string> pipes = new List<string>();
            var lines = File.ReadLines("input.txt");
            foreach (string line in lines) {
                pipes.Add(line);
            }
            int sRow = 0, sCol = 0;
            for (int i = 0; i < pipes.Count; i++) {
                int ind = pipes[i].IndexOf('S');
                if (ind != -1) {
                    sRow = i;
                    sCol = ind;
                    break;
                }
            }

            int findLength(int i, int j, char dir) {
                int curr = 1;
                while (i >= 0 && i < pipes.Count && j >= 0 && j < pipes[0].Length) {
                    switch (pipes[i][j]) {
                        case '|':
                            if (dir == 'd') {
                                i++;
                            }
                            else if (dir == 'u') {
                                i--;
                            }
                            else {
                                return -1;
                            }
                            break;
                        case '-':
                            if (dir == 'l') {
                                j--;
                            }
                            else if (dir == 'r') {
                                j++;
                            }
                            else {
                                return -1;
                            }
                            break;
                        case 'L':
                            if (dir == 'd') {
                                j++;
                                dir = 'r';
                            }
                            else if (dir == 'l') {
                                i--;
                                dir = 'u';
                            }
                            else {
                                return -1;
                            }
                            break;
                        case 'J':
                            if (dir == 'd') {
                                j--;
                                dir = 'l';
                            }
                            else if (dir == 'r') {
                                i--;
                                dir = 'u';
                            }
                            else {
                                return -1;
                            }
                            break;
                        case '7':
                            if (dir == 'r') {
                                i++;
                                dir = 'd';
                            }
                            else if (dir == 'u') {
                                j--;
                                dir = 'l';
                            }
                            else {
                                return -1;
                            }
                            break;
                        case 'F':
                            if (dir == 'l') {
                                i++;
                                dir = 'd';
                            }
                            else if (dir == 'u') {
                                j++;
                                dir = 'r';
                            }
                            else {
                                return -1;
                            }
                            break;
                        case '.':
                            return -1;
                        case 'S':
                            return curr;
                        default:
                            break;
                    }
                    curr++;
                }
                return -1;
            }
            
            int ans = Math.Max(findLength(sRow - 1, sCol, 'u'),
                            Math.Max(findLength(sRow + 1, sCol, 'd'),
                            Math.Max(findLength(sRow, sCol - 1, 'l'), findLength(sRow, sCol + 1, 'r'))));
            Console.WriteLine(ans / 2);
        }
    }
}