# -*- coding: utf-8 -*-
# @Time   :2022/12/10 下午3:41
# @Author :Suer
# @File   :game_stats.py

class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        #在任何时候都不应重置最高得分
        self.high_score = 0
        filename = 'high_score.txt'
        with open(filename) as file_object:
            self.highestscore = file_object.read()
        self.high_score = int(self.highestscore)

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1