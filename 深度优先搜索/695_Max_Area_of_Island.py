# -*- coding：utf-8 -*-
# &Author  AnFany

# 695_Max_Area_of_Island 岛屿的最大面积


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 利用深度优先搜索
        # 首先找到任意一个为1的陆地，利用深度优先搜索，获取与这个陆地直接或者间接相连的所有的陆地

        # 获取网格的行、列
        row, column = len(grid), len(grid[0])

        # 已经遍历过的陆地
        land_dict = {}

        # 存储岛屿的最大面积
        area_island = 0

        # 首先任意获取一个陆地
        for o in range(row):
            for l in range(column):
                if grid[o][l] == 1 and (o, l) not in land_dict:
                    # 开始深度优先搜索, 开始的需要搜索的陆地列表
                    current_land = [(o, l)]
                    land_dict[(o, l)] = 0
                    # 岛屿面积
                    island_area = 1
                    while current_land:
                        for i in current_land:
                            r, c = i
                            # 判断上、下、左、右四个方向是否是陆地
                            if r > 0:  # 上
                                if grid[r - 1][c] == 1 and (r - 1, c) not in land_dict:
                                    current_land.append((r - 1, c))
                                    land_dict[(r - 1, c)] = 0
                                    island_area += 1

                            if r < row - 1:  # 下
                                if grid[r + 1][c] == 1 and (r + 1, c) not in land_dict:
                                    current_land.append((r + 1, c))
                                    land_dict[(r + 1, c)] = 0
                                    island_area += 1

                            if c > 0:  # 左
                                if grid[r][c - 1] == 1 and (r, c - 1) not in land_dict:
                                    current_land.append((r, c - 1))
                                    land_dict[(r, c - 1)] = 0
                                    island_area += 1

                            if c < column - 1:  # 右
                                if grid[r][c + 1] == 1 and (r, c + 1) not in land_dict:
                                    current_land.append((r, c + 1))
                                    land_dict[(r, c + 1)] = 0
                                    island_area += 1

                            current_land.remove(i)

                    # 计算刚才的岛屿的面积
                    area_island = max(area_island, island_area)

        return max(0, area_island)

