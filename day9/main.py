import copy
import os
import sys

with open('input') as f:
    lines_raw = [[int(line.rstrip())] + [False] for line in f]
    lines = copy.deepcopy(lines_raw)
    print(lines)
    i = 4
    while i < len(lines) - 1:
        print(lines[i])
        i += 1
        target_sum = lines[i][0]

        x = i - 25
        y = i - 25
        while x < i:
            if lines[x][1]:
                x += 1
                continue
            while y < i:
                if y == x:
                    y += 1
                    continue
                if lines[y][1]:
                    y += 1
                    continue
                if lines[x][0] + lines[y][0] == target_sum:
                    print("Found", lines[x][0], lines[y][0], target_sum)
                    lines[x][1] = True
                    lines[y][1] = True
                y += 1
            y = i - 25
            x += 1
    print(lines[i])